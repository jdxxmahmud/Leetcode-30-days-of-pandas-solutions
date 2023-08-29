# Problem Link: https://leetcode.com/problems/immediate-food-delivery-i/

import pandas as pd

def food_delivery(delivery: pd.DataFrame) -> pd.DataFrame:

    # Immediate Order count
    immediateCount = delivery[delivery['order_date'] == delivery['customer_pref_delivery_date']].shape[0]

    # Find the ratio of immediate vs total orders
    ratio = round((immediateCount * 100)/delivery.shape[0], 2)

    # Result
    result = pd.DataFrame([ratio], columns=['immediate_percentage'])

    return result