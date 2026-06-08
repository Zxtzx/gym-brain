
from validators import get_exercise, get_int, get_float, get_again
from calculations import calculate_1rm, calculate_setvol

#Loop that exeecutes main scipt and finds how many sets to calculate
while True:
    exercise = get_exercise()
    sets = get_int(f"How many sets did you do for {exercise}?: ")
    volume = 0
    best_1rm = 0
    best_1rm_set = 0
    
#Loop for the amount of sets entered beforehand 
    for i in range(sets):
        print(f"Set {i + 1}")
        weight = get_float(f"What weight did you do for set {i + 1} of {exercise}?: ")
        reps = get_int(f"How many reps of {weight:.0f} lbs did you do for Set {i + 1} of {exercise}?: ")
        
        epely = calculate_1rm(weight, reps)
        if epely > best_1rm:
            best_1rm = epely
            best_1rm_set = (i + 1)

        set_volume = calculate_setvol(weight, reps)
        volume = set_volume + volume
    print()
    print("=" * 30)
    print(f"Exercise: {exercise}")
    print(f"Your estimated 1RM for {exercise} is {best_1rm:.0f} from Set {best_1rm_set}!")
    print(f"Your total volume for {sets} Sets of {exercise} is {volume:.0f} lbs!")
    print("=" * 30)
    
    again = get_again()
    if not again:
        print("Thank you")
        quit()      