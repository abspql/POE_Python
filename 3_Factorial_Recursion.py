def factorial(n):

    if(n==0 or n==1):
        return 1
    else:
        return (n * factorial(n-1))


num1 = int(input("Enetr The Number : "))
print("Number is ", num1)
print("Factorial of Number is : ",factorial(num1))