---
id: lesson-demo-001
title: Prefer project-bound docs for engine tasks
status: candidate
confidence: high
trigger: "A task asks about Unity behavior without naming a version."
scope: "Unity engine documentation retrieval."
guidance: "Use the Unity corpus bound to the project before considering newer Unity docs."
evidence:
  - corpus: unity-6.3
failure_modes:
  - "The user explicitly asks to compare versions."
---

# Prefer Project-Bound Docs

Unity versions can change behavior enough that newer docs may mislead an agent.
