#Number checker
def is_prime(num):

    count = 0

    for i in range(1,num+1):

        if(num%i==0):
            count = count + 1

    if(count==2):
        return True
    else:
        return False

def is_even(num):

    if(num%2==0):
        return  True
    else:
        return False
