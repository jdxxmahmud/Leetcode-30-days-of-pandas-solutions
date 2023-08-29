# Problem Link: https://leetcode.com/problems/number-of-unique-subjects-taught-by-each-teacher

import pandas as pd

def count_unique_subjects(teacher: pd.DataFrame) -> pd.DataFrame:

    #Grouping by teacher_id
    df = teacher.groupby('teacher_id')

    # finding unique subject_id count using "nunique" from the grouped output
    df = df['subject_id'].nunique().reset_index()

    # renaming columns
    df.rename(
        columns = {
            'subject_id': 'cnt'
        }, inplace = True
    )


    return df