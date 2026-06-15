# script for determining letter grade from user inputted number grade
# function to check if number
def is_number(num):
    try:
        float(num)
        return True
    except:
        return False

# define the variable for the loop to initially run
user_grade = ""

# take input (v1 assumes valid number input from the user)
while is_number(user_grade) == False:
    user_grade = input("Submit your current average: ")

    # if true, then make this into a number to check in the conditional
    if is_number(user_grade) == True:
        user_grade = float(user_grade)

# letter grade
user_letter = ""
# it will be a string, so check if it's either a digit or a float, anything else is invalid
if user_grade >= 90 and user_grade <= 100:
    print("Your grade is: A.")
    user_letter = "A"
elif user_grade >= 80 and user_grade < 90:
    print("Your grade is: B.")
    user_letter = "B"
elif user_grade >= 70 and user_grade < 80:
    print("Your grade is: C.")
    user_letter = "C"
elif user_grade >= 60 and user_grade < 70:
    print("Your grade is: D.")
    user_letter = "D"
elif user_grade >= 0 and user_grade < 60:
    print("Your grade is: F.")
    user_letter = "F"

# use pass set
pass_set = set("ABC")

print("Congrats!") if user_letter in pass_set else print("Try again.")