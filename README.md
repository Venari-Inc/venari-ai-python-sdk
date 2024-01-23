# openapi

<div align="left">
    <a href="https://speakeasyapi.dev/"><img src="https://custom-icon-badges.demolab.com/badge/-Built%20By%20Speakeasy-212015?style=for-the-badge&logoColor=FBE331&logo=speakeasy&labelColor=545454" /></a>
    <a href="https://opensource.org/licenses/MIT">
        <img src="https://img.shields.io/badge/License-MIT-blue.svg" style="width: 100px; height: 28px;" />
    </a>
</div>

## SDK Installation

```bash
pip install git+https://github.com/Venari-Inc/venari-ai-python-sdk.git
```
<!-- End SDK Installation [installation] -->

<!-- Start SDK Example Usage [usage] -->
## SDK Example Usage

### Example

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
<!-- End SDK Example Usage [usage] -->

<!-- Start Available Resources and Operations [operations] -->
## Available Resources and Operations

### [inference](docs/sdks/inference/README.md)

* [sneaker_id](docs/sdks/inference/README.md#sneaker_id) - Single image ID.
* [sneaker_id_batch](docs/sdks/inference/README.md#sneaker_id_batch) - Images batch ID.
* [sneaker_id_async](docs/sdks/inference/README.md#sneaker_id_async) - Single image async ID
* [sneaker_id_batch_async](docs/sdks/inference/README.md#sneaker_id_batch_async) - Images batch async ID.

### [search](docs/sdks/search/README.md)

* [product_data](docs/sdks/search/README.md#product_data) - Search catalog product by ID.
* [catalog_search](docs/sdks/search/README.md#catalog_search) - Catalog text search.
* [similar_by_item](docs/sdks/search/README.md#similar_by_item) - Similarity search by item.

### [catalog](docs/sdks/catalog/README.md)

* [catalog_item_update](docs/sdks/catalog/README.md#catalog_item_update) - Updates a catalog item status.
* [catalog_item_add](docs/sdks/catalog/README.md#catalog_item_add) - Adds an item to the catalog database.
<!-- End Available Resources and Operations [operations] -->

<!-- Start Error Handling [errors] -->
## Error Handling

Handling errors in this SDK should largely match your expectations.  All operations return a response object or raise an error.  If Error objects are specified in your OpenAPI Spec, the SDK will raise the appropriate Error type.

| Error Object                                  | Status Code                                   | Content Type                                  |
| --------------------------------------------- | --------------------------------------------- | --------------------------------------------- |
| errors.SneakerIDResponseBody                  | 400                                           | application/json                              |
| errors.SneakerIDInferenceResponseBody         | 403                                           | application/json                              |
| errors.SneakerIDInferenceResponseResponseBody | 500                                           | application/json                              |
| errors.SDKError                               | 4x-5xx                                        | */*                                           |

### Example

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

res = None
try:
    res = s.inference.sneaker_id(req)
except errors.SneakerIDResponseBody as e:
    print(e)  # handle exception
    raise(e)
except errors.SneakerIDInferenceResponseBody as e:
    print(e)  # handle exception
    raise(e)
except errors.SneakerIDInferenceResponseResponseBody as e:
    print(e)  # handle exception
    raise(e)
except errors.SDKError as e:
    print(e)  # handle exception
    raise(e)

if res.object is not None:
    # handle response
    pass
```
<!-- End Error Handling [errors] -->

<!-- Start Server Selection [server] -->
## Server Selection

### Select Server by Index

You can override the default server globally by passing a server index to the `server_idx: int` optional parameter when initializing the SDK client instance. The selected server will then be used as the default on the operations that use it. This table lists the indexes associated with the available servers:

| # | Server | Variables |
| - | ------ | --------- |
| 0 | `https://api.venari.ai` | None |

#### Example

```python
import venariai
from venariai.models import components

s = venariai.VenariAI(
    server_idx=0,
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


### Override Server URL Per-Client

The default server can also be overridden globally by passing a URL to the `server_url: str` optional parameter when initializing the SDK client instance. For example:
```python
import venariai
from venariai.models import components

s = venariai.VenariAI(
    server_url="https://api.venari.ai",
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
<!-- End Server Selection [server] -->

<!-- Start Custom HTTP Client [http-client] -->
## Custom HTTP Client

The Python SDK makes API calls using the [requests](https://pypi.org/project/requests/) HTTP library.  In order to provide a convenient way to configure timeouts, cookies, proxies, custom headers, and other low-level configuration, you can initialize the SDK client with a custom `requests.Session` object.

For example, you could specify a header for every request that this sdk makes as follows:
```python
import venariai
import requests

http_client = requests.Session()
http_client.headers.update({'x-custom-header': 'someValue'})
s = venariai.VenariAI(client: http_client)
```
<!-- End Custom HTTP Client [http-client] -->

<!-- Start Authentication [security] -->
## Authentication

### Per-Client Security Schemes

This SDK supports the following security scheme globally:

| Name      | Type      | Scheme    |
| --------- | --------- | --------- |
| `api_key` | apiKey    | API key   |

To authenticate with the API the `api_key` parameter must be set when initializing the SDK client instance. For example:
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
<!-- End Authentication [security] -->

<!-- Start SDK Installation [installation] -->
## SDK Installation

```bash
pip install git+https://github.com/Venari-Inc/venari-ai-python-sdk.git
```
<!-- End SDK Installation [installation] -->

<!-- Placeholder for Future Speakeasy SDK Sections -->

