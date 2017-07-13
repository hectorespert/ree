# reescraper (Red Eléctrica de España data scraper)

Package install:

```
pip install reescraper
```

Example Code:

```python
from reescraper import CanaryIslands

generation = CanaryIslands().get()
print(generation)
```
Output:

```
Response 2017-07-13T10:20:00+00:00 Demand 0.0 Diesel: 282.2 Gas: 159.4 Wind: 48.2 Combined: 338.3 Vapor: 329.5 Solar: 89.0 Hydraulic: -3.4
```
