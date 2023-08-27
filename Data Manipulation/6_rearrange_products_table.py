# Problem Link: https://leetcode.com/problems/rearrange-products-table/?envType=study-plan-v2&envId=30-days-of-pandas&lang=pythondata


# reference: https://pandas.pydata.org/docs/reference/api/pandas.melt.html

import pandas as pd

def rearrange_products_table(products: pd.DataFrame) -> pd.DataFrame:

    # Using pd.melt function to unpivot the table.
    df = pd.melt(products, 
                id_vars = ['product_id'], 
                value_vars = ['store1', 'store2', 'store3'],
                var_name = 'store',
                value_name = 'price')

    df.dropna(inplace=True)

    return df

    