# generated by datamodel-codegen:
#   filename:  entity/services/metadataService.json
#   timestamp: 2023-04-14T12:26:07+00:00

from __future__ import annotations

from enum import Enum
from typing import List, Optional, Union

from pydantic import BaseModel, Extra, Field

from ...type import basic, entityHistory, entityReference, tagLabel
from .connections import testConnectionResult
from .connections.metadata import (
    amundsenConnection,
    atlasConnection,
    metadataESConnection,
    openMetadataConnection,
)


class MetadataServiceType(Enum):
    Amundsen = 'Amundsen'
    MetadataES = 'MetadataES'
    OpenMetadata = 'OpenMetadata'
    Atlas = 'Atlas'


class MetadataConnection(BaseModel):
    class Config:
        extra = Extra.forbid

    config: Optional[
        Union[
            amundsenConnection.AmundsenConnection,
            metadataESConnection.MetadataESConnection,
            openMetadataConnection.OpenMetadataConnection,
            atlasConnection.AtlasConnection,
        ]
    ] = None


class MetadataService(BaseModel):
    class Config:
        extra = Extra.forbid

    id: basic.Uuid = Field(
        ..., description='Unique identifier of this database service instance.'
    )
    name: basic.EntityName = Field(
        ..., description='Name that identifies this database service.'
    )
    fullyQualifiedName: Optional[basic.FullyQualifiedEntityName] = Field(
        None, description='FullyQualifiedName same as `name`.'
    )
    displayName: Optional[str] = Field(
        None, description='Display Name that identifies this database service.'
    )
    serviceType: MetadataServiceType = Field(
        ...,
        description='Type of database service such as MySQL, BigQuery, Snowflake, Redshift, Postgres...',
    )
    description: Optional[basic.Markdown] = Field(
        None, description='Description of a database service instance.'
    )
    connection: Optional[MetadataConnection] = None
    pipelines: Optional[entityReference.EntityReferenceList] = Field(
        None,
        description='References to pipelines deployed for this database service to extract metadata, usage, lineage etc..',
    )
    version: Optional[entityHistory.EntityVersion] = Field(
        None, description='Metadata version of the entity.'
    )
    updatedAt: Optional[basic.Timestamp] = Field(
        None,
        description='Last update time corresponding to the new version of the entity in Unix epoch time milliseconds.',
    )
    updatedBy: Optional[str] = Field(None, description='User who made the update.')
    testConnectionResult: Optional[testConnectionResult.TestConnectionResult] = Field(
        None, description='Last test connection results for this service'
    )
    tags: Optional[List[tagLabel.TagLabel]] = Field(
        None, description='Tags for this Metadata Service.'
    )
    owner: Optional[entityReference.EntityReference] = Field(
        None, description='Owner of this database service.'
    )
    href: Optional[basic.Href] = Field(
        None, description='Link to the resource corresponding to this database service.'
    )
    changeDescription: Optional[entityHistory.ChangeDescription] = Field(
        None, description='Change that lead to this version of the entity.'
    )
    deleted: Optional[bool] = Field(
        False, description='When `true` indicates the entity has been soft deleted.'
    )
    provider: Optional[basic.ProviderType] = basic.ProviderType.user
