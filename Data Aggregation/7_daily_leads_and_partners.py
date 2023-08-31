# Problem Link: https://leetcode.com/problems/daily-leads-and-partners/

import pandas as pd

def daily_leads_and_partners(daily_sales: pd.DataFrame) -> pd.DataFrame:
    
    # Dropping duplicate values
    df = daily_sales.drop_duplicates()

    # Group by columns to find the unique values
    df = df.groupby(['date_id', 'make_name']).agg(
        {
            "lead_id": "nunique",
            "partner_id": "nunique"
        }
    ).reset_index()

    # Renaming columns
    df.rename(columns = {
        "lead_id": "unique_leads",
        "partner_id": "unique_partners"
    }, inplace = True)


    return df
    
