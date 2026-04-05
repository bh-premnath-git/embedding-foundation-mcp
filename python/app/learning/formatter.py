def format_learning_result(topic: str, level: str) -> dict[str, object]:
    return {
        "concept": topic,
        "level": level,
        "core_explanation": "Teaching formatter scaffold created.",
        "embedding_explanation": "Embedding-specific explanation will be added per concept.",
        "real_world_use_cases": [],
        "worked_example": {},
        "common_mistakes": [],
        "next_topics": [],
    }
