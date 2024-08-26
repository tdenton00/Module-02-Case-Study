""" 
Tyrece Denton
Module 02 Case Study
This program prompts the user to input their name, as well as their GPA. The program then tests to see if the user's
GPA is high enough to be on the Dean's list, or high enough to be on the honor roll.
"""

first_name = input("Enter your first name: ")
last_name = input("Enter your last name, or 'ZZZ' to quit: ")
if last_name == "ZZZ":
    quit()
full_name = first_name + " " + last_name
while True:
    try:
        user_GPA = float(input("Enter your GPA: "))
        if user_GPA <= 0 or user_GPA > 4.0:
            print("Invalid GPA.")
            continue
    except ValueError:
        print("Invalid input.")
        continue
    else:
        break

if user_GPA >= 3.5:
    print("Congratulation, " + full_name + ". You've made the Dean's List!")
elif user_GPA >= 3.25:
    print("Congratulations, " + full_name + ". You've made the Honor Roll!")
else:
    print("Sorry, " + full_name + ". You did not make the Dean's List or the Honor Roll.")
        
    