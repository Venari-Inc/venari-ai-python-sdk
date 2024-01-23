# Search
(*search*)

### Available Operations

* [product_data](#product_data) - Search catalog product by ID.
* [catalog_search](#catalog_search) - Catalog text search.
* [similar_by_item](#similar_by_item) - Similarity search by item.

## product_data

Search product details by internal product uuid.

### Example Usage

```python
import venariai
from venariai.models import operations

s = venariai.VenariAI(
    api_key="YOUR_API_KEY",
)


res = s.search.product_data(product_id='26d17f72-44e8-467a-8931-8867e11075a4', inference_id='491a66ec-6cf6-4fb7-a02c-7e4caa3d1942')

if res.product_with_uuid is not None:
    # handle response
    pass
```

### Parameters

| Parameter                            | Type                                 | Required                             | Description                          | Example                              |
| ------------------------------------ | ------------------------------------ | ------------------------------------ | ------------------------------------ | ------------------------------------ |
| `product_id`                         | *str*                                | :heavy_check_mark:                   | The internal product id.             | 26d17f72-44e8-467a-8931-8867e11075a4 |
| `inference_id`                       | *Optional[str]*                      | :heavy_minus_sign:                   | The inference id.                    | 491a66ec-6cf6-4fb7-a02c-7e4caa3d1942 |


### Response

**[operations.ProductDataResponse](../../models/operations/productdataresponse.md)**
### Errors

| Error Object                                 | Status Code                                  | Content Type                                 |
| -------------------------------------------- | -------------------------------------------- | -------------------------------------------- |
| errors.ProductDataResponseBody               | 400                                          | application/json                             |
| errors.ProductDataSearchResponseBody         | 403                                          | application/json                             |
| errors.ProductDataSearchResponseResponseBody | 500                                          | application/json                             |
| errors.SDKError                              | 4x-5xx                                       | */*                                          |

## catalog_search

Search product details by text query.

### Example Usage

```python
import venariai
from venariai.models import operations

s = venariai.VenariAI(
    api_key="YOUR_API_KEY",
)


res = s.search.catalog_search(query='red air jordan', limit=10)

if res.classes is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                | Type                                     | Required                                 | Description                              | Example                                  |
| ---------------------------------------- | ---------------------------------------- | ---------------------------------------- | ---------------------------------------- | ---------------------------------------- |
| `query`                                  | *str*                                    | :heavy_check_mark:                       | The text query.                          | red air jordan                           |
| `limit`                                  | *Optional[float]*                        | :heavy_minus_sign:                       | The maximum number of results to return. | 10                                       |


### Response

**[operations.CatalogSearchResponse](../../models/operations/catalogsearchresponse.md)**
### Errors

| Error Object                                   | Status Code                                    | Content Type                                   |
| ---------------------------------------------- | ---------------------------------------------- | ---------------------------------------------- |
| errors.CatalogSearchResponseBody               | 400                                            | application/json                               |
| errors.CatalogSearchSearchResponseBody         | 403                                            | application/json                               |
| errors.CatalogSearchSearchResponseResponseBody | 500                                            | application/json                               |
| errors.SDKError                                | 4x-5xx                                         | */*                                            |

## similar_by_item

Similarity search by item.

### Example Usage

```python
import venariai
from venariai.models import components

s = venariai.VenariAI(
    api_key="YOUR_API_KEY",
)

req = components.SimilarItemPayload(
    external_id='26d17f72-44e8-467a-8931-8867e11075a4',
    min_score=0.5,
)

res = s.search.similar_by_item(req)

if res.search_similar_by_item_results is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                      | Type                                                                           | Required                                                                       | Description                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `request`                                                                      | [components.SimilarItemPayload](../../models/components/similaritempayload.md) | :heavy_check_mark:                                                             | The request object to use for the request.                                     |


### Response

**[operations.SimilarByItemResponse](../../models/operations/similarbyitemresponse.md)**
### Errors

| Error Object                                   | Status Code                                    | Content Type                                   |
| ---------------------------------------------- | ---------------------------------------------- | ---------------------------------------------- |
| errors.SimilarByItemResponseBody               | 400                                            | application/json                               |
| errors.SimilarByItemSearchResponseBody         | 403                                            | application/json                               |
| errors.SimilarByItemSearchResponseResponseBody | 500                                            | application/json                               |
| errors.SDKError                                | 4x-5xx                                         | */*                                            |
