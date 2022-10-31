# Write a Python Program to Check Armstrong Number.

print("\nArmstrong Number\n")
Entered_no = int(input("Enter the number for checking wheather it is a armstrong no. or not : "))

converted_to_string = str(Entered_no)
len_of_string = len(converted_to_string)
Armstorng_number = 0

for i in range(len_of_string):
    Armstorng_number = Armstorng_number + (int(converted_to_string[i])**len_of_string)


if Armstorng_number == Entered_no:
    print(Entered_no," is a Armstrong Number.")
else:
    print(Entered_no, " is not a Armstrong Number.")