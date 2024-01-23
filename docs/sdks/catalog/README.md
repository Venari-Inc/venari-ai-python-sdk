# Catalog
(*catalog*)

### Available Operations

* [catalog_item_update](#catalog_item_update) - Updates a catalog item status.
* [catalog_item_add](#catalog_item_add) - Adds an item to the catalog database.

## catalog_item_update

Updates a catalog item status.

### Example Usage

```python
import venariai
from venariai.models import operations

s = venariai.VenariAI(
    api_key="YOUR_API_KEY",
)

req = operations.CatalogItemUpdateRequestBody(
    external_id='491a66ec-6cf6-4fb7-a02c-7e4caa3d1942',
    status=operations.Status.ACTIVE,
)

res = s.catalog.catalog_item_update(req)

if res.object is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                          | Type                                                                                               | Required                                                                                           | Description                                                                                        |
| -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| `request`                                                                                          | [operations.CatalogItemUpdateRequestBody](../../models/operations/catalogitemupdaterequestbody.md) | :heavy_check_mark:                                                                                 | The request object to use for the request.                                                         |


### Response

**[operations.CatalogItemUpdateResponse](../../models/operations/catalogitemupdateresponse.md)**
### Errors

| Error Object                                        | Status Code                                         | Content Type                                        |
| --------------------------------------------------- | --------------------------------------------------- | --------------------------------------------------- |
| errors.CatalogItemUpdateResponseBody                | 400                                                 | application/json                                    |
| errors.CatalogItemUpdateCatalogResponseBody         | 403                                                 | application/json                                    |
| errors.CatalogItemUpdateCatalogResponseResponseBody | 500                                                 | application/json                                    |
| errors.SDKError                                     | 4x-5xx                                              | */*                                                 |

## catalog_item_add

Adds an item to the catalog database.

### Example Usage

```python
import venariai
from venariai.models import components

s = venariai.VenariAI(
    api_key="YOUR_API_KEY",
)

req = components.CatalogItem(
    external_id='8574528356656',
    title='1017 ALYX 9SM City Scape Tee - Black',
    product_type='T-Shirt',
    status=components.Status.ACTIVE,
    mpn='mpn-123',
    brand='Nike',
    category=[
        'Apparel',
        'Men\'s',
        'T-Shirts',
    ],
    description='This is a sample description.',
    product_url='https://test.com/product/8574528356656',
    tags=[
        '1017-alyx-9sm',
        '8818',
        'aamts0018a001-1-bl',
        'mens',
        'tee shirt',
        'tees',
        'tops',
    ],
    images=[
        components.Images(
            url='https://cdn.shopify.com/s/files/1/0814/9627/7296/products/AAMTS0018A001-1-BL-4.jpg?v=1692374837',
            alt_text='1017 ALYX 9SM City Scape Tee - Black',
            width=2000,
            height=2000,
        ),
    ],
    variants=[
        components.Variants(
            sku='98149972',
            title='XS',
            price=205,
            compare_at_price=205,
            product_code=components.ProductCode(
                type=components.Type.BARCODE,
                value='9893567872',
            ),
            position=1,
            inventory_quantity=10,
            size='XL',
        ),
    ],
)

res = s.catalog.catalog_item_add(req)

if res.object is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                        | Type                                                             | Required                                                         | Description                                                      |
| ---------------------------------------------------------------- | ---------------------------------------------------------------- | ---------------------------------------------------------------- | ---------------------------------------------------------------- |
| `request`                                                        | [components.CatalogItem](../../models/components/catalogitem.md) | :heavy_check_mark:                                               | The request object to use for the request.                       |


### Response

**[operations.CatalogItemAddResponse](../../models/operations/catalogitemaddresponse.md)**
### Errors

| Error Object                                     | Status Code                                      | Content Type                                     |
| ------------------------------------------------ | ------------------------------------------------ | ------------------------------------------------ |
| errors.CatalogItemAddResponseBody                | 400                                              | application/json                                 |
| errors.CatalogItemAddCatalogResponseBody         | 403                                              | application/json                                 |
| errors.CatalogItemAddCatalogResponseResponseBody | 500                                              | application/json                                 |
| errors.SDKError                                  | 4x-5xx                                           | */*                                              |
