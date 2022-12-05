# ADVENT OF CODE 2022
# Day 1 - Calorie Counting

# init variables
elfTotalCalories = 0    # total for this elf
maxCalories = 0         # maximum calories
elfNumber = 0           # elf number

# open the provided input file
with open("01_Calorie_counting/input.txt", "r") as inFile:
    # foreach line
    for l in inFile:
        # if line is empty.
        if l == '\n':
            # onto the next elf
            elfNumber += 1
            # print for debugging purposes.
            print(f"Elf #{elfNumber} - Cals: {elfTotalCalories}")
            # update the maximum (if the number is bigger)
            maxCalories = max(elfTotalCalories, maxCalories)
            # reset calories for this elf
            elfTotalCalories = 0
        else:
            # increase this elf's total calories (parsing input as integer)
            elfTotalCalories += int(l)

print("Max calories are: ", maxCalories)
