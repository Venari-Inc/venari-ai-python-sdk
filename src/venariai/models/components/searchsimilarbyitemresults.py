"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from typing import List, Optional
from venariai import utils


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SearchSimilarByItemResultsProducts:
    external_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('external_id') }})
    id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id') }})
    image: Optional[str] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('image') }})
    price: float = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('price') }})
    product_type: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('product_type') }})
    rank: float = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('rank') }})
    status: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('status') }})
    title: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('title') }})
    alt_text: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('alt_text') }})
    brand: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('brand') }})
    product_url: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('product_url') }})
    score: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('score') }})
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class Products:
    products: List[SearchSimilarByItemResultsProducts] = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('products') }})
    results: float = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('results') }})
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SearchSimilarByItemResults:
    products: Products = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('products') }})
    

