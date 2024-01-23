# SimilarItemPayload

Payload for similar item search.


## Fields

| Field                                       | Type                                        | Required                                    | Description                                 | Example                                     |
| ------------------------------------------- | ------------------------------------------- | ------------------------------------------- | ------------------------------------------- | ------------------------------------------- |
| `external_id`                               | *str*                                       | :heavy_check_mark:                          | The external id of the item to search for.  | 26d17f72-44e8-467a-8931-8867e11075a4        |
| `min_score`                                 | *Optional[float]*                           | :heavy_minus_sign:                          | The minimum score of the results to return. | 0.5                                         |