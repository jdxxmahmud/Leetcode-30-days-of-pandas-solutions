# Problem Link: https://leetcode.com/problems/customer-placing-the-largest-number-of-orders/

from pandas import pd


def largest_orders(orders: pd.DataFrame) -> pd.DataFrame:
    
    # Finding customer order count using group by
    df = orders.groupby('customer_number').count().reset_index()

    # Sorting values based on order count
    df.sort_values(by='order_number', ascending=False, inplace = True)
    
    # Returing only the first row of the customer_number column.
    return df[['customer_number']].head(1)



# one line solution 
def largest_orders2(orders: pd.DataFrame) -> pd.DataFrame:
    
    return orders.groupby('customer_number'
                          ).count().reset_index(
                          ).sort_values(
                            by='order_number', 
                            ascending=False)[['customer_number']].head(1)