# Problem Link: https://leetcode.com/problems/calculate-special-bonus/?envType=study-plan-v2&envId=30-days-of-pandas&lang=pythondata

import pandas as pd

def calculate_special_bonus(employees: pd.DataFrame) -> pd.DataFrame:

    # Filter for the given condition
    myFilter = (employees['employee_id'] % 2 == 1) & (~(employees['name'].str.startswith('M')))

    # Initially creating a new column containing all 0s
    employees['bonus'] = 0

    # Putting salary as bonus where the filtering condition is met
    employees.loc[myFilter, 'bonus'] = employees['salary']
    
    # Selecting specific columns
    employees = employees[['employee_id', 'bonus']]

    # Sorting dataframe based on employee_id
    employees = employees.sort_values(by='employee_id', ascending=True)

    return employees