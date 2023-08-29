# Problem Link: https://leetcode.com/problems/count-salary-categories

import pandas as pd

def count_salary_categories(accounts: pd.DataFrame) -> pd.DataFrame:

    # Creating category column based on income column values
    accounts['category'] = accounts.income.map(lambda x: 'Low Salary'
        if x < 20000 else ('High Salary' if x > 50000
                                else 'Average Salary'))

    # Categories column
    categories = ['Low Salary', 'Average Salary', 'High Salary']

    # Categorical count of income
    accounts_count = []
    accounts_count.append(len(accounts[accounts['category'] == 'Low Salary']))
    accounts_count.append(len(accounts[accounts['category'] == 'Average Salary']))
    accounts_count.append(len(accounts[accounts['category'] == 'High Salary']))

    # Creating the result dataframe
    df = pd.DataFrame(
        {'category': categories,
        'accounts_count': accounts_count}
    )


    return df