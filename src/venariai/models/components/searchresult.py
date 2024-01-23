"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from typing import Optional
from venariai import utils


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SearchResult:
    brand_name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('brand_name') }})
    id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id') }})
    image: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('image') }})
    product_title: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('product_title') }})
    style_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('style_id') }})
    age_group: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('age_group') }})
    release_year: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('release_year') }})
    

