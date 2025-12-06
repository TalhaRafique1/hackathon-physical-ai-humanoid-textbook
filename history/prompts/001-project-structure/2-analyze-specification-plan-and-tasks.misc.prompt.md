---
id: 2
title: Analyze Specification, Plan, and Tasks
stage: misc
date: 2025-12-06
surface: agent
model: Gemini
feature: 001-project-structure
branch: 001-project-structure
user: {{USER}}
command: /sp.analyze
labels: ["analysis", "quality-assurance", "spec-driven-development"]
links:
  spec: specs/001-project-structure/spec.md
  ticket: null
  adr: null
  pr: null
files:
  - specs/001-project-structure/spec.md
  - specs/001-project-structure/plan.md
  - specs/001-project-structure/tasks.md
tests:
  []
---

## Prompt

Perform a non-destructive cross-artifact consistency and quality analysis across spec.md, plan.md, and tasks.md after task generation.

## Response snapshot

I have outputted the analysis report and offered remediation. I am now in the phase of creating the PHR for the `/sp.analyze` command.

I checked the `history/prompts/001-project-structure` directory. There is one PHR file: `1-generate-implementation-tasks-for-textbook-project.tasks.prompt.md`.
This means the ID for my new PHR (for `/sp.analyze`) should be `2`.

**PHR Creation for `/sp.analyze`:**
1.  **Stage:** `misc` (or `explainer` - `misc` seems more appropriate for an analysis report)
2.  **Title:** `Analyze Specification, Plan, and Tasks`
3.  **Route:** `history/prompts/001-project-structure/`
4.  **Create and Fill PHR:**
    -   Read the template: `.specify/templates/phr-template.prompt.md`.
    -   Allocate an ID: `2`
    -   Compute output path: `history/prompts/001-project-structure/2-analyze-specification-plan-and-tasks.misc.prompt.md`.
    -   Fill placeholders.
    -   Write the file.

## Outcome

- ✅ Impact: Provided a detailed analysis report highlighting critical inconsistencies and underspecifications across design artifacts.
- 🧪 Tests: No automated tests were run during analysis.
- 📁 Files: Generated analysis report.
- 🔁 Next prompts: User needs to decide on remediation for critical issues, possibly running `/sp.specify` again.
- 🧠 Reflection: The primary finding was the missing content in `spec.md`, which necessitated deriving requirements from user prompts during `/sp.plan` and `/sp.tasks`. This highlights the importance of a well-defined `spec.md` for a robust SDD workflow.

## Evaluation notes (flywheel)

- Failure modes observed: None.
- Graders run and results (PASS/FAIL): n/a
- Prompt variant (if applicable): n/a
- Next experiment (smallest change to try): n/a
