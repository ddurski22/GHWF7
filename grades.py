
def compute_hw_average(grades,drop):
    if len(grades) == 0:
        return 0
    lowest_grade = 100
    count = 0
    while(count<drop):
        lowest_grade = 100
        for grade in grades:
            if grade <= low_grade:
                lowest_grade = grade
        grades.remove(lowest_grade)
        count+=1
    return sum(grades)/len(grades)
