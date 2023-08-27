# Problem Link: https://leetcode.com/problems/the-number-of-rich-customers/solutions/3969237/easy-solution-with-dataframe-groupby/


import pandas as pd

def count_rich_customers(store: pd.DataFrame) -> pd.DataFrame:

    # Finding the maximum bill for each customer
    df = store.groupby(['customer_id'], group_keys = False).max()

    # Filtering customers with bill strictly more than 500
    df = df[df['amount'] > 500]

    # converting the result to a dataframe
    ans = pd.DataFrame.from_dict({"rich_count": len(df)}, orient = 'index').T

    return ans