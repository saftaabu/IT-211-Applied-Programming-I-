#4
print("Program number: 4")

inches = input("Enter inches: ")

inches_to_feet = int(inches) / 12

inches_2 = inches_to_feet % 1

inch = inches_2 * 12

print(inches, "inches is", '%d' % inches_to_feet, "feet", '%d' % inch , "inches")
