# Problem Link: https://leetcode.com/problems/article-views-i/?envType=study-plan-v2&envId=30-days-of-pandas&lang=pythondata


import pandas as pd

def article_views(views: pd.DataFrame) -> pd.DataFrame:
    df =  views[views['author_id'] == views['viewer_id']][['author_id']]

    # Dropping duplicate ids
    df = df.drop_duplicates(subset=['author_id'])

    # sorting dataframe by author_id in ascending order
    df = df.sort_values(by='author_id')

    return df.rename(columns= {'author_id': 'id'})