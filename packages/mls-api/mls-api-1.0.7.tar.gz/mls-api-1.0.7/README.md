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
response_text = get_all_hist()
print("All historical data response:", response_text)

# Get historical data by ID
hist_id = "the_uuid" # UUID
response_text = get_hist_by_id(hist_id)
print("Historical data by ID response:", response_text)

# Get all real-time data (RTD)
response_text = get_all_rtd()
print("All real-time data response:", response_text)

# Get real-time data (RTD) by ID
rtd_id = "the_uuid" # UUID
response_text = get_rtd_by_id(rtd_id)
print("Real-time data by ID response:", response_text)

# Get a list of players with a custom limit and offset
limit = 20
offset = 10
response_text = get_all_players(limit, offset)
print("Players response:", response_text)

# Get a specific player by ID
player_id = "the_uuid" # UUID
response_text = get_player_by_id(player_id)
print("Player by ID response:", response_text)

# Get all top scorers data
all_topscorers = topscorer.get_all_topscorers()
print("All Top Scorers:")
print(all_topscorers)

# Get top scorers data by ID
topscorer_id = "the_uuid" # UUID
specific_topscorer = topscorer.get_topscorer_by_id(topscorer_id)
print(f"Top Scorer with ID {topscorer_id}:")
print(specific_topscorer)

# Get all offence data
all_offences = offence.get_all_offences()
print("All Offences:")
print(all_offences)

# Get offence data by ID
offence_id = "the_uuid" # UUID
specific_offence = offence.get_offence_by_id(offence_id)
print(f"Offence with ID {offence_id}:")
print(specific_offence)

# Get all assists data
all_assists = assists.get_all_assists()
print("All Assists:")
print(all_assists)

# Get assists data by ID
assist_id = "the_uuid" # UUID
specific_assist = assists.get_assist_by_id(assist_id)
print(f"Assist with ID {assist_id}:")
print(specific_assist)

# Get all teams data
all_teams = teams.get_all_teams()
print("All teams:\n", all_teams)

# Get teams data by ID
team_id = "the_uuid" # UUID
team = teams.get_team_by_id(team_id)
print(f"Team with ID {team_id}:\n", team)

# Get all fixtures data
all_fixtures = fixtures.get_all_fixtures()
print("All fixtures:\n", all_fixtures)

# Get fixtures data by ID
fixture_id = "the_uuid" # UUID
fixture = fixtures.get_fixture_by_id(fixture_id)
print(f"Fixture with ID {fixture_id}:\n", fixture)

# Get all standings data
all_standings = standings.get_all_standings()
print(all_standings)

# Get a specific standing by ID
standing_id = "the_uuid" # UUID
specific_standing = standings.get_standing_by_id(standing_id)
print(specific_standing)

# Get all news data
all_news = news.get_all_news()
print(all_news)

# Get a specific news item by ID
news_id = "the_uuid" # UUID
specific_news = news.get_news_by_id(news_id)
print(specific_news)
```

## Setting up an MLS API Account

Sign up for a self-service [user account](https://moatsystems.com/mls-api/).


## Using the MLS API

You can read the [API documentation](https://docs.mlssoccerapi.com/) to understand what's possible with the MLS API. If you need further assistance, don't hesitate to [contact us](https://moatsystems.com/contact/).


## License

This project is licensed under the [MIT License](./LICENSE).


## Copyright

(c) 2021 - 2023 [Moat Systems Limited](https://moatsystems.com/). All Rights Reserved.
