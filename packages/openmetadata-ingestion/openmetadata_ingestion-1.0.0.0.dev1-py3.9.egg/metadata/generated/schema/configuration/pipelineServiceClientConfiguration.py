# generated by datamodel-codegen:
#   filename:  configuration/pipelineServiceClientConfiguration.json
#   timestamp: 2023-04-14T12:26:07+00:00

from __future__ import annotations

from typing import Any, Dict, Optional

from pydantic import BaseModel, Extra, Field

from . import authConfig, sslConfig


class PipelineServiceClientConfiguration(BaseModel):
    class Config:
        extra = Extra.forbid

    className: str = Field(
        ..., description='Class Name for the Pipeline Service Client.'
    )
    apiEndpoint: str = Field(
        ...,
        description='External API root to interact with the Pipeline Service Client',
    )
    hostIp: Optional[str] = Field(
        None,
        description='Pipeline Service Client host IP that will be used to connect to the sources.',
    )
    ingestionIpInfoEnabled: Optional[bool] = Field(
        False,
        description='Enable or disable the API that fetches the public IP running the ingestion process.',
    )
    metadataApiEndpoint: str = Field(
        ..., description='Metadata api endpoint, e.g., `http://localhost:8585/api`'
    )
    verifySSL: Optional[str] = Field(
        'no-ssl',
        description='Client SSL verification policy: no-ssl, ignore, validate.',
    )
    sslConfig: Optional[sslConfig.SSLConfig] = Field(
        None, description='OpenMetadata Client SSL configuration.'
    )
    authProvider: Optional[str] = Field(
        None,
        description='Auth Provider like no-auth, azure , google, okta, auth0, customOidc, openmetadata',
    )
    authConfig: Optional[authConfig.AuthConfiguration] = Field(
        None, description='Auth Provider Configuration.'
    )
    parameters: Optional[Dict[str, Any]] = Field(
        None,
        description='Additional parameters to initialize the PipelineServiceClient.',
    )
