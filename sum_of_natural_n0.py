# Write a Python Program to Find the Sum of Natural Numbers.

print("\nFinding the sum of first n Natural Number")
a = int(input("\nEnter the no. of term  : "))
b=0
for i in range(1,a+1):
    b=b+i

print("The Sum of first  ",a," Natural number is " ,b)