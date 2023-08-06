from typing import Optional
from datetime import datetime
from dataclasses import dataclass, asdict

from klu.common.models import BaseEngineModel


@dataclass
class Action(BaseEngineModel):
    guid: str
    name: str
    style: int
    prompt: str
    app_id: int
    model_id: int
    agent_type: str
    description: Optional[str]
    model_config: Optional[dict]
    experiment_id: Optional[int] = None
    updated_at: Optional[datetime] = None
    created_at: datetime = datetime.utcnow()

    @classmethod
    def _from_engine_format(cls, data: dict) -> "Action":
        app = cls(
            **{
                "app_id": data.pop("appId", None),
                "model_id": data.pop("modelId", None),
                "updated_at": data.pop("updatedAt", None),
                "created_at": data.pop("createdAt", None),
                "experiment_id": data.pop("experimentId", None),
            },
            **data
        )

        return app

    def _to_engine_format(self) -> dict:
        return {
            **asdict(self),
            "appId": self.app_id,
            "modelId": self.model_id,
            "updatedAt": self.updated_at,
            "createdAt": self.created_at,
            "experimentId": self.experiment_id,
        }


@dataclass
class PromptResponse:
    msg: str


@dataclass
class ActionPromptResponse(PromptResponse):
    feedback_url: str


@dataclass
class PlaygroundPromptResponse(PromptResponse):
    streaming: bool
    streaming_url: Optional[str] = None
