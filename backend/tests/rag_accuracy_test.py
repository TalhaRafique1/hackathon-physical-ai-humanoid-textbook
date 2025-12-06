import pytest
from ..src.api.rag import query_rag_chatbot, QueryRequest, QueryResponse # Assuming relative import path

# Define a set of test queries and their expected characteristics
TEST_QUERIES = [
    {"query": "What is ROS 2?", "expected_sources": ["ros2/chapter1.md"], "expected_keywords": ["robot operating system"]},
    {"query": "How do I setup Gazebo?", "expected_sources": ["gazebo-unity/chapter1.md"], "expected_keywords": ["simulation", "installation"]},
    # Add more queries here (up to 20 for accuracy metric)
]

@pytest.mark.asyncio
async def test_rag_accuracy():
    accurate_responses = 0
    total_queries = len(TEST_QUERIES)

    # If there are not enough queries, we cannot reach 90% accuracy on 20 queries
    if total_queries < 20:
        pytest.skip(f"Not enough test queries defined ({total_queries}) to meet 90% accuracy on 20 queries.")
        
    for i, test_case in enumerate(TEST_QUERIES):
        print(f"\n--- Running test query {i+1}/{total_queries}: {test_case['query']} ---")
        request = QueryRequest(query=test_case["query"])
        
        try:
            response: QueryResponse = await query_rag_chatbot(request)
            print(f"RAG Response: {response.response}")
            print(f"RAG Sources: {response.sources}")

            # Placeholder for actual accuracy validation logic
            # This would involve more sophisticated NLP techniques or human judgment
            is_accurate = False
            if any(keyword in response.response.lower() for keyword in test_case["expected_keywords"]):
                if any(source in s for s in response.sources for source in test_case["expected_sources"]):
                    is_accurate = True
            
            if is_accurate:
                accurate_responses += 1
                print("Result: ACCURATE")
            else:
                print("Result: INACCURATE")

        except Exception as e:
            print(f"Error during RAG query: {e}")

    accuracy_percentage = (accurate_responses / total_queries) * 100
    print(f"\n--- RAG Accuracy: {accuracy_percentage:.2f}% ---")

    # Assert that accuracy meets the 90% target
    assert accuracy_percentage >= 90.0, f"RAG accuracy {accuracy_percentage:.2f}% is below 90% target."
