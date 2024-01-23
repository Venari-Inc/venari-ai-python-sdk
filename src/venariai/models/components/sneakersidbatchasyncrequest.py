"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from typing import Any, Dict, List, Optional
from venariai import utils


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SneakersIDBatchAsyncRequest:
    listing_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('listing_id') }})
    r"""The sneaker's listing id to be asociated with the array of images."""
    postback_url: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('postback_url') }})
    r"""The URL to which the webhook will be delivered once the identification process is completed."""
    urls: List[str] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('urls') }})
    r"""The sneaker's array of image URLs. Specify a maximum of 32 urls."""
    confidence_threshold: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('confidence_threshold'), 'exclude': lambda f: f is None }})
    r"""The confidence threshold value."""
    custom: Optional[Dict[str, Any]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('custom'), 'exclude': lambda f: f is None }})
    r"""User-defined flat object to be returned in the response."""
    restrictive_mode: Optional[bool] = dataclasses.field(default=False, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('restrictive_mode'), 'exclude': lambda f: f is None }})
    r"""A boolean flag for restrictive mode."""
    

