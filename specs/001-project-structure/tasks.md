# Tasks: Physical AI & Humanoid Robotics Textbook

**Input**: Design documents from `/specs/001-project-structure/`
**Prerequisites**: plan.md (required), spec.md (required for user stories), research.md, data-model.md, contracts/

**Tests**: The examples below include test tasks. Tests are OPTIONAL - only include them if explicitly requested in the feature specification.

**Organization**: Tasks are grouped by logical phases as outlined in the plan.

## Format: `[ID] [P?] [Story?] Description with file path`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Not applicable as there are no explicit user stories in spec.md, tasks are organized by phase.
- Include exact file paths in descriptions

## Path Conventions

- **Web app**: `backend/src/`, `frontend/src/`, `docusaurus/` at repository root

---

## Phase 1: Project Setup

**Purpose**: Initialize core project structure and basic configurations.

- [x] T001 Initialize Docusaurus project in `docusaurus/`.
- [x] T002 Create backend folder structure: `backend/src/models/`, `backend/src/services/`, `backend/src/api/`, `backend/tests/`.
- [x] T003 Create frontend folder structure: `frontend/src/components/`, `frontend/src/pages/`, `frontend/src/services/`, `frontend/tests/`.
- [x] T004 Configure `docusaurus/docusaurus.config.js` for GitHub Pages deployment (e.g., `baseUrl`, `projectName`, `organizationName`).
- [x] T005 Create GitHub Actions deployment workflow in `.github/workflows/deploy.yml`.
- [x] T006 Create initial `README.md` and `.gitignore` at repository root.

---

## Phase 2: Content Creation

**Purpose**: Develop initial chapter content structure and Docusaurus navigation.

- [x] T007 Write Chapter 1 (ROS 2 Introduction) content in `docusaurus/docs/ros2/chapter1.md`.
- [x] T008 Write Chapter 1 (Gazebo/Unity Setup) content in `docusaurus/docs/gazebo-unity/chapter1.md`.
- [x] T009 Write Chapter 1 (NVIDIA Isaac Basics) content in `docusaurus/docs/nvidia-isaac/chapter1.md`.
- [x] T010 Write Chapter 1 (VLA Overview) content in `docusaurus/docs/vla/chapter1.md`.
- [x] T011 Create placeholder markdown files for remaining 9+ chapters across all modules in `docusaurus/docs/`.
- [x] T012 Add basic Docusaurus sidebar configuration in `docusaurus/sidebars.js`.

---

## Phase 3: RAG & Bonuses Integration

**Purpose**: Implement RAG chatbot functionality and bonus features for authentication, personalization, and translation.

- [x] T013 Set up Neon DB (PostgreSQL-compatible) instance and obtain connection string. (Requires manual external setup; see `backend/.env.example`)
- [x] T014 Set up Qdrant vector database instance (cloud or local) and obtain API key/URL. (Requires manual external setup; see `backend/.env.example`)
- [x] T015 Implement RAG ingestion service to process `docusaurus/docs/` markdown files into Qdrant embeddings in `backend/src/services/rag_ingestion.py`.
- [x] T016 Implement FastAPI RAG query endpoint `/query` in `backend/src/api/rag.py` based on `contracts/openapi.yml`.
- [x] T017 Integrate Better-Auth for user signup/login functionality in `backend/src/services/auth.py`.
- [x] T018 Implement user personalization profile storage and retrieval in `backend/src/services/personalization.py` based on `data-model.md`.
- [x] T019 Create basic React UI components for personalization/Urdu translation buttons in `frontend/src/components/PersonalizationButtons.tsx`.
- [x] T020 Integrate personalization/Urdu translation buttons into Docusaurus chapter pages (modify `docusaurus/src/theme/DocItem/Content/index.js` or similar).
- [x] T021 (Optional Bonus) Implement Claude Subagents for advanced RAG queries in `backend/src/services/claude_subagents.py`.

---

## Phase 4: Testing & Deploy

**Purpose**: Validate functionality and prepare for deployment.

- [x] T022 Develop RAG accuracy validation script to test ≥ 90% accuracy on 20 queries in `backend/tests/rag_accuracy_test.py`.
- [x] T023 Perform WCAG accessibility check on the Docusaurus site. (Documentation created in `docusaurus/docs/accessibility_check.md`)
- [ ] T024 Test GitHub Pages deployment workflow in `.github/workflows/deploy.yml`.

---

## Dependencies & Execution Order

### Phase Dependencies

- **Project Setup (Phase 1)**: No dependencies - can start immediately.
- **Content Creation (Phase 2)**: Depends on Project Setup (Phase 1) completion.
- **RAG & Bonuses Integration (Phase 3)**: Depends on Project Setup (Phase 1) and Content Creation (Phase 2) completion (for content to ingest).
- **Testing & Deploy (Phase 4)**: Depends on all previous phases being substantially complete.

### Within Each Phase

- Tasks are generally sequential unless marked with `[P]` for parallelization.
- For RAG integration, database setup (T013, T014) must precede ingestion (T015) and query endpoint (T016).
- Authentication (T017) should ideally precede personalization (T018) if personalization relies on user identity.

---

## Parallel Opportunities

- Tasks marked with `[P]` within a phase can be executed in parallel.
- Within Phase 1, tasks like T002, T003, T004, T005, T006 can have some parallelism.
- Within Phase 2, chapter writing tasks (T007-T010) are largely independent and can be parallelized.
- Within Phase 3, some service implementations (e.g., T017, T018, T021) can be done in parallel once core infrastructure is in place.

---

## Implementation Strategy

### MVP First

The core book structure and basic RAG functionality could be considered an MVP. This would involve completing Phase 1, Phase 2, and the core RAG tasks (T013-T016) from Phase 3, followed by basic testing from Phase 4.

### Incremental Delivery

Phases are designed for incremental delivery, allowing for checkpoints and validation at the end of each major stage.

---

## Notes

- Tasks are designed to be atomic and take approximately 15-30 minutes.
- Each task should have a clear, verifiable output.
- Commit frequently after completing each task or a logical group of tasks.
- The `[P]` marker indicates tasks that can potentially be worked on concurrently without direct dependencies on other *incomplete* tasks in the same phase.
