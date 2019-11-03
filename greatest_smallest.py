"""This program reads input from user. If input is "done", then end the program and print the min
and max numbers entered If the input is a number, store the integer as largest variable and
smallest variable and repromput user. Continue to prompt user for input and evaluate what
largest and smallest variables were, until "done" is entered. Add an exception that says if the
input is not an integer, and the input is not equal to "done", throw exeption error and reprompt
for input.
"""

largest = None
smallest = None
while True:
    num = input("Enter a number ('done' to quit):")
    if num != "done":
        try:
            check = int(num)
        except ValueError:
            print("Invalid Input")
            continue
        else:
            num = int(num)
            if largest is None:
                largest = int(num)
            if smallest is None:
                smallest = int(num)
            if num >= largest:
                largest = int(num)
            if num <= smallest:
                smallest = num
    if num == "done":
        print("Largest Number input is", largest)
        print("Smallest Number input is", smallest)
        break
