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