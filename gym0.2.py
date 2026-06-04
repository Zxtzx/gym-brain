def get_again():
    while True:
        again = input("Would you like to calculate another exercise? (Yes/No): ").lower()

        if again == "yes":
            return True
        elif again == "no":
            return False
        else:
            print("Please enter a Yes or No!")

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

def get_exercise():
    while True:
            exercise = input("Please enter what exercise you have done: ")

            if exercise.isalpha():
                return exercise
                
            else:
               print("Please enter only letters!")

            
def get_calc(weight, reps):
    epely = weight * (1 + reps / 30)
    return epely
while True:
    exercise = get_exercise()
    sets = get_int(f"How many sets did you do for {exercise}?: ")
    volume = 0
    best = 0
    for i in range(sets):
        print(f"Set {i + 1}")
        weight = get_float(f"What weight did you do for set {i + 1} of {exercise}?: ")
        reps = get_int(f"How many reps of {weight:.0f} lbs did you do for Set {i + 1} of {exercise}?: ")
        
        epely = get_calc(weight, reps)
        if epely > best:
            best = epely

        
        set_volume = (weight * reps)
        volume = set_volume + volume

    print(f"Your estimated 1RM for {exercise} is {best:.0f}!")
    print(f"Your total volume for {sets} sets of {exercise} is {volume:.0f} lbs!")
    
    again = get_again()
    if not again:
        print("Thank you")
        quit()      