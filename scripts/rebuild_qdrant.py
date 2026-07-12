"""Rebuild the documentation collection using the incremental bulk ingester."""

import subprocess
import sys
from pathlib import Path


if __name__ == "__main__":
    root = Path(__file__).resolve().parent.parent
    command = [
        sys.executable,
        str(root / "scripts" / "build_massive_index.py"),
        str(root / "docs"),
        "--recreate",
    ]
    raise SystemExit(subprocess.run(command).returncode)
