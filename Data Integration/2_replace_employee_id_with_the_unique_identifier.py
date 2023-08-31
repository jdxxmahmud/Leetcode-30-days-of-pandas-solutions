# Problem Link: https://leetcode.com/problems/replace-employee-id-with-the-unique-identifier

import pandas as pd

def replace_employee_id(employees: pd.DataFrame, employee_uni: pd.DataFrame) -> pd.DataFrame:
    
    # Joining tables, left join on "id"
    df = employees.merge(employee_uni, how = 'left', on = 'id')

    # Returing specific columns
    return df[['unique_id', 'name']]