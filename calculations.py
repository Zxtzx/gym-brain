#Function to do Epely formula
def calculate_1rm(weight, reps):
    epely = weight * (1 + reps / 30)
    return epely

#Function that calculates total volume for 1 set of i
def calculate_setvol(weight, reps):
    set_volume = (weight * reps)
    return set_volume
