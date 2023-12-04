num1 = int(input("Enter The Number : "))

factorial = 1;

if(num1<0):
    print("Sorry, Factorial does not exist for negative number")
elif(num1 == 0):
    print("The factorial of 1 is 0")
else:
    for i in range(1, num1+1):
        factorial = factorial * i

    print("The factorial of", num1,"is :", factorial)

