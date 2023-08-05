# generated by datamodel-codegen:
#   filename:  metadataIngestion/dashboardServiceMetadataPipeline.json
#   timestamp: 2023-04-14T12:26:07+00:00

from __future__ import annotations

from enum import Enum
from typing import List, Optional

from pydantic import BaseModel, Extra, Field

from ..type import filterPattern


class DashboardMetadataConfigType(Enum):
    DashboardMetadata = 'DashboardMetadata'


class DashboardServiceMetadataPipeline(BaseModel):
    class Config:
        extra = Extra.forbid

    type: Optional[DashboardMetadataConfigType] = Field(
        DashboardMetadataConfigType.DashboardMetadata, description='Pipeline type'
    )
    dashboardFilterPattern: Optional[filterPattern.FilterPattern] = Field(
        None,
        description='Regex to exclude or include dashboards that matches the pattern.',
    )
    chartFilterPattern: Optional[filterPattern.FilterPattern] = Field(
        None, description='Regex exclude or include charts that matches the pattern.'
    )
    dataModelFilterPattern: Optional[filterPattern.FilterPattern] = Field(
        None,
        description='Regex exclude or include data models that matches the pattern.',
    )
    dbServiceNames: Optional[List] = Field(
        None,
        description='List of Database Service Name for creation of lineage',
        title='Database Service Name List',
    )
    overrideOwner: Optional[bool] = Field(
        'false',
        description='Enabling this flag will override current owner with new owner from the source,if that is fetched during metadata ingestion. Kindly make to keep it enabled, to get the owner, for first time metadata ingestion.',
        title='Override Current Owner',
    )
    markDeletedDashboards: Optional[bool] = Field(
        True,
        description='Optional configuration to soft delete dashboards in OpenMetadata if the source dashboards are deleted. Also, if the dashboard is deleted, all the associated entities like lineage, etc., with that dashboard will be deleted',
    )
    includeTags: Optional[bool] = Field(
        True, description='Optional configuration to toggle the tags ingestion.'
    )
    includeDataModels: Optional[bool] = Field(
        True,
        description='Optional configuration to toggle the ingestion of data models.',
    )
