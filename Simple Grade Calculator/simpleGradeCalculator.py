print("Hello! Welcome to the Grade Evaluator.")
finalGrade = 0
assignmentCount = 0
while True:
    grade = int(input("What is the grade you received on your assignment? (0-100): "))
    finalGrade += grade
    assignmentCount += 1
    repeat = input("Would you like to add another grade? (y/n): ")
    if repeat == "y":
        continue
    elif repeat == "n":
        break
    else:
        print("Sorry, that wasn't a valid response. Please restart ")
        exit()
finalGrade = finalGrade / assignmentCount

if finalGrade >= 90:
    print("Your final grade is an A.")
elif finalGrade >= 80:
    print("Your final grade is a B.")
elif finalGrade >= 70:
    print("Your final grade is a C.")
elif finalGrade >= 60:
    print("Your final grade is a D.")
elif finalGrade < 60:
    print("Your final grade is an F.")
else:
    print("Sorry, something went wrong. Please restart the program.")