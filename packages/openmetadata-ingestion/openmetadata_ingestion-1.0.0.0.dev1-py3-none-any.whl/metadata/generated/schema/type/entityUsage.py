# generated by datamodel-codegen:
#   filename:  type/entityUsage.json
#   timestamp: 2023-04-14T12:26:07+00:00

from __future__ import annotations

from typing import List

from pydantic import BaseModel, Extra, Field

from . import entityReference, usageDetails


class EntityUsage(BaseModel):
    class Config:
        extra = Extra.forbid

    entity: entityReference.EntityReference = Field(
        ..., description='Entity for which usage is returned.'
    )
    usage: List[usageDetails.UsageDetails] = Field(
        ..., description='List usage details per day.'
    )
