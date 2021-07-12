# use the bisection functions to maintain a list in sorted order
import bisect

values = [5, 7, 13, 20, 25, 31, 36, 43, 47, 49, 50, 75]

# TODO: exercise the left and right bisection routines
print(bisect.bisect(values, 25))
print(bisect.bisect_right(values, 25))
print(bisect.bisect_left(values, 25))

# TODO: use insort to insert new items
# bisect.insort(values, 34)
bisect.insort_right(values, 25)
print(values)

# bisect can be used as an array lookup using breakpoints
break_points = [60, 70, 80, 90]
grade_letters = 'FDCBA'
scores = [81, 68, 53, 91, 90, 82, 76, 71, 84]

def calc_grade(score):
    # TODO: use the bisect function to identify cutoff points for the letter grades
    i = bisect.bisect(break_points, score)
    return grade_letters[i]

results = [calc_grade(score) for score in scores]
print(results)
print(list(zip(scores, results)))
