# Problem Link: https://leetcode.com/problems/students-and-examinations

import pandas as pd

def students_and_examinations(students: pd.DataFrame, subjects: pd.DataFrame, examinations: pd.DataFrame) -> pd.DataFrame:

    # Finding exam count and renaming the new column
    exam_count = examinations.groupby(['student_id', 'subject_name']).size().reset_index(name="attended_exams")

    # Finding the cross join to find all the possible combinations of student and subject
    st_sub = pd.merge(students, subjects, how='cross')

    # Joining tables
    df = st_sub.merge(exam_count, how='left', on=['student_id', 'subject_name']).fillna(0)

    # Sorting rows on student_id and lexicographically subject_name
    df.sort_values(by=['student_id', 'subject_name'], inplace = True)

    return df[[
        'student_id',
        'student_name',
        'subject_name',
        'attended_exams'
    ]]