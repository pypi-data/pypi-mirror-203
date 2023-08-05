# generated by datamodel-codegen:
#   filename:  security/credentials/gcsCredentials.json
#   timestamp: 2023-04-14T12:26:07+00:00

from __future__ import annotations

from typing import Union

from pydantic import BaseModel, Extra, Field

from . import gcsValues


class GCSCredentialsPath(BaseModel):
    __root__: str = Field(
        ...,
        description='Pass the path of file containing the GCS credentials info',
        title='GCS Credentials Path',
    )


class GCSCredentials(BaseModel):
    class Config:
        extra = Extra.forbid

    gcsConfig: Union[gcsValues.GcsCredentialsValues, GCSCredentialsPath] = Field(
        ...,
        description='We support two ways of authenticating to GCS i.e via GCS Credentials Values or GCS Credentials Path',
        title='GCS Credentials Configuration',
    )
