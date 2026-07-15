from __future__ import annotations

from pydantic import BaseModel, Field


class ResourceState(BaseModel):
    attributes: dict[str, str] = Field(default_factory=dict)


class ResourceRecord(BaseModel):
    arn: str
    resource_type: str
    tags: dict[str, str] = Field(default_factory=dict)
    before: ResourceState
    after: ResourceState


class TrailEvent(BaseModel):
    event_id: str
    resource_arn: str
    event_name: str
    event_time: str
    actor_arn: str
    session_name: str
    source_ip: str
    user_agent: str


class FixtureBundle(BaseModel):
    resources: list[ResourceRecord]
    trail_events: list[TrailEvent]


class ResourceAttributionReport(BaseModel):
    arn: str
    resource_type: str
    actor_arn: str
    session_name: str
    source_channel: str
    classification: str
    event_ids: list[str]
    before: dict[str, str]
    after: dict[str, str]
    tags: dict[str, str]
