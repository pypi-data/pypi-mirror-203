# generated by datamodel-codegen:
#   filename:  analytics/webAnalyticEvent.json
#   timestamp: 2023-04-14T12:26:07+00:00

from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, Extra, Field

from ..type import basic, entityHistory, entityReference
from . import basic as basic_1


class WebAnalyticEvent(BaseModel):
    class Config:
        extra = Extra.forbid

    id: Optional[basic.Uuid] = Field(
        None, description='Unique identifier of the report.'
    )
    name: basic.EntityName = Field(..., description='Name that identifies this event.')
    fullyQualifiedName: Optional[basic.FullyQualifiedEntityName] = Field(
        None, description='FullyQualifiedName same as `name`.'
    )
    displayName: Optional[str] = Field(
        None, description='Display Name that identifies this web analytics event.'
    )
    description: Optional[basic.Markdown] = Field(
        None, description='Description of the event.'
    )
    eventType: basic_1.WebAnalyticEventType = Field(..., description='event type')
    version: Optional[entityHistory.EntityVersion] = Field(
        None, description='Metadata version of the entity.'
    )
    owner: Optional[entityReference.EntityReference] = Field(
        None, description='Owner of this report.'
    )
    updatedAt: Optional[basic.Timestamp] = Field(
        None,
        description='Last update time corresponding to the new version of the entity in Unix epoch time milliseconds.',
    )
    updatedBy: Optional[str] = Field(None, description='User who performed the update.')
    href: Optional[basic.Href] = Field(
        None, description='Link to the resource corresponding to this entity.'
    )
    changeDescription: Optional[entityHistory.ChangeDescription] = Field(
        None, description='Change that lead to this version of the entity.'
    )
    deleted: Optional[bool] = Field(
        False, description='When `true` indicates the entity has been soft deleted.'
    )
    enabled: Optional[bool] = Field(
        True, description='Weather the event is enable (i.e. data is being collected)'
    )
