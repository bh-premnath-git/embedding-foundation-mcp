from python.app.learning.formatter import format_learning_result
from python.app.schemas.contracts import ToolRequest, ToolResponse


class ExecutionRouter:
    def route(self, request: ToolRequest) -> ToolResponse:
        if request.mode == "learn":
            result = format_learning_result(request.topic, request.level)
        else:
            result = {
                "message": "Execution path scaffolded.",
                "mode": request.mode,
                "topic": request.topic,
            }

        return ToolResponse(
            mode=request.mode,
            level=request.level,
            topic=request.topic,
            result=result,
        )
