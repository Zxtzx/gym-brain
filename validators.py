
#Ask user if they want to calculate another 1RM
def get_again():
    while True:
        again = input("Would you like to calculate another exercise? (Yes/No): ").lower()

        if again == "yes":
            return True
        elif again == "no":
            return False
        else:
            print("Please enter a Yes or No!")

#Get inputs for positive numbers that allow decimals
def get_float(question):
    while True:
        try:
            number = float(input(question))
            if number > 0:
                return number
            else:
                print("Please enter a positive number!")
        except ValueError:
            print("Please enter a valid number!")

#Get inputs for positive whole numbers
def get_int(question):
    while True:
        try:
            number = int(input(question))
            if number > 0:
                return number
            else:
                print("Please enter a positive number!")
        except ValueError:
            print("Please enter a whole number")

#Input for asking what exercise and handling errors
def get_exercise():
    while True:
            exercise = input("Please enter what exercise you have done: ")

            if exercise.replace(" ", "").isalpha():
                return exercise.title()
                
            else:
               print("Please enter only letters!")