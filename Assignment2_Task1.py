input_int = int(input("Enter a positive number: "))
if input_int <= 0:
    print(input_int, " is not a positive number")
elif (input_int % 2 == 0):
    print(input_int, " is an even number")
else:
    print(input_int, " is an odd number")

