noofstudent=int(input('Enter the noofstudent'))
noofsubjects=int(input('Enter the noofsubjects'))
for n in range(1,noofsubjects+1):
    subjects = dict(000)
    subjectName=input('Enter subjectName: ')
    score=int(input('Enter score: '))
    subjects[subjectName]=score

print(subjects)



