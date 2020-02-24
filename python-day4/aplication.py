studentName=input('Enter name:  ')
regesNo=input('Enter regesNo: ')
math=int(input('Enter mathscore: '))
eng=int(input('Enter Engscore: '))
kis=int(input('Enter Kisscore: '))
def gradesystem(marks):
    if marks >= 80 and marks <= 100:
        return 'A'
    elif marks >= 60 and marks < 80:
        return 'B'
    elif marks >= 40 and marks < 60:
        return 'C'
    elif marks >= 0 and marks < 40:
        return 'D'
    else:
        return 'unknown Grade'
print("Math Grade: {}".format(gradesystem(math)))
print("Eng Grade: {}".format(gradesystem(eng)))
print("Kisw Grade: {}".format(gradesystem(kis)))
def sum(num1,num2,num3):
    sum = num1 + num2 + num3
    return sum
print("Total Mark: {}".format(sum(math,eng,kis)))
def averageMark(num1,num2,num3):
    marks = (num1+num2+num3)/3
    return marks
average = averageMark(math,eng,kis)
print("Average Mark:{}".format(average))
print("Mean Grade:{}".format(gradesystem(average)))