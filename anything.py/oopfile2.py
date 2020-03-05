class customer:
    def __init__(self,firstname,lastname,age):
        self.firstname=firstname
        self.lastname=lastname
        self.age=age
    def myoutput(self):
        print(self.firstname)
brian=customer("Brian","kip",20)
print(brian.firstname)
sylus=customer("sylus","yegon","32")
print(sylus.age)
sylus.age=25
print(sylus.age)
sylus.myoutput()