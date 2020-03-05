class Account:
    def __init__(self,customerName,accountNo,balance,currency):
        self.customerName=customerName
        self.accountNo=accountNo
        self.balance=balance
        self.currency=currency

    def showAcc(self):
        print('customerName: ',self.customerName,'accountNo: ',self.accountNo,'balance: ',self.balance,'currency type:',self.currency)

customerName=input('Enter customerName: ')
accountNo=int(input('Enter accountNo: '))
balance=int(input('Enter balance: '))
currency=input('Enter currency type')


customer1=Account(customerName,accountNo,balance,currency)
customer1.showAcc()


print(customer1)

