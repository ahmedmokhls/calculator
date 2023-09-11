#First project (Calculator)

def add(num_1,num_2):
    result = num_1+num_2
    return result

def sub(num_1,num_2):
    result=num_1-num_2
    return result

def mul(num_1,num_2):
    result=num_1*num_2
    return result

def div(num_1,num_2):
    if num_2 == 0:
        print('cannot divded by 0')
    else:
        result=num_1/num_2
        return result

while True:
    
    num_1=float(input('please enter first number: '))
    operation=input("Enter an operation: ")
    num_2=float(input('please enter second number: '))

    if operation == '*':
        print('result =', mul(num_1,num_2))
    elif operation == '+':
        print('result =', add(num_1,num_2))
    elif operation == '-':
        print('result =', sub(num_1,num_2))
    elif operation == '/':
        print('result =', div(num_1,num_2))
    else:
        print('result = none')
        
        
    another_calculation = input("Do you want to perform another calculation? (yes/no): ")
    if another_calculation.lower() != 'yes':
        print('Goodbye!')
        break       

    
    