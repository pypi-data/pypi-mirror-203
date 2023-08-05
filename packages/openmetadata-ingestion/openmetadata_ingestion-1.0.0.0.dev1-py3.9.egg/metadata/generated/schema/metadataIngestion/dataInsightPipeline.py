# generated by datamodel-codegen:
#   filename:  metadataIngestion/dataInsightPipeline.json
#   timestamp: 2023-04-14T12:26:07+00:00

from __future__ import annotations

from enum import Enum

from pydantic import BaseModel, Extra, Field


class DataInsightConfigType(Enum):
    dataInsight = 'dataInsight'


class DataInsightPipeline(BaseModel):
    class Config:
        extra = Extra.forbid

    type: DataInsightConfigType = Field(..., description='Pipeline type')
