# SneakerIDBatchResponseBody

Successful processing of batch of image URLs


## Fields

| Field                                                          | Type                                                           | Required                                                       | Description                                                    | Example                                                        |
| -------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------- |
| `product`                                                      | [components.Product](../../models/components/product.md)       | :heavy_check_mark:                                             | N/A                                                            |                                                                |
| `custom`                                                       | Dict[str, *Any*]                                               | :heavy_minus_sign:                                             | User-defined flat object to be returned in the response.       | {"myCustomProp":"Hello!","myCustomValue":10}                   |
| `variants`                                                     | List[[components.Product](../../models/components/product.md)] | :heavy_minus_sign:                                             | N/A                                                            |                                                                |
| `confidence`                                                   | *float*                                                        | :heavy_check_mark:                                             | The inference confidence value.                                | 85.32                                                          |
| `meta`                                                         | [components.MetaData](../../models/components/metadata.md)     | :heavy_check_mark:                                             | N/A                                                            |                                                                |