# Problem Link: https://leetcode.com/problems/sales-person

import pandas as pd

def sales_person(sales_person: pd.DataFrame, company: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:

    # Getting id of company name "RED"
    red_id = company[company['name']=='RED']['com_id']

    # Finding all sale orders related to "RED" company
    red_orders = orders.merge(red_id, how='right')

    # Joining (left) red orders, find the None value
    df = sales_person.merge(red_orders, on='sales_id', how='left')

    # Returning names for the null rows
    df = df[df['order_id'].isna()][['name']]
    
    return df