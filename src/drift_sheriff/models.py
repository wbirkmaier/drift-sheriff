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
    ownership: list[OwnershipRecord] = Field(default_factory=list)


class OwnershipRecord(BaseModel):
    owner_tag: str
    repository: str
    approved_role_arns: list[str] = Field(default_factory=list)


class ResourceAttributionReport(BaseModel):
    arn: str
    resource_type: str
    actor_arn: str
    session_name: str
    source_channel: str
    classification: str
    likely_owner_repository: str | None
    ownership_fit: str
    event_ids: list[str]
    before: dict[str, str]
    after: dict[str, str]
    tags: dict[str, str]
