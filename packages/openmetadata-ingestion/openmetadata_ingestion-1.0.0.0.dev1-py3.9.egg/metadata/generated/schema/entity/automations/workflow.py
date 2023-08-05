# generated by datamodel-codegen:
#   filename:  entity/automations/workflow.json
#   timestamp: 2023-04-14T12:26:07+00:00

from __future__ import annotations

from enum import Enum
from typing import Optional

from pydantic import BaseModel, Extra, Field

from ...type import basic, entityHistory, entityReference
from ..services.connections import testConnectionResult
from ..services.connections.metadata import openMetadataConnection
from . import testServiceConnection


class WorkflowType(Enum):
    TEST_CONNECTION = 'TEST_CONNECTION'


class WorkflowStatus(Enum):
    Pending = 'Pending'
    Successful = 'Successful'
    Failed = 'Failed'
    Running = 'Running'


class Workflow(BaseModel):
    class Config:
        extra = Extra.forbid

    id: basic.Uuid = Field(
        ..., description='Unique identifier of this workflow instance.'
    )
    name: basic.EntityName = Field(..., description='Name of the workflow.')
    displayName: Optional[str] = Field(
        None, description='Display Name that identifies this workflow definition.'
    )
    description: Optional[basic.Markdown] = Field(
        None, description='Description of the test connection def.'
    )
    fullyQualifiedName: Optional[basic.FullyQualifiedEntityName] = Field(
        None, description='FullyQualifiedName same as `name`.'
    )
    workflowType: WorkflowType = Field(..., description='Type of the workflow.')
    status: Optional[WorkflowStatus] = Field(
        WorkflowStatus.Pending, description='Workflow computation status.'
    )
    request: testServiceConnection.TestServiceConnectionRequest = Field(
        ..., description='Request body for a specific workflow type'
    )
    response: Optional[testConnectionResult.TestConnectionResult] = Field(
        None, description='Response to the request.'
    )
    openMetadataServerConnection: Optional[
        openMetadataConnection.OpenMetadataConnection
    ] = None
    owner: Optional[entityReference.EntityReference] = Field(
        None, description='Owner of this workflow.'
    )
    version: Optional[entityHistory.EntityVersion] = Field(
        None, description='Metadata version of the entity.'
    )
    updatedAt: Optional[basic.Timestamp] = Field(
        None,
        description='Last update time corresponding to the new version of the entity in Unix epoch time milliseconds.',
    )
    updatedBy: Optional[str] = Field(None, description='User who made the update.')
    href: Optional[basic.Href] = Field(
        None, description='Link to the resource corresponding to this entity.'
    )
    changeDescription: Optional[entityHistory.ChangeDescription] = Field(
        None, description='Change that lead to this version of the entity.'
    )
    deleted: Optional[bool] = Field(
        False, description='When `true` indicates the entity has been soft deleted.'
    )
