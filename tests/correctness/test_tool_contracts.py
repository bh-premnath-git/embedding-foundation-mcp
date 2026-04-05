from python.app.schemas.contracts import ToolRequest
from python.app.services.execution_router import ExecutionRouter


def test_learn_mode_returns_structured_teaching_payload() -> None:
    router = ExecutionRouter()
    request = ToolRequest(mode="learn", level="L2", topic="cosine_similarity")

    response = router.route(request)

    assert response.mode == "learn"
    assert response.level == "L2"
    assert response.topic == "cosine_similarity"
    assert response.result["concept"] == "cosine_similarity"
    assert response.result["level"] == "L2"
    assert "core_explanation" in response.result
    assert "embedding_explanation" in response.result


def test_non_learn_mode_returns_execution_scaffold_payload() -> None:
    router = ExecutionRouter()
    request = ToolRequest(mode="compute", level="L2", topic="matrix_ops")

    response = router.route(request)

    assert response.result == {
        "message": "Execution path scaffolded.",
        "mode": "compute",
        "topic": "matrix_ops",
    }
