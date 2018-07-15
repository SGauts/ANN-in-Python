#Importing number checker and testing it
import number_checker

n = int(input("Enter a number"))
prime = number_checker.is_prime(n)
even =  number_checker.is_even(n)

if(prime):
    print("Number is prime")
elif(even):
    print("Even number")
else:
    print("Neither even nor prime")
