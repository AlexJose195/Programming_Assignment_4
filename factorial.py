# Write a Python Program to Find the Factorial of a Number.

a = int(input("Enter the number for finding Factorial : "))
b=1
for i in range(1,a+1):
    b=b*i

print("The Factorial of ",a," is " ,b)
