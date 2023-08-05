# generated by datamodel-codegen:
#   filename:  entity/utils/entitiesCount.json
#   timestamp: 2023-04-14T12:26:07+00:00

from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, Extra, Field


class EntitiesCount(BaseModel):
    class Config:
        extra = Extra.forbid

    tableCount: Optional[int] = Field(None, description='Table Count')
    topicCount: Optional[int] = Field(None, description='Topic Count')
    dashboardCount: Optional[int] = Field(None, description='Dashboard Count')
    pipelineCount: Optional[int] = Field(None, description='Pipeline Count')
    mlmodelCount: Optional[int] = Field(None, description='MlModel Count')
    servicesCount: Optional[int] = Field(None, description='Services Count')
    userCount: Optional[int] = Field(None, description='User Count')
    teamCount: Optional[int] = Field(None, description='Team Count')
    testSuiteCount: Optional[int] = Field(None, description='Test Suite Count')
    storageContainerCount: Optional[int] = Field(
        None, description='Storage Container Count'
    )
    glossaryCount: Optional[int] = Field(None, description='Glossary Count')
    glossaryTermCount: Optional[int] = Field(None, description='Glossary Term Count')
