# generated by datamodel-codegen:
#   filename:  entity/services/connections/dashboard/lookerConnection.json
#   timestamp: 2023-04-14T12:26:07+00:00

from __future__ import annotations

from enum import Enum
from typing import Optional, Union

from pydantic import AnyUrl, BaseModel, Extra, Field

from metadata.ingestion.models.custom_pydantic import CustomSecretStr

from .....security.credentials import githubCredentials
from .. import connectionBasicType


class LookerType(Enum):
    Looker = 'Looker'


class NoGitHubCredentials(BaseModel):
    pass

    class Config:
        extra = Extra.forbid


class LookerConnection(BaseModel):
    class Config:
        extra = Extra.forbid

    type: Optional[LookerType] = Field(
        LookerType.Looker, description='Service Type', title='Service Type'
    )
    clientId: str = Field(
        ...,
        description="User's Client ID. This user should have privileges to read all the metadata in Looker.",
        title='Client ID',
    )
    clientSecret: CustomSecretStr = Field(
        ..., description="User's Client Secret.", title='Client Secret'
    )
    hostPort: AnyUrl = Field(
        ..., description='URL to the Looker instance.', title='Host and Port'
    )
    githubCredentials: Optional[
        Union[NoGitHubCredentials, githubCredentials.GitHubCredentials]
    ] = Field(
        None,
        description='Credentials to extract the .lkml files from a repository. This is required to get all the lineage and definitions.',
        title='GitHub Credentials',
    )
    supportsMetadataExtraction: Optional[
        connectionBasicType.SupportsMetadataExtraction
    ] = Field(None, title='Supports Metadata Extraction')
