noofstudents =int(input('Enter the number of students: '))
for n in range(1,noofstudents+1):
    noofsubjects=int(input('Enter the number of subjects: '))
    for n in range(1,noofsubjects+1):
        subjectName=input('Enter subjectName: ')
        studentName=input('Enter studentName: ')
        subjectScore=int(input('Enter subjectScore: '))

def mydictionary():
    subjects=dict()
    subjects[subjectName]=subjectScore

subjects=dict()


def gradesystem(Score):
    if Score >= 80 and Score <100:
        return 'A'
    elif Score >=60 and Score <80:
        return 'B'
    elif Score >=40 and Score <60:
        return 'C'
    elif Score >=0 and Score <40:
        return 'D'
    else:
        return 'zero'
    

def mystudents():
    students=dict()
    students['studentName']=input('Enter studentName: ')
    students['RegistrationNo']=int(input('Enter RegistrationNo: '))
    students['studentclass']=input('Enter the class of student: ')
    students['studentsubject']=input('Enter subjectName: ')

students=dict()
