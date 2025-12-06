---
id: 1
title: Update Constitution for Physical AI & Humanoid Robotics
stage: constitution
date: 2025-12-05
surface: agent
model: gemini
feature: none
branch: master
user: {{USER}}
command: /sp.constitution Update the project constitution to reflect the core principles and guidelines for a textbook project on "Physical AI & Humanoid Robotics". The constitution should emphasize: 1. *Interdisciplinary Collaboration*: Stress the importance of collaboration across AI, robotics, biomechanics, cognitive science, and ethics. 2. *Ethical AI Development*: Highlight the necessity of ethical standards, human well-being, autonomy, privacy, fairness, bias detection, transparency, and accountability. 3. *Robustness & Safety Engineering*: Emphasize engineering for extreme robustness, reliability, and safety in unpredictable environments, including risk assessment and rigorous testing. 4. *Human-Robot Interaction Design*: Focus on intuitive, natural, and trustworthy human-robot interaction, considering psychological, social, and cultural factors. 5. *Continuous Learning & Adaptation*: Include the principle of systems designed to continuously learn, adapt, and improve through real-world interaction. Also, add sections for "Technical Standards" (leveraging simulation, hardware-software co-design) and "Research & Development Workflow" (iterative, hypothesis-driven, peer review, knowledge transfer). The governance section should reflect these new principles.
labels: [constitution, documentation]
links:
  spec: null
  ticket: null
  adr: null
  pr: null
files:
 - .specify/memory/constitution.md
 - .specify/templates/plan-template.md
tests:
 - "none"
---

## Prompt

/sp.constitution Update the project constitution to reflect the core principles and guidelines for a textbook project on "Physical AI & Humanoid Robotics". The constitution should emphasize: 1. *Interdisciplinary Collaboration*: Stress the importance of collaboration across AI, robotics, biomechanics, cognitive science, and ethics. 2. *Ethical AI Development*: Highlight the necessity of ethical standards, human well-being, autonomy, privacy, fairness, bias detection, transparency, and accountability. 3. *Robustness & Safety Engineering*: Emphasize engineering for extreme robustness, reliability, and safety in unpredictable environments, including risk assessment and rigorous testing. 4. *Human-Robot Interaction Design*: Focus on intuitive, natural, and trustworthy human-robot interaction, a considering psychological, social, and cultural factors. 5. *Continuous Learning & Adaptation*: Include the principle of systems designed to continuously learn, adapt, and improve through real-world interaction. Also, add sections for "Technical Standards" (leveraging simulation, hardware-software co-design) and "Research & Development Workflow" (iterative, hypothesis-driven, peer review, knowledge transfer). The governance section should reflect these new principles.

## Response snapshot

The project constitution was updated to version 1.0.0, incorporating new principles for "Physical AI & Humanoid Robotics". The `plan-template.md` was also updated to reflect these changes.

## Outcome

- ✅ Impact: Major update to the project's guiding principles.
- 🧪 Tests: No tests were run as this was a documentation update.
- 📁 Files: 2 files were modified.
- 🔁 Next prompts: none
- 🧠 Reflection: The process of updating the constitution and propagating changes to templates was successful.

## Evaluation notes (flywheel)

- Failure modes observed: none
- Graders run and results (PASS/FAIL): PASS
- Prompt variant (if applicable): null
- Next experiment (smallest change to try): n/a
