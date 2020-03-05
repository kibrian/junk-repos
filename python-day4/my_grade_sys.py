from myfunctions import getGrade,getMeanScore,getSum
nameOfStudent= input('Enter name of student \n')
regNO=input('Enter the REG Number \n')

mathScore= int(input('Enter Math Score \n'))
engScore = int(input('Enter English Score \n'))
swaScore = int(input('Enter Swa Score \n'))

print('Exam Report for ',nameOfStudent,'\n')
print(("maths"),mathScore,'\n')
print(("eng"),engScore,'\n')
print(("swa"),swaScore,'\n')
sum = (mathScore+engScore+swaScore)
meanScore =(sum)
grade =(meanScore)

print(meanScore)
print('Mean Grade :',grade)
print('Mean Grade :',getGrade(getMeanScore(getSum(mathScore,engScore,swaScore))))



