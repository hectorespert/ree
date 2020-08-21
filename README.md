# ree (Red Eléctrica de España data)
Library to query information of Spain  electric energy demand from [Red Eléctrica de España](https://demanda.ree.es).

![Tests](https://github.com/hectorespert/ree/workflows/Tests/badge.svg) [![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=hectorespert_ree&metric=alert_status)](https://sonarcloud.io/dashboard?id=hectorespert_ree)

## Package install:

```bash
pip install ree
```

### Example Code:

```python
from ree import CanaryIslands

generation = CanaryIslands().get()
print(generation)
```
Output:

```
Response 2017-07-13T10:20:00+00:00 Demand 0.0 Diesel: 282.2 Gas: 159.4 Wind: 48.2 Combined: 338.3 Vapor: 329.5 Solar: 89.0 Hydraulic: -3.4
```
