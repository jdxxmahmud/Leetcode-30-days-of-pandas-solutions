# Problem Link: https://leetcode.com/problems/recyclable-and-low-fat-products/?envType=study-plan-v2&envId=30-days-of-pandas&lang=pythondata

import pandas as pd

def find_products(products: pd.DataFrame) -> pd.DataFrame:
    df = products[(products["low_fats"] == 'Y') & (products["recyclable"] == 'Y')]
    return df[['product_id']]