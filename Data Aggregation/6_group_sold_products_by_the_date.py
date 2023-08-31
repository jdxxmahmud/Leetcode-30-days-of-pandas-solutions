# Problem Link: https://leetcode.com/problems/group-sold-products-by-the-date

import pandas as pd

def categorize_products(activities: pd.DataFrame) -> pd.DataFrame:

    # Removing duplicate values
    df = activities.drop_duplicates()
    
    # Sorting product names lexicographically. 
    # Then group by sell date to concatnate the product names
    df = df.sort_values(by='product').groupby('sell_date')['product'].apply(
        ','.join).reset_index()

    # Renaming column name
    df.rename(columns = {
        'product': 'products'
    }, inplace = True)

    # Finding numbers of products sold for each date
    df['num_sold'] = df.products.apply(lambda x: len(x.split(',')))


    # Reordering columns
    return df[['sell_date', 'num_sold', 'products']]