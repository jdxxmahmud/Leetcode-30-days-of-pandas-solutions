# Problem Link: https://leetcode.com/problems/rank-scores/?envType=study-plan-v2&envId=30-days-of-pandas&lang=pythondata

import pandas as pd

def order_scores(scores: pd.DataFrame) -> pd.DataFrame:
    
    # assigning ranks using pandas.series.rank function with method = dense and descending order
    scores['rank'] = scores.score.rank(method='dense', ascending=False).astype('int')

    # sorting the dataframe
    scores = scores.sort_values(by=['rank'], ascending=True)
    
    return scores[['score', 'rank']]