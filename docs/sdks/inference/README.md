# Inference
(*inference*)

### Available Operations

* [sneaker_id](#sneaker_id) - Single image ID.
* [sneaker_id_batch](#sneaker_id_batch) - Images batch ID.
* [sneaker_id_async](#sneaker_id_async) - Single image async ID
* [sneaker_id_batch_async](#sneaker_id_batch_async) - Images batch async ID.

## sneaker_id

Identify one sneaker from a single image URL.

### Example Usage

```python
import venariai
from venariai.models import components

s = venariai.VenariAI(
    api_key="YOUR_API_KEY",
)

req = components.SneakersIDRequest(
    custom={
        'myCustomProp': 'string',
        'myCustomValue': 'string',
    },
    confidence_threshold=25,
    restrictive_mode=False,
    url='https://www.shutterstock.com/shutterstock/photos/647477452/display_1500/stock-photo-urban-teenager-legs-silhouette-wearing-sneakers-647477452.jpg',
    variants=False,
)

res = s.inference.sneaker_id(req)

if res.object is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                    | Type                                                                         | Required                                                                     | Description                                                                  |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| `request`                                                                    | [components.SneakersIDRequest](../../models/components/sneakersidrequest.md) | :heavy_check_mark:                                                           | The request object to use for the request.                                   |


### Response

**[operations.SneakerIDResponse](../../models/operations/sneakeridresponse.md)**
### Errors

| Error Object                                  | Status Code                                   | Content Type                                  |
| --------------------------------------------- | --------------------------------------------- | --------------------------------------------- |
| errors.SneakerIDResponseBody                  | 400                                           | application/json                              |
| errors.SneakerIDInferenceResponseBody         | 403                                           | application/json                              |
| errors.SneakerIDInferenceResponseResponseBody | 500                                           | application/json                              |
| errors.SDKError                               | 4x-5xx                                        | */*                                           |

## sneaker_id_batch

Identify one sneaker from an array of image URLs.

### Example Usage

```python
import venariai
from venariai.models import components

s = venariai.VenariAI(
    api_key="YOUR_API_KEY",
)

req = components.SneakersIDBatchRequest(
    custom={
        'myCustomProp': 'string',
        'myCustomValue': 'string',
    },
    confidence_threshold=25,
    restrictive_mode=False,
    urls=[
        'https://www.shutterstock.com/shutterstock/photos/647477452/display_1500/stock-photo-urban-teenager-legs-silhouette-wearing-sneakers-647477452.jpg',
        'https://www.shutterstock.com/shutterstock/photos/647477452/display_1500/stock-photo-urban-teenager-legs-silhouette-wearing-sneakers-647477452.jpg',
    ],
    listing_id='cool-sneaker-abc-123',
    variants=False,
)

res = s.inference.sneaker_id_batch(req)

if res.object is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `request`                                                                              | [components.SneakersIDBatchRequest](../../models/components/sneakersidbatchrequest.md) | :heavy_check_mark:                                                                     | The request object to use for the request.                                             |


### Response

**[operations.SneakerIDBatchResponse](../../models/operations/sneakeridbatchresponse.md)**
### Errors

| Error Object                                       | Status Code                                        | Content Type                                       |
| -------------------------------------------------- | -------------------------------------------------- | -------------------------------------------------- |
| errors.SneakerIDBatchResponseBody                  | 400                                                | application/json                                   |
| errors.SneakerIDBatchInferenceResponseBody         | 403                                                | application/json                                   |
| errors.SneakerIDBatchInferenceResponseResponseBody | 500                                                | application/json                                   |
| errors.SDKError                                    | 4x-5xx                                             | */*                                                |

## sneaker_id_async

Identify one sneaker from a single image URL and receive the response as a webhook to a provided URL.

### Example Usage

```python
import venariai
from venariai.models import components

s = venariai.VenariAI(
    api_key="YOUR_API_KEY",
)

req = components.SneakersIDAsyncRequest(
    custom={
        'myCustomProp': 'string',
        'myCustomValue': 'string',
    },
    confidence_threshold=25,
    restrictive_mode=False,
    url='https://www.shutterstock.com/shutterstock/photos/647477452/display_1500/stock-photo-urban-teenager-legs-silhouette-wearing-sneakers-647477452.jpg',
    postback_url='https://my-postback-url.com/product/123456',
)

res = s.inference.sneaker_id_async(req)

if res.object is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `request`                                                                              | [components.SneakersIDAsyncRequest](../../models/components/sneakersidasyncrequest.md) | :heavy_check_mark:                                                                     | The request object to use for the request.                                             |


### Response

**[operations.SneakerIDAsyncResponse](../../models/operations/sneakeridasyncresponse.md)**
### Errors

| Error Object                                       | Status Code                                        | Content Type                                       |
| -------------------------------------------------- | -------------------------------------------------- | -------------------------------------------------- |
| errors.SneakerIDAsyncResponseBody                  | 400                                                | application/json                                   |
| errors.SneakerIDAsyncInferenceResponseBody         | 403                                                | application/json                                   |
| errors.SneakerIDAsyncInferenceResponseResponseBody | 500                                                | application/json                                   |
| errors.SDKError                                    | 4x-5xx                                             | */*                                                |

## sneaker_id_batch_async

Identify one sneaker from an array of image URLs and receive the response as a webhook to a provided URL.

### Example Usage

```python
import venariai
from venariai.models import components

s = venariai.VenariAI(
    api_key="YOUR_API_KEY",
)

req = components.SneakersIDBatchAsyncRequest(
    custom={
        'myCustomProp': 'string',
        'myCustomValue': 'string',
    },
    confidence_threshold=25,
    restrictive_mode=False,
    postback_url='https://my-postback-url.com/product/123456',
    urls=[
        'https://www.shutterstock.com/shutterstock/photos/647477452/display_1500/stock-photo-urban-teenager-legs-silhouette-wearing-sneakers-647477452.jpg',
        'https://www.shutterstock.com/shutterstock/photos/647477452/display_1500/stock-photo-urban-teenager-legs-silhouette-wearing-sneakers-647477452.jpg',
    ],
    listing_id='cool-sneaker-abc-123',
)

res = s.inference.sneaker_id_batch_async(req)

if res.object is not None:
    # handle response
    pass
```

### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `request`                                                                                        | [components.SneakersIDBatchAsyncRequest](../../models/components/sneakersidbatchasyncrequest.md) | :heavy_check_mark:                                                                               | The request object to use for the request.                                                       |


### Response

**[operations.SneakerIDBatchAsyncResponse](../../models/operations/sneakeridbatchasyncresponse.md)**
### Errors

| Error Object                                            | Status Code                                             | Content Type                                            |
| ------------------------------------------------------- | ------------------------------------------------------- | ------------------------------------------------------- |
| errors.SneakerIDBatchAsyncResponseBody                  | 400                                                     | application/json                                        |
| errors.SneakerIDBatchAsyncInferenceResponseBody         | 403                                                     | application/json                                        |
| errors.SneakerIDBatchAsyncInferenceResponseResponseBody | 500                                                     | application/json                                        |
| errors.SDKError                                         | 4x-5xx                                                  | */*                                                     |
