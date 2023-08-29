# Problem Link: https://leetcode.com/problems/find-total-time-spent-by-each-employee

import pandas as pd

def total_time(employees: pd.DataFrame) -> pd.DataFrame:

    # First calculating the total in_time and total out_time
    #   for each employee everyday
    df = employees.groupby(['emp_id', 'event_day']).sum().reset_index()

    # Calculating total time
    df['total_time'] = df['out_time'] - df['in_time']

    # Dropping unnecessary columns
    df.drop(columns = ['in_time', 'out_time'], inplace = True, axis = 1)

    # Renaming event_day column to day
    df.rename(columns = {
        "event_day" : "day"
    }, inplace = True)

    # Reording columns and dropping the index column
    #   the answer will be accepted even if this step is skipped.
    df = df[['day', 'emp_id', 'total_time']].reset_index(drop = True)

    return df