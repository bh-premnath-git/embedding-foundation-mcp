from python.app.schemas.contracts import ToolRequest, ToolResponse
from python.app.services.execution_router import ExecutionRouter


class MCPServer:
    def __init__(self) -> None:
        self.router = ExecutionRouter()

    def handle_tool_request(self, request: ToolRequest) -> ToolResponse:
        return self.router.route(request)
