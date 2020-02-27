#customers details
firstName=input('Enter customers firstName: ')
lastName=input('Enter customers lastName: ')
mobileNo=int(input('Enter customers phone number: '))
idNumber=int(input('Enter customers ID number: '))
account_number=int(input('Enter customers Account number: '))

#all details of customers into dictionary
customer = dict()
customer['firstName'] = firstName
customer['lastName'] = lastName
customer['mobileNo'] = mobileNo
customer['idNumber'] = idNumber
customer['account_number']= account_number

print(customer)

#accounts details
account = dict()
account['account_number']=account_number
account['account_Type']= 'saving'
account['currency']= 'KES'
account['account_balance']= int(input('Enter account_balance'))

print(account)

#currency details
currency=dict()
currency['currensycode']= 'KES'
currency['currencyName']= 'Kenyashillings'

print(currency)


print(customer)




# def mydictionary():
#     Accountpropertice=dict()
#     Accountproperty['Accountnumber']='xxxxxxxxxxxxxx'
#     Accountproperty['current saving']='xxxxxxxxxxxxx'
#     Accountproperty['currency']='KES,USD'
#     currency[currency name]='Kenyan shillings'
    