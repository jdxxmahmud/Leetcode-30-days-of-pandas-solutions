# Problem Link: https://leetcode.com/problems/fix-names-in-a-table/?envType=study-plan-v2&envId=30-days-of-pandas&lang=pythondata

import pandas as pd

def fix_names(users: pd.DataFrame) -> pd.DataFrame:

    # Applying title case function.
    users['name'] = users['name'].str.title()

    return users.sort_values(by='user_id', ascending=True)