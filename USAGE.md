<!-- Start SDK Example Usage [usage] -->
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