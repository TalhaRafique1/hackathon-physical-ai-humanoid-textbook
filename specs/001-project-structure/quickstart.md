# Quickstart Guide

This guide provides basic instructions to set up and run the different components of the Physical AI & Humanoid Robotics textbook project.

## Prerequisites

-   Node.js (v20 or later)
-   Python (v3.11 or later)
-   `pip` and `npm` (or `yarn`)

## 1. Docusaurus Textbook Site

The core textbook content is served by Docusaurus.

```bash
# Navigate to the docusaurus directory
cd docusaurus

# Install dependencies
npm install

# Start the local development server
npm start
```

The site will be available at `http://localhost:3000`.

## 2. FastAPI RAG Backend

The RAG chatbot and personalization services are powered by a FastAPI backend.

```bash
# Navigate to the backend directory
cd backend

# It is recommended to create a virtual environment
python -m venv .venv
source .venv/bin/activate  # On Windows use `.venv\Scripts\activate`

# Install Python dependencies
pip install -r requirements.txt

# Run the backend server
uvicorn main:app --reload
```

The API will be available at `http://localhost:8000`, with interactive documentation at `http://localhost:8000/docs`.

## 3. Frontend Components

The shared React components for features like authentication are located in the `frontend` directory. These are typically consumed by the Docusaurus site.

To run tests or view components in isolation (e.g., with Storybook), you can work within this directory.

```bash
# Navigate to the frontend directory
cd frontend

# Install dependencies
npm install

# Run component tests
npm test
```
