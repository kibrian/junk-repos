studentname=input('Enter name: ')
regesno=input('Enter number: ')
math=int(input('Enter mathscore: '))
eng=int(input('Enter engscore: '))
kisw=int(input('Enter kiswscore: '))
def gradesystem(marks):
    if marks >80:
        return 'A'
    elif marks >60 and marks <80:
        return 'B' 
    elif marks >40 and marks <60:
        return 'C'
    elif marks >=0 and marks <40:
        return 'D'
    else:
        return 'none'

print("math Grade:  {}".format(gradesystem(math)))
print("eng Grade: {}".format(gradesystem(eng)))   
print("kisw Grade: {}".format(gradesystem(kisw)))

def sum(num1,num2,num3):
    sum=num1 + num2 + num3
    return sum

print("Total marks: {}".format(sum(math,eng,kisw)))

def average Mark(num1,num2,num3):
    marks = (num1+num2+num3)/3
    return marks

print("avarage Mark:{}".format(avarage Mark))
print("Mean Grade: {}".format(gradesystem(avarage Mark)))








