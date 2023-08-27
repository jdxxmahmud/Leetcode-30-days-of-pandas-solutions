# Problem Link: https://leetcode.com/problems/delete-duplicate-emails/?envType=study-plan-v2&envId=30-days-of-pandas&lang=pythondata

# reference: https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.drop_duplicates.html

import pandas as pd

# Modify Person in place
def delete_duplicate_emails(person: pd.DataFrame) -> None:
    
    # Sorting the dataframe based on id, by default ascending order
    person.sort_values(by='id', inplace=True)

    # Using DataFrame.drop_duplicates() function
    #   to drop duplicate emails.

    # keep='first' keeps the first value.
    # since we sorted the dataframe, the smallest id 
    # will be preserved.
    person.drop_duplicates(subset='email', keep='first', inplace=True)


