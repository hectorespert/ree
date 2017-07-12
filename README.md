# reescraper (Red Eléctrica de España data scraper)

Require phantomjs binary available in your system path.

Ubuntu phantomjs install:

```
sudo apt install phantomjs
```

Package install:

```
pip install reescraper
```

Example Code:

```python
from reescraper import GenerationCanaryIslands

generation = GenerationCanaryIslands().get()
print(generation)
```
Output:

```
Generation 2017-07-12T19:20:00+00:00 Diesel: 310.0 Gas: 115.2 Wind: 57.6 Combined: 315.0 Vapor: 394.0 Solar: 1.9 Hydraulic: -0.2
```
