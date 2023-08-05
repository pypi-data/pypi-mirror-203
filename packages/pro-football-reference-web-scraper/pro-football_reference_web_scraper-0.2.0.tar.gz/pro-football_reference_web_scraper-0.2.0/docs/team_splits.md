# Team Splits

In order to retrieve a team's game log in a given season, you will first need to know the name of the team you are interested in. The spelling of the team's name must exactly match its spelling on [Pro Football Reference](https://www.pro-football-reference.com/). You will also need to specify the season you are interested in, as well as if you want the stats as averages or sums.

## Home-Road Splits

You can retrieve a team's stats in home vs. road games either as averages or sums.

### Averages

The following code will output the Philadelphia Eagles stats in home vs. road games in the 2018 season as averages.

```eval_rst

.. note:: The 'team' parameter is case sensitive. 'Philadelphia eagles' will not work, but 'Philadelphia Ealges' will.

```

```python

from pro_football_reference_web_scraper import team_splits as t

print(t.home_road(team = 'Philadelphia Eagles', season = 2022, avg = True))

```

Output:

```

| game_location   |   games |   wins |   ties |   losses |   points_for |   points_allowed |   tot_yds |   pass_yds |   rush_yds |   opp_tot_yds |   opp_pass_yds |   opp_rush_yds |
|:----------------|--------:|-------:|-------:|---------:|-------------:|-----------------:|----------:|-----------:|-----------:|--------------:|---------------:|---------------:|
| home            |       9 |      7 |      0 |        2 |      26.8889 |          18.7778 |   380.889 |    231.333 |    149.556 |       286.444 |        173.778 |        112.667 |
| away            |       8 |      7 |      0 |        1 |      29.375  |          21.875  |   398.25  |    252.875 |    145.375 |       318.375 |        186.625 |        131.75  |

```