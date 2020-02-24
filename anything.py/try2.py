# this is a comment
familyname=input("Enter familyname: ")
fathersname=input("Enter fathersname: ")
mothersname=input("Enter mothersname: ")
sonsname=input("Enter sonsname: ")
age=int(input("Enter age: "))

def agefunction(age):
    if age > 60:
        return 'should retire'
    elif age >=50 and age <60:
        return 'should own a business'
    elif age > 40 and  age < 50:
        return 'should have a family'
    elif age >=30 and age < 40:
        return 'should be married' 
    elif age >=20 and age < 30:
        return  'should studing and working' 
    else:
        return 'should do house chores and be schooling'

agefunction=agefunction("fathersname,mothersname,sonsname")

print("agefunction {}".format("father"))
print("agefunction {}".format("mother"))
print("agefunction {}".format("son"))