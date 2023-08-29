# Problem Link: https://leetcode.com/problems/game-play-analysis-i

import pandas as pd


# Solution 1
def game_analysis1(activity: pd.DataFrame) -> pd.DataFrame:

    # Choosing required columns
    df = activity[['player_id', 'event_date']]

    # Group by player_id to find the minimum of event_date
    df = df.groupby('player_id').min().reset_index()
    
    # renaming column of event_date to first_login
    df.rename(columns = {
      "event_date": "first_login"
          }, inplace = True)

    return df

# Solution 2

def game_analysis2(activity: pd.DataFrame) -> pd.DataFrame:

    # Group by player_id
    df = activity.groupby('player_id')

    # Using agg function to find the minimum
    df = df.agg(
        first_login = ('event_date', 'min')
    )

    # Reseting index
    df.reset_index(inplace = True)

    return df
    