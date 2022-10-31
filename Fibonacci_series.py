# Write a Python Program to Print the Fibonacci sequence.

print("Fibonacci Sequence")
n = int(input("Enter the no. of terms you want in Fibonacci Sequence : "))

for i in range(n):
    if i == 0:
        a = i
        print(a,end=", ")

    elif i == 1:
        b = i
        print(b,end=", ")

    else:
        c=a+b
        print(c,end=", ")
        a,b=b,c