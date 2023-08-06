from typing import Optional
from datetime import datetime
from dataclasses import dataclass, asdict

from klu.common.models import BaseEngineModel


@dataclass
class Application(BaseEngineModel):
    guid: str
    name: str
    app_type: str
    enabled: bool

    description: Optional[str]
    model_config: Optional[dict]
    deleted: Optional[bool] = None
    updated_at: Optional[datetime] = None
    created_at: datetime = datetime.utcnow()

    @classmethod
    def _from_engine_format(cls, data: dict) -> "Application":
        app = cls(
            **{
                "updated_at": data.pop("updatedAt"),
                "created_at": data.pop("createdAt"),
            },
            **data
        )

        return app

    def _to_engine_format(self) -> dict:
        return {
            **asdict(self),
            "updatedAt": self.updated_at,
            "createdAt": self.created_at,
        }
