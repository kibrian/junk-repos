

class Students:
    def __init__(self,name,regNo,stdclass):
        self.name=name
        self.regNo=regNo
        self.stdclass=stdclass
class brian(Students):
    def stdclass(self):
        print(brian) 

class Geofry(Students):
    def regNo(self):
        print(Geofry)       

student1=brian("kip","xxx09ax99","7")

student2=Geofry("bio","bbsaxx904","6")

students=[student1,student2]
for x in students:
    print(x)
print(students)