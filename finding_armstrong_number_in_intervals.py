# Write a Python Program to Find Armstrong Number in an Interval.

print("Finding Armstrong Number in Given Interval")
Starting_point=int(input("Enter the starting point :"))
Ending_point=int(input("Enter the Ending point :"))

for num in range(Starting_point,Ending_point):
    converted_to_string = str(num)
    len_of_string = len(converted_to_string)
    Armstorng_number = 0

    for i in range(len_of_string):
        Armstorng_number = Armstorng_number + (int(converted_to_string[i]) ** len_of_string)

    if Armstorng_number == num:
        print(num,end= ", ")
    else:
        continue