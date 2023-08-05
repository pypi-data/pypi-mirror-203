# generated by datamodel-codegen:
#   filename:  type/entityLineage.json
#   timestamp: 2023-04-14T12:26:07+00:00

from __future__ import annotations

from typing import List, Optional

from pydantic import BaseModel, Extra, Field

from . import basic, entityReference


class ColumnLineage(BaseModel):
    fromColumns: Optional[List[basic.FullyQualifiedEntityName]] = Field(
        None,
        description='One or more source columns identified by fully qualified column name used by transformation function to create destination column.',
    )
    toColumn: Optional[basic.FullyQualifiedEntityName] = Field(
        None,
        description='Destination column identified by fully qualified column name created by the transformation of source columns.',
    )
    function: Optional[basic.SqlFunction] = Field(
        None,
        description='Transformation function applied to source columns to create destination column. That is `function(fromColumns) -> toColumn`.',
    )


class LineageDetails(BaseModel):
    sqlQuery: Optional[basic.SqlQuery] = Field(
        None, description='SQL used for transformation.'
    )
    columnsLineage: Optional[List[ColumnLineage]] = Field(
        None,
        description='Lineage information of how upstream columns were combined to get downstream column.',
    )
    pipeline: Optional[entityReference.EntityReference] = Field(
        None, description='Pipeline where the sqlQuery is periodically run.'
    )


class Edge(BaseModel):
    class Config:
        extra = Extra.forbid

    fromEntity: basic.Uuid = Field(
        ..., description='From entity that is upstream of lineage edge.'
    )
    toEntity: basic.Uuid = Field(
        ..., description='To entity that is downstream of lineage edge.'
    )
    description: Optional[basic.Markdown] = None
    lineageDetails: Optional[LineageDetails] = Field(
        None,
        description='Optional lineageDetails provided only for table to table lineage edge.',
    )


class EntitiesEdge(BaseModel):
    class Config:
        extra = Extra.forbid

    fromEntity: entityReference.EntityReference = Field(
        ..., description='From entity that is upstream of lineage edge.'
    )
    toEntity: entityReference.EntityReference = Field(
        ..., description='To entity that is downstream of lineage edge.'
    )
    description: Optional[basic.Markdown] = None
    lineageDetails: Optional[LineageDetails] = Field(
        None,
        description='Optional lineageDetails provided only for table to table lineage edge.',
    )


class EntityLineage(BaseModel):
    class Config:
        extra = Extra.forbid

    entity: entityReference.EntityReference = Field(
        ..., description='Primary entity for which this lineage graph is created.'
    )
    nodes: Optional[List[entityReference.EntityReference]] = None
    upstreamEdges: Optional[List[Edge]] = None
    downstreamEdges: Optional[List[Edge]] = None
