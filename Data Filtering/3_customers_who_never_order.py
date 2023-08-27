# Problem Link: https://leetcode.com/problems/customers-who-never-order/description/?envType=study-plan-v2&envId=30-days-of-pandas&lang=pythondata

import pandas as pd

def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    # print(orders['customerId'])
    df = customers[~customers['id'].isin(list(orders['customerId']))]
    df = df.rename(columns={'name': 'Customers'})
    return df[['Customers']]