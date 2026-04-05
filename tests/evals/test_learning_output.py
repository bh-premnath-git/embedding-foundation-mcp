from python.app.learning.formatter import format_learning_result


def test_learning_formatter_includes_expected_fields() -> None:
    result = format_learning_result("bayes_update", "L3")

    assert result["concept"] == "bayes_update"
    assert result["level"] == "L3"
    assert isinstance(result["real_world_use_cases"], list)
    assert isinstance(result["worked_example"], dict)
    assert isinstance(result["common_mistakes"], list)
    assert isinstance(result["next_topics"], list)


def test_learning_formatter_stays_embedding_aware() -> None:
    result = format_learning_result("cosine_similarity", "L2")

    assert "Embedding" in result["embedding_explanation"]
