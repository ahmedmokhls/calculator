import methods

#First project (Calculator)
while True:
    
    num_1=float(input('please enter first number: '))
    operation=input("Enter an operation: ")
    num_2=float(input('please enter second number: '))

    if operation == '*':
        print('result =', methods.mul(num_1,num_2))
    elif operation == '+':
        print('result =', methods.add(num_1,num_2))
    elif operation == '-':
        print('result =', methods.sub(num_1,num_2))
    elif operation == '/':
        print('result =', methods.div(num_1,num_2))
    else:
        print('result = none')
        
        
    another_calculation = input("Do you want to perform another calculation? (yes/no): ")
    if another_calculation.lower() != 'yes':
        print('Goodbye!')
        break       

    
    