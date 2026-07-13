---
id: skill-candidate-demo-001
name: Route Official Docs Queries
status: candidate
confidence: medium
trigger: "The user asks a technical question that depends on official documentation."
inputs:
  - user_query
  - project_binding
workflow:
  - Detect product and version from the query.
  - Apply project binding when version is missing.
  - Select the smallest relevant corpus set.
  - Build a bounded context pack.
outputs:
  - context_pack
scripts:
  - scripts/validate_second_brain.py
eval:
  - "Unity queries route to the bound Unity version."
failure_modes:
  - "Ask for clarification when product or version is ambiguous."
---

# Route Official Docs Queries

Use this candidate workflow to keep retrieval version-aware before searching.
