# Problem Link: https://leetcode.com/problems/actors-and-directors-who-cooperated-at-least-three-times

import pandas as pd

def actors_and_directors(actor_director: pd.DataFrame) -> pd.DataFrame:

    # Finding specific actor director interaction count
    df = actor_director.groupby(['actor_id', 'director_id']).count().reset_index()

    # Filtering rows
    df = df[df.timestamp >= 3]

    # Returning selected rows
    return df[['actor_id', 'director_id']]