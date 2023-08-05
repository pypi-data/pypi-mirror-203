# generated by datamodel-codegen:
#   filename:  auth/emailRequest.json
#   timestamp: 2023-04-14T12:26:07+00:00

from __future__ import annotations

from pydantic import BaseModel, Extra, Field

from ..type import basic


class EmailRequest(BaseModel):
    class Config:
        extra = Extra.forbid

    email: basic.Email = Field(..., description='Login Email')
