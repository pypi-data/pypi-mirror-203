# generated by datamodel-codegen:
#   filename:  entity/services/connections/mlmodel/sklearnConnection.json
#   timestamp: 2023-04-14T12:26:07+00:00

from __future__ import annotations

from enum import Enum
from typing import Optional

from pydantic import BaseModel, Extra, Field

from .. import connectionBasicType


class SklearnType(Enum):
    Sklearn = 'Sklearn'


class SklearnConnection(BaseModel):
    class Config:
        extra = Extra.forbid

    type: Optional[SklearnType] = Field(
        SklearnType.Sklearn, description='Service Type', title='Service Type'
    )
    supportsMetadataExtraction: Optional[
        connectionBasicType.SupportsMetadataExtraction
    ] = Field(None, title='Supports Metadata Extraction')
