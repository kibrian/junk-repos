students =dict()

student1=dict()
student1['regno']='1234'
student1['name']='Nick'

student2=dict()
student2['regno']='5678'
student2['name']='brian'

students['1']=student1
students['2']=student2

print(students)



print(students.get("1"))
print(students.get('2'))
