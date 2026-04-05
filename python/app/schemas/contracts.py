from typing import Any, Literal

from pydantic import BaseModel, Field


Mode = Literal["learn", "compute", "verify", "visualize", "reason"]
Level = Literal["L1", "L2", "L3", "L4"]


class ToolRequest(BaseModel):
    mode: Mode
    level: Level
    topic: str = Field(min_length=1)
    input: dict[str, Any] = Field(default_factory=dict)
    options: dict[str, Any] = Field(default_factory=dict)


class ToolResponse(BaseModel):
    mode: Mode
    level: Level
    topic: str
    result: dict[str, Any] = Field(default_factory=dict)


class HealthResponse(BaseModel):
    status: str
    service: str
