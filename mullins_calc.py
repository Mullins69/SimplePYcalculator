print("Welcome to Mullins simple Calculator")
print("Do you want to use the calc, yes or no?")

question = input("yes or no, no caps: ")
if question == "yes":
    print("Which would you like to use, addition, subtraction , division or multiplication? ")
    question2 = input("no caps : ")
    if question2 == "addition":
        input1 = int(input("Please Enter Value 1: "))
        input2 = int(input("Please Enter Value 2: "))
        print(str(input1) + " plus " + str(input2) + " = " + str(input1 + input2)  )
        print("thank you for using my addition calculator , LOL ")
    if question2 == "subtraction":
        input1 = int(input("Please Enter Value 1: "))
        input2 = int(input("Please Enter Value 2: "))
        print(str(input1) + " minus " + str(input2) + " = " + str(input1 - input2))
        print("thank you for using my subtraction calculator , LOL ")
    if question2 ==  "division":
        input1 = int(input("Please Enter Value 1: "))
        input2 = int(input("Please Enter Value 2: "))
        print(str(input1) + " divide by " + str(input2) + " = " + str(input1 / input2))
        print("thank you for using my division calculator , LOL ")
    if question2 == "multiplication":
        input1 = int(input("Please Enter Value 1: "))
        input2 = int(input("Please Enter Value 2: "))
        print(str(input1) + " multiply by " + str(input2) + " = " + str(input1 * input2))
        print("thank you for using my multiplication calculator , LOL ")
else:
    print("why did you have to choose no? aii... ")
