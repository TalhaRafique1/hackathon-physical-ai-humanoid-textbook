# Research & Decisions

This document captures the key architectural and strategic decisions made during the planning phase for the Physical AI & Humanoid Robotics textbook project.

## 1. RAG Vector Database

-   **Decision**: Use **Qdrant** as the vector database.
-   **Rationale**: Qdrant is a dedicated, high-performance vector database with a managed free tier. This provides a more scalable and robust solution compared to an in-memory library, which is essential as the textbook content and number of users grow. It offloads the complexity of vector indexing and search, allowing the backend service to remain lightweight.
-   **Alternatives Considered**:
    -   **In-memory (e.g., FAISS)**: Rejected because it does not scale well. It would require loading all embeddings into the application's memory, which could easily exceed the resource limits of free-tier cloud services and lead to slow startup times.

## 2. Content Research Strategy

-   **Decision**: Perform research **concurrently for each module**.
-   **Rationale**: A concurrent approach allows for parallel work streams, significantly speeding up the content creation phase. Subject matter experts or teams can work on different modules (ROS 2, Gazebo, NVIDIA Isaac, VLA) simultaneously without blocking each other.
-   **Alternatives Considered**:
    -   **Upfront Research**: Rejected because it would create a major bottleneck at the beginning of the project. All content creation would be stalled until the entire research phase was complete, jeopardizing the 4-6 week timeline.

## 3. Personalization Depth

-   **Decision**: Implement personalization as **simple tips and supplemental content**.
-   **Rationale**: This approach provides tangible value to the reader by showing relevant hints, links to prerequisites, or extra-challenging examples based on their profile, without adding significant complexity. It allows for a clear separation between the core content and personalized additions, making it easier to implement and maintain within the project timeline.
-   **Alternatives Considered**:
    -   **Full Chapter Rewrite**: Rejected due to excessive complexity. Dynamically rewriting entire chapters based on a user's profile would require a sophisticated content generation and management system, which is well beyond the scope of a 4-6 week project.
