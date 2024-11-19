operation_type = input("Please select a mathematical operation to calcuate; input must be in all caps: ")
if operation_type == "ADDITION":
    print("You are now doing {operation_type}.")
    first_addend = input("Please input the first addend: ")
    second_addend = input("Please input the second addend: ")
    print("Okay, here is the answer!")
    print(first_addend+second_addend)
elif operation_type == "SUBTRACTION":
    print("You are now doing {operation_type}.")
    minuend = input("Please input the minuend: ")
    subtrahend = input("Please input the subtrahend: ")
    print("Okay, here is the answer!")
    print(minuend-subtrahend)
elif operation_type == "MULTIPLICATION":
    print("You are now doing {operation_type}.")
    first_factor = input("Please input the first factor: ")
    second_factor = input("Please input the second factor: ")
    print("Okay, here is the answer!")
    print(first_factor*second_factor)
elif operation_type == "DIVISION":
    print("You are now doing {operation_type}.")
    dividend = input("Please input the dividend: ")
    divisor = input("Please input the divisor: ")
    print("Okay, here is the answer!")
    print(dividend/divisor)
else:
    print("Sorry, that is an invalid mathematical operation! Please try again.")