from typing import Optional
from uuid import UUID, uuid4
from datetime import datetime
from dataclasses import dataclass, field, asdict

from klu.common.models import BaseEngineModel


@dataclass
class Workspace(BaseEngineModel):
    id: int
    name: str

    project_guid: UUID = uuid4()
    updated_at: Optional[datetime] = None
    created_at: datetime = datetime.utcnow()

    @classmethod
    def _from_engine_format(cls, data: dict) -> "Workspace":
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
