# generated by datamodel-codegen:
#   filename:  metadataIngestion/pipelineServiceMetadataPipeline.json
#   timestamp: 2023-04-14T12:26:07+00:00

from __future__ import annotations

from enum import Enum
from typing import Optional

from pydantic import BaseModel, Extra, Field

from ..type import filterPattern


class PipelineMetadataConfigType(Enum):
    PipelineMetadata = 'PipelineMetadata'


class PipelineServiceMetadataPipeline(BaseModel):
    class Config:
        extra = Extra.forbid

    type: Optional[PipelineMetadataConfigType] = Field(
        PipelineMetadataConfigType.PipelineMetadata, description='Pipeline type'
    )
    includeLineage: Optional[bool] = Field(
        True,
        description='Optional configuration to turn off fetching lineage from pipelines.',
    )
    pipelineFilterPattern: Optional[filterPattern.FilterPattern] = Field(
        None, description='Regex exclude pipelines.'
    )
    markDeletedPipelines: Optional[bool] = Field(
        True,
        description='Optional configuration to soft delete Pipelines in OpenMetadata if the source Pipelines are deleted. Also, if the Pipeline is deleted, all the associated entities like lineage, etc., with that Pipeline will be deleted',
    )
    includeTags: Optional[bool] = Field(
        True, description='Optional configuration to toggle the tags ingestion.'
    )
