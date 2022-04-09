def computegrade(score):
    mark = ''
    if score > 1 or score < 0:
        mark = 'Bad Score'
    elif score >= 0.9: 
        mark = 'A'
    elif score >= 0.8: 
        mark = 'B'
    elif score >= 0.7:
        mark = 'C'
    elif score >= 0.6:
        mark = 'D'
    elif score < 0.6:
        mark = 'F'

    return mark




try:
    score = float(input("Enter score: "))
    grade = computegrade(score)
    print(grade)

except:
    print("Bad score")
