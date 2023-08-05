# MLS API Python Package

The package provides convenient access to the [MLS API](https://moatsystems.com/mls-api/) functionality from applications written in the Python language.

## Requirements

Python 2.7 and later.

## Setup

You can install this package by using the pip tool and installing:

```python
pip install mls-api
## OR
easy_install mls-api
```

Install from source with:

```python
python setup.py install --user

## or `sudo python setup.py install` to install the package for all users
```

Usage Example
-------------

```python
import os, json
import mls_api

# Authentication
username = "your_username"
password = "your_password"
response_text = login(username, password)
print("Login response:", response_text)

# Get all historical data
response_text = mls_api.get_all_hist()
print("All historical data response:", response_text)

# Get all real-time data (RTD)
response_text = mls_api.get_all_rtd()
print("All real-time data response:", response_text)

# Get a list of players with a custom limit and offset
limit = 20
offset = 10
response_text = mls_api.get_all_players(limit, offset)
print("Players response:", response_text)

# Get all top scorers data
all_topscorers = mls_api.get_all_topscorers()
print("All Top Scorers:")
print(all_topscorers)

# Get all offence data
all_offences = mls_api.get_all_offences()
print("All Offences:")
print(all_offences)

# Get all assists data
all_assists = mls_api.get_all_assists()
print("All Assists:")
print(all_assists)

# Get all teams data
all_teams = mls_api.get_all_teams()
print("All teams:\n", all_teams)

# Get all fixtures data
all_fixtures = mls_api.get_all_fixtures()
print("All fixtures:\n", all_fixtures)

# Get all standings data
all_standings = mls_api.get_all_standings()
print(all_standings)

# Get all news data
all_news = mls_api.get_all_news()
print(all_news)
```

## Setting up an MLS API Account

Sign up for a self-service [user account](https://moatsystems.com/mls-api/).


## Using the MLS API

You can read the [API documentation](https://docs.mlssoccerapi.com/) to understand what's possible with the MLS API. If you need further assistance, don't hesitate to [contact us](https://moatsystems.com/contact/).


## License

This project is licensed under the [MIT License](./LICENSE).


## Copyright

(c) 2021 - 2023 [Moat Systems Limited](https://moatsystems.com/). All Rights Reserved.
