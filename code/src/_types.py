from __future__ import annotations

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    from .models import PineconeIntegration
    from .vector_stores import PineconeDatabase

    ActorInputsDb: TypeAlias = PineconeIntegration
    VectorDb: TypeAlias = PineconeDatabase
