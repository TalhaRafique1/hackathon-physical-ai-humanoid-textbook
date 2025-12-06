# Data Model

This document defines the key data entities for the Physical AI & Humanoid Robotics textbook project.

## Entity: User

Represents an end-user of the textbook.

| Field | Type | Description |
|---|---|---|
| `user_id` | UUID | Primary key. |
| `email` | String | User's email for authentication. |
| `auth_provider` | String | The authentication provider used (e.g., 'google', 'github'). |
| `created_at` | Timestamp | Timestamp of user creation. |

## Entity: PersonalizationProfile

Stores a user's preferences and knowledge level to tailor their learning experience.

| Field | Type | Description |
|---|---|---|
| `profile_id` | UUID | Primary key. |
| `user_id` | UUID | Foreign key to the `User` entity. |
| `knowledge_level` | Enum | User's self-assessed knowledge (e.g., 'beginner', 'intermediate', 'expert'). |
| `interests` | Array[String] | List of topics the user is interested in (e.g., ["ROS", "VLA", "Simulation"]). |
| `updated_at` | Timestamp | Timestamp of last profile update. |

## Entity: Chapter

Represents a single chapter in the textbook.

| Field | Type | Description |
|---|---|---|
| `chapter_id` | UUID | Primary key. |
| `title` | String | The title of the chapter. |
| `module` | String | The module the chapter belongs to (e.g., "ROS 2", "Gazebo/Unity"). |
| `content_md_url` | String | URL or path to the markdown file containing the chapter content. |

## Entity: RAGQuery

Logs queries made to the RAG chatbot for analytics and improvement.

| Field | Type | Description |
|---|---|---|
| `query_id` | UUID | Primary key. |
| `user_id` | UUID | Foreign key to the `User` who made the query (can be null for anonymous users). |
| `query_text` | String | The text of the user's query. |
| `response_text` | String | The generated response from the chatbot. |
| `sources` | Array[String] | List of chapter/section IDs used as sources for the response. |
| `timestamp` | Timestamp | Timestamp of when the query was made. |
