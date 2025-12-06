# Physical AI & Humanoid Robotics Textbook

This repository contains the source code and content for the "Physical AI & Humanoid Robotics" online textbook.

## Project Structure

- `docusaurus/`: Contains the Docusaurus project for the textbook content. The Docusaurus site has been configured with the correct GitHub Pages URL and the main navigation label has been updated from "Tutorial" to "Learning Path". The chapters currently contain outline content as placeholders.
- `backend/`: Contains the FastAPI backend for the RAG chatbot and personalization services.
- `frontend/`: Contains shared React components for authentication and other frontend features.

## Getting Started

To get started with the Docusaurus textbook locally:

1. Navigate to the `docusaurus/` directory.
2. Run `npm install` to install dependencies.
3. Run `npm start` to start the development server.

## Development Workflow

- **Specification**: `specs/001-project-structure/spec.md`
- **Implementation Plan**: `specs/001-project-structure/plan.md`
- **Tasks**: `specs/001-project-structure/tasks.md`

## Deployment

The Docusaurus site is configured for deployment to GitHub Pages. Refer to `.github/workflows/deploy.yml` for the GitHub Actions workflow.

## Contributing

Please refer to the project's [Constitution](.specify/memory/constitution.md) for core principles and guidelines.
