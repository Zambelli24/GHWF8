
def compute_hw_average(grades, dropped_grades):
    if len(grades) == 0:
        return 0
    if dropped_grades > 0:
        grades = sorted(grades)
        for i in range(dropped_grades):
            grades.pop(0)
    return sum(grades) / len(grades)
