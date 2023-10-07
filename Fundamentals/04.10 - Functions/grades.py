def grades_evaluation(grade: str) -> str:
    grade = float(grade)
    result = ""
    if 2.00 <= grade < 3.00:
        result = "Fail"
    elif 3.00 <= grade < 3.50:
        result = "Poor"
    elif 3.50 <= grade < 4.50:
        result = "Good"
    elif 4.50 <= grade < 5.50:
        result = "Very Good"
    elif 5.50 <= grade <= 6.00:
        result = "Excellent"
    print(result)

    return result


receives_a_grade = input()
grades_evaluation(receives_a_grade)
