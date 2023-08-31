# Problem Link: https://leetcode.com/problems/classes-more-than-5-students/

import pandas as pd

def find_classes(courses: pd.DataFrame) -> pd.DataFrame:

    df = courses.groupby(['class']).agg(
        student_count = ('student', 'count')
    ).reset_index()

    df = df[df['student_count'] >= 5][['class']]

    return df