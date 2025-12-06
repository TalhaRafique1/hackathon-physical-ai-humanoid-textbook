import os
from typing import Dict, Any, Optional, List
from uuid import UUID

class PersonalizationService:
    def __init__(self):
        # In a real scenario, this would interact with a database (e.g., Neon DB)
        self._profiles: Dict[UUID, Dict[str, Any]] = {} # In-memory mock for now

    def create_profile(self, user_id: UUID, knowledge_level: str, interests: List[str]) -> Dict[str, Any]:
        """Creates a new personalization profile for a user."""
        # Generating a dummy profile_id for mock
        profile_id = UUID(int=len(self._profiles) + 1)
        profile = {
            "profile_id": str(profile_id), # Convert UUID to string for payload
            "user_id": str(user_id),       # Convert UUID to string for payload
            "knowledge_level": knowledge_level,
            "interests": interests,
            "updated_at": "mock_timestamp"
        }
        self._profiles[profile_id] = profile
        print(f"Mocked creation of profile for user {user_id}: {profile}")
        return profile

    def get_profile(self, user_id: UUID) -> Optional[Dict[str, Any]]:
        """Retrieves a personalization profile for a user."""
        for profile in self._profiles.values():
            if UUID(profile["user_id"]) == user_id: # Convert back to UUID for comparison
                print(f"Mocked retrieval of profile for user {user_id}: {profile}")
                return profile
        print(f"Mocked: No profile found for user {user_id}")
        return None

    def update_profile(self, user_id: UUID, updates: Dict[str, Any]) -> Optional[Dict[str, Any]]:
        """Updates an existing personalization profile for a user."""
        profile = self.get_profile(user_id)
        if profile:
            profile.update(updates)
            profile["updated_at"] = "mock_timestamp_updated"
            print(f"Mocked update of profile for user {user_id}: {profile}")
            return profile
        return None

# Example usage (for testing purposes)
if __name__ == "__main__":
    service = PersonalizationService()
    user_uuid = UUID("a1b2c3d4-e5f6-7890-1234-567890abcdef")
    service.create_profile(user_uuid, "intermediate", ["ROS", "VLA"])
    service.get_profile(user_uuid)
    service.update_profile(user_uuid, {"knowledge_level": "expert"})
