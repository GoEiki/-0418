def get_math_highscore_student(student_list):
    if not student_list:
        return None
    math_high_score=0
    math_high_student=None

    for student in student_list:
        if student.math > math_high_score:
          math_high_score = student.math
          math_high_student = student.name

    return math_high_student    
    
    
