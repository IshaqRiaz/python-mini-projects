#A simple Rock, Paper, Scissors game in Python using basic concepts like loops, conditions, and randomization. The user plays against the computer, scores are tracked, and invalid inputs are handled. Players can quit anytime by pressing 'q'. A fun beginner-friendly project to practice Python fundamentals.


print("Welcome to the Calculator project")
while True:
    print("Enter your q to quit at any time")
    #getting the first input from the user
    first_number = input("Please enter your first number: ")
    #termination of calculation due to "q" selection
    if first_number == "q":
        print("Calculation has been Terminated!")
        break
    #conversion of input to float
    first_number = float(first_number)
    #getting the second input from the user
    second_number = input("Please enter your second number: ")
    #termination of calculation due to "q" selection
    if second_number == "q":
        print("Calculation has been Terminated!")
        break
    #conversion of input to float
    second_number = float(second_number)
    #Main program execution
    operation = input("Which operation do you want to perform i.e +,-,/,*: ")
    # + operation
    if operation == "+":
        sum  = first_number + second_number
        print("The sum (+) of Both numbers are: ", sum)
    # - operation
    elif operation == "-":
        difference  = first_number - second_number
        print("The Difference (-) of Both numbers are: ", difference)
    # * operation
    elif operation == "*":
        multiply  = first_number * second_number
        print("The Multiply (*) of Both numbers are: ", multiply)
    # / operation
    elif operation == "/":
        #controlling of devident by zero
        if second_number == 0:
            print("Error: 0 can't be used as a devident")
        else:
            result = first_number / second_number
            print("The devident (/) of Both numbers are: ", result)
else:
    print("Invalid choice")
    
print("Thank you for your time")