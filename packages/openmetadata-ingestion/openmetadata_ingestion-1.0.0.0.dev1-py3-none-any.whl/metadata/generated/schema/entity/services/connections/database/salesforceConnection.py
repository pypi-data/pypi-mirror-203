# generated by datamodel-codegen:
#   filename:  entity/services/connections/database/salesforceConnection.json
#   timestamp: 2023-04-14T12:26:07+00:00

from __future__ import annotations

from enum import Enum
from typing import Optional

from pydantic import BaseModel, Extra, Field

from metadata.ingestion.models.custom_pydantic import CustomSecretStr

from .. import connectionBasicType


class SalesforceType(Enum):
    Salesforce = 'Salesforce'


class SalesforceScheme(Enum):
    salesforce = 'salesforce'


class SalesforceConnection(BaseModel):
    class Config:
        extra = Extra.forbid

    type: Optional[SalesforceType] = Field(
        SalesforceType.Salesforce, description='Service Type', title='Service Type'
    )
    scheme: Optional[SalesforceScheme] = Field(
        SalesforceScheme.salesforce,
        description='SQLAlchemy driver scheme options.',
        title='Connection Scheme',
    )
    username: str = Field(
        ...,
        description='Username to connect to the Salesforce. This user should have privileges to read all the metadata in Redshift.',
        title='Username',
    )
    password: Optional[CustomSecretStr] = Field(
        None, description='Password to connect to the Salesforce.', title='Password'
    )
    securityToken: Optional[CustomSecretStr] = Field(
        None, description='Salesforce Security Token.', title='Security Token'
    )
    hostPort: Optional[str] = Field(
        None,
        description='Host and port of the Salesforce service.',
        title='Host and Port',
    )
    sobjectName: Optional[str] = Field(
        None, description='Salesforce Object Name.', title='Object Name'
    )
    databaseName: Optional[str] = Field(
        None,
        description='Optional name to give to the database in OpenMetadata. If left blank, we will use default as the database name.',
        title='Database',
    )
    connectionOptions: Optional[connectionBasicType.ConnectionOptions] = Field(
        None, title='Connection Options'
    )
    connectionArguments: Optional[connectionBasicType.ConnectionArguments] = Field(
        None, title='Connection Arguments'
    )
    supportsMetadataExtraction: Optional[
        connectionBasicType.SupportsMetadataExtraction
    ] = Field(None, title='Supports Metadata Extraction')
    supportsProfiler: Optional[connectionBasicType.SupportsProfiler] = Field(
        None, title='Supports Profiler'
    )
    supportsQueryComment: Optional[connectionBasicType.SupportsQueryComment] = Field(
        None, title='Supports Query Comment'
    )
