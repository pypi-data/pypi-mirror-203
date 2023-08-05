# generated by datamodel-codegen:
#   filename:  tests/testSuite.json
#   timestamp: 2023-04-14T12:26:07+00:00

from __future__ import annotations

from enum import Enum
from typing import Any, List, Optional

from pydantic import BaseModel, Extra, Field

from ..entity.services.connections import testConnectionResult
from ..type import basic, entityHistory, entityReference


class ServiceType(Enum):
    TestSuite = 'TestSuite'


class TestSuiteConnection(BaseModel):
    config: Optional[Any] = None


class TestSuite(BaseModel):
    class Config:
        extra = Extra.forbid

    id: Optional[basic.Uuid] = Field(
        None, description='Unique identifier of this test suite instance.'
    )
    name: basic.EntityName = Field(
        ..., description='Name that identifies this test suite.'
    )
    displayName: Optional[str] = Field(
        None, description='Display Name that identifies this test suite.'
    )
    fullyQualifiedName: Optional[basic.FullyQualifiedEntityName] = Field(
        None, description='FullyQualifiedName same as `name`.'
    )
    description: basic.Markdown = Field(
        ..., description='Description of the test suite.'
    )
    tests: Optional[List[entityReference.EntityReference]] = None
    connection: Optional[TestSuiteConnection] = None
    testConnectionResult: Optional[testConnectionResult.TestConnectionResult] = None
    pipelines: Optional[entityReference.EntityReferenceList] = Field(
        None,
        description='References to pipelines deployed for this database service to extract metadata, usage, lineage etc..',
    )
    serviceType: Optional[ServiceType] = Field(
        ServiceType.TestSuite,
        description='Type of database service such as MySQL, BigQuery, Snowflake, Redshift, Postgres...',
    )
    owner: Optional[entityReference.EntityReference] = Field(
        None, description='Owner of this TestCase definition.'
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
