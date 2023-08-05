# generated by datamodel-codegen:
#   filename:  email/smtpSettings.json
#   timestamp: 2023-04-14T12:26:07+00:00

from __future__ import annotations

from enum import Enum
from typing import Optional

from pydantic import BaseModel, Extra, Field


class TransportationStrategy(Enum):
    SMTP = 'SMTP'
    SMPTS = 'SMPTS'
    SMTP_TLS = 'SMTP_TLS'


class SmtpSettings(BaseModel):
    class Config:
        extra = Extra.forbid

    emailingEntity: Optional[str] = Field('OpenMetadata', description='Emailing Entity')
    supportUrl: Optional[str] = Field(
        'https://slack.open-metadata.org', description='Support Url'
    )
    enableSmtpServer: Optional[bool] = Field(
        False,
        description='If this is enable password will details will be shared on mail',
    )
    openMetadataUrl: str = Field(..., description='Openmetadata Server Endpoint')
    senderMail: str = Field(..., description='Mail of the sender')
    serverEndpoint: str = Field(..., description='Smtp Server Endpoint')
    serverPort: int = Field(..., description='Smtp Server Endpoint')
    username: str = Field(..., description='Smtp Server Username')
    password: str = Field(..., description='Smtp Server Password')
    transportationStrategy: Optional[
        TransportationStrategy
    ] = TransportationStrategy.SMTP
