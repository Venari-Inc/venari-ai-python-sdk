"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from typing import Optional
from venariai import utils

class Status(str, Enum):
    r"""The status of the item."""
    ACTIVE = 'active'
    INACTIVE = 'inactive'
    DELETED = 'deleted'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class CatalogItemUpdateRequestBody:
    external_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('external_id'), 'exclude': lambda f: f is None }})
    r"""The internal product id."""
    status: Optional[Status] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('status'), 'exclude': lambda f: f is None }})
    r"""The status of the item."""
    


class CatalogItemUpdateStatus(str, Enum):
    r"""The status of the the operation."""
    SUCCESS = 'success'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class CatalogItemUpdateResponseBody:
    r"""Successfully updated catalog item"""
    status: Optional[CatalogItemUpdateStatus] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('status'), 'exclude': lambda f: f is None }})
    r"""The status of the the operation."""
    



@dataclasses.dataclass
class CatalogItemUpdateResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    raw_response: requests_http.Response = dataclasses.field()
    r"""Raw HTTP response; suitable for custom response parsing"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    object: Optional[CatalogItemUpdateResponseBody] = dataclasses.field(default=None)
    r"""Successfully updated catalog item"""
    

