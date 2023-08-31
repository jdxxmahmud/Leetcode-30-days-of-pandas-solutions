# Problem Link: https://leetcode.com/problems/managers-with-at-least-5-direct-reports

import pandas as pd

def find_managers(employee: pd.DataFrame) -> pd.DataFrame:

    # Counting with group by managerId.
    df = employee.groupby("managerId", as_index = False).agg("count")

    # Getting employees that have managers and report count at least 5
    df = employee[employee["id"].isin(df[df["id"] >= 5]["managerId"].values)][["name"]]
    
    return df