"""Extract reviewable lesson and skill candidates from one evidence file."""

from __future__ import annotations

import argparse
import re
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path

import yaml


@dataclass
class Evidence:
    path: Path
    frontmatter: dict
    body: str


def slugify(text: str) -> str:
    slug = re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")
    return slug[:64] or "experience"


def split_frontmatter(text: str) -> tuple[dict, str]:
    if not text.startswith("---\n"):
        return {}, text
    end = text.find("\n---\n", 4)
    if end == -1:
        return {}, text
    return yaml.safe_load(text[4:end]) or {}, text[end + 5 :]


def load_evidence(path: Path) -> Evidence:
    frontmatter, body = split_frontmatter(path.read_text(encoding="utf-8"))
    return Evidence(path=path, frontmatter=frontmatter, body=body)


def ranked_sources(body: str) -> list[dict]:
    sources = []
    blocks = re.split(r"\n###\s+\d+\.\s+", "\n" + body)
    for block in blocks[1:]:
        lines = block.strip().splitlines()
        if not lines:
            continue
        source_path = lines[0].strip()
        corpus = ""
        snippet = ""
        for line in lines:
            if line.startswith("- Corpus:"):
                corpus = line.split(":", 1)[1].strip()
            if line.startswith("- Snippet:"):
                snippet = line.split(":", 1)[1].strip()
        sources.append({"path": source_path, "corpus": corpus, "snippet": snippet})
    return sources


def evidence_title(evidence: Evidence) -> str:
    return evidence.frontmatter.get("query") or evidence.frontmatter.get("title") or evidence.path.stem.replace("-", " ")


def now_id(prefix: str, title: str) -> str:
    stamp = datetime.now(timezone.utc).strftime("%Y%m%d%H%M%S")
    return f"{prefix}-{slugify(title)}-{stamp}"


def render_markdown(frontmatter: dict, sections: list[str]) -> str:
    return "\n".join(["---", yaml.safe_dump(frontmatter, sort_keys=False).strip(), "---", "", *sections, ""])


def lesson_frontmatter(evidence: Evidence, lesson_id: str, sources: list[dict]) -> dict:
    title = evidence_title(evidence)
    return {
        "id": lesson_id,
        "title": f"Use evidence before answering: {title}",
        "status": "candidate",
        "confidence": "medium" if sources else "low",
        "trigger": title,
        "scope": "agent_response_context",
        "guidance": "Use the cited evidence paths as bounded context before answering similar tasks.",
        "evidence": [{"path": str(evidence.path), "type": "source"}],
        "failure_modes": [
            "Do not treat this candidate as active memory before review.",
            "Do not generalize beyond the cited corpus/version.",
        ],
    }


def write_lesson(evidence: Evidence, out_root: Path) -> Path:
    title = evidence_title(evidence)
    sources = ranked_sources(evidence.body)
    lesson_id = now_id("lesson", title)
    out = out_root / "memory" / "lessons" / f"{lesson_id}.md"
    out.parent.mkdir(parents=True, exist_ok=True)
    source_lines = ["## Evidence Sources", ""]
    if sources:
        for source in sources[:10]:
            source_lines.append(f"- `{source['path']}` ({source.get('corpus') or 'unknown corpus'})")
    else:
        source_lines.append(f"- `{evidence.path}`")
    out.write_text(
        render_markdown(
            lesson_frontmatter(evidence, lesson_id, sources),
            [
                f"# {title}",
                "",
                "## Candidate Guidance",
                "",
                "Use this as reviewable guidance only. Promote it after human review if it repeatedly improves agent output.",
                "",
                *source_lines,
            ],
        ),
        encoding="utf-8",
    )
    return out


def is_workflow_like(evidence: Evidence) -> bool:
    text = evidence.body.lower()
    markers = ["workflow:", "steps:", "procedure:", "checklist:", "repeatable workflow"]
    return any(marker in text for marker in markers)


def write_skill_candidate(evidence: Evidence, out_root: Path) -> Path:
    title = evidence_title(evidence)
    skill_id = now_id("skill", title)
    out = out_root / "skills" / "candidates" / skill_id / "SKILL.md"
    out.parent.mkdir(parents=True, exist_ok=True)
    frontmatter = {
        "id": skill_id,
        "name": slugify(title),
        "status": "candidate",
        "confidence": "medium",
        "trigger": title,
        "inputs": ["Evidence file", "User task context"],
        "workflow": [
            "Read the evidence.",
            "Follow the repeatable steps only when the current task matches the trigger.",
            "Record limitations or warnings before using the result.",
        ],
        "outputs": ["Reviewable task result", "Warnings when evidence is insufficient"],
        "scripts": [],
        "eval": "Run against one matching and one non-matching task before activation.",
        "failure_modes": ["Do not activate without review.", "Do not use for unrelated corpora or task types."],
        "evidence": [{"path": str(evidence.path), "type": "source"}],
    }
    out.write_text(
        render_markdown(
            frontmatter,
            [
                f"# {title}",
                "",
                "## Candidate Skill",
                "",
                "This is a generated skill candidate. Review, edit, and approve before moving it into active skills.",
            ],
        ),
        encoding="utf-8",
    )
    return out


def write_run(evidence: Evidence, out_root: Path, outputs: list[Path], warnings: list[str], decisions: list[str]) -> Path:
    run_id = now_id("extraction-run", evidence.path.stem)
    out = out_root / "memory" / "extraction-runs" / f"{run_id}.md"
    out.parent.mkdir(parents=True, exist_ok=True)
    frontmatter = {
        "id": run_id,
        "created_at": datetime.now(timezone.utc).isoformat(),
        "operator": "codex",
        "inputs": [str(evidence.path)],
        "method": "deterministic-heuristic-v1",
        "outputs": [str(path) for path in outputs],
        "review_status": "pending" if outputs else "partial",
        "warnings": warnings,
        "decisions": decisions,
    }
    out.write_text(
        render_markdown(frontmatter, ["# Extraction Run", "", "Generated reviewable candidates only."]),
        encoding="utf-8",
    )
    return out


def extract(path: Path, out_root: Path) -> tuple[list[Path], Path]:
    evidence = load_evidence(path)
    outputs = [write_lesson(evidence, out_root)]
    warnings: list[str] = []
    decisions = ["Generated candidate lesson from evidence."]
    if is_workflow_like(evidence):
        outputs.append(write_skill_candidate(evidence, out_root))
        decisions.append("Generated candidate skill because workflow-like evidence was found.")
    else:
        decisions.append("No workflow-like evidence found; skipped skill candidate.")
    run = write_run(evidence, out_root, outputs, warnings, decisions)
    return outputs, run


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path)
    parser.add_argument("--out-root", type=Path, default=Path("second-brain"))
    args = parser.parse_args(argv)
    extract(args.input, args.out_root)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
