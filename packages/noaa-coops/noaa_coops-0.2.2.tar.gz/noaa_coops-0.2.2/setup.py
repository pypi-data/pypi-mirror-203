# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['noaa_coops']

package_data = \
{'': ['*']}

install_requires = \
['numpy>=1.24.1,<2.0.0',
 'pandas>=1.5.3,<2.0.0',
 'requests>=2.28.2,<3.0.0',
 'zeep>=4.2.1,<5.0.0']

setup_kwargs = {
    'name': 'noaa-coops',
    'version': '0.2.2',
    'description': 'Python wrapper for NOAA Tides & Currents Data and Metadata.',
    'long_description': '# noaa_coops\n\n[![Build Status](https://travis-ci.org/GClunies/noaa_coops.svg?branch=master)](https://travis-ci.org/GClunies/noaa_coops)\n[![PyPI](https://img.shields.io/pypi/v/noaa_coops.svg)](https://pypi.python.org/pypi/noaa-coops)\n[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/noaa_coops.svg)](https://pypi.python.org/pypi/noaa-coops)\n\nA Python wrapper for the NOAA CO-OPS Tides &amp; Currents [Data](https://tidesandcurrents.noaa.gov/api/)\nand [Metadata](https://tidesandcurrents.noaa.gov/mdapi/latest/) APIs.\n\n## Installation\nThis package is distributed through [pip](https://pypi.org/project/noaa-coops/) and can be installed to an environment via `pip install noaa-coops`.\n\n## Getting Started\n\n### Stations\nData is accessed via `Station` class objects. Each station is uniquely identified by an `id`. To initialize a `Station` object, run:\n\n```python\n>>> from noaa_coops import Station\n>>> seattle = Station(id="9447130")  # Create Station object for Seattle (ID = 9447130)\n```\n\nStations can be found with the Tides & Currents [mapping interface](https://tidesandcurrents.noaa.gov/) or the `get_stations_from_bbox` function, which searches a bounding box for stations and returns their IDs (if found).\n```python\n>>> from pprint import pprint\n>>> from noaa_coops import Station, get_stations_from_bbox\n>>> stations = get_stations_from_bbox(lat_coords=[40.389, 40.9397], lon_coords=[-74.4751, -73.7432])\n>>> pprint(stations)\n[\'8516945\', \'8518750\', \'8519483\', \'8531680\']\n>>> station_one = Station(id="8516945")\n>>> pprint(station_one.name)\n\'Kings Point\'\n```\n\n#### Metadata\nStation metadata is stored in the `.metadata` attribute of a `Station` object. Additionally, the keys of the metadata attribute dictionary are also assigned as attributes of the station object itself.\n\n```python\n>>> from pprint import pprint\n>>> from noaa_coops import Station\n>>> seattle = Station(id="9447130")\n>>> pprint(list(seattle.metadata.items())[:5])                   # Print first 3 items in metadata\n[(\'tidal\', True), (\'greatlakes\', False), (\'shefcode\', \'EBSW1\')]  # Metadata dictionary can be very long\n>>> pprint(seattle.lat_lon[\'lat\'])                               # Print latitude\n47.601944\n>>> pprint(seattle.lat_lon[\'lon\'])                               # Print longitude\n-122.339167\n```\n\n#### Data Inventory\nA description of a Station\'s data products and available dates can be accessed via the `.data_inventory` attribute of a `Station` object.\n\n```python\n>>> from noaa_coops import Station\n>>> from pprint import pprint\n>>> seattle = Station(id="9447130")\n>>> pprint(seattle.data_inventory)\n{\'Air Temperature\': {\'end_date\': \'2019-01-02 18:36\',\n                     \'start_date\': \'1991-11-09 01:00\'},\n \'Barometric Pressure\': {\'end_date\': \'2019-01-02 18:36\',\n                         \'start_date\': \'1991-11-09 00:00\'},\n \'Preliminary 6-Minute Water Level\': {\'end_date\': \'2023-02-05 19:54\',\n                                      \'start_date\': \'2001-01-01 00:00\'},\n \'Verified 6-Minute Water Level\': {\'end_date\': \'2022-12-31 23:54\',\n                                   \'start_date\': \'1995-06-01 00:00\'},\n \'Verified High/Low Water Level\': {\'end_date\': \'2022-12-31 23:54\',\n                                   \'start_date\': \'1977-10-18 02:18\'},\n \'Verified Hourly Height Water Level\': {\'end_date\': \'2022-12-31 23:00\',\n                                        \'start_date\': \'1899-01-01 00:00\'},\n \'Verified Monthly Mean Water Level\': {\'end_date\': \'2022-12-31 23:54\',\n                                       \'start_date\': \'1898-12-01 00:00\'},\n \'Water Temperature\': {\'end_date\': \'2019-01-02 18:36\',\n                       \'start_date\': \'1991-11-09 00:00\'},\n \'Wind\': {\'end_date\': \'2019-01-02 18:36\', \'start_date\': \'1991-11-09 00:00\'}}\n```\n\n#### Data\nStation data can be fetched using the `.get_data` method on a `Station` object. Data is returned as Pandas DataFrames for ease of use and analysis. Available data products can be found in [NOAA CO-OPS Data API](https://tidesandcurrents.noaa.gov/api/#products) docs.\n\n`noaa_coops` currently supports the following data products:\n- Currents\n- Observed water levels\n- Observed daily high and low water levels (use `product="high_low"`)\n- Predicted water levels\n- Predicted high and low water levels\n- Winds\n- Air pressure\n- Air temperature\n- Water temperature\n\nThe example below fetches water level data from the Seattle station for a 3 month period.\n\n```python\n>>> from noaa_coops import Station\n>>> seattle = Station(id="9447130")\n>>> df_water_levels = seattle.get_data(\n...     begin_date="20150101",\n...     end_date="20150331",\n...     product="water_level",\n...     datum="MLLW",\n...     units="metric",\n...     time_zone="gmt")\n>>> df_water_levels.head()\n                     water_level  sigma    flags QC\ndate_time\n2015-01-01 00:00:00        1.799  0.023  0,0,0,0  v\n2015-01-01 00:06:00        1.718  0.018  0,0,0,0  v\n2015-01-01 00:12:00        1.639  0.013  0,0,0,0  v\n2015-01-01 00:18:00        1.557  0.012  0,0,0,0  v\n2015-01-01 00:24:00        1.473  0.014  0,0,0,0  v\n\n```\n\n## Development\n\n### Requirements\nThis package and its dependencies are managed using [poetry](https://python-poetry.org/). To install the development environment for `noaa_coops`, first install poetry, then run (inside the repo):\n\n```bash\npoetry install\n```\n\n### TODO\nClick [here](https://github.com/GClunies/noaa_coops/issues) for a list of existing issues and to submit a new one.\n\n### Contribution\nContributions are welcome, feel free to submit a pull request.\n',
    'author': 'Greg Clunies',
    'author_email': 'greg.clunies@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/GClunies/noaa_coops',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
