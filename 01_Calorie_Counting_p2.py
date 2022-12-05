# ADVENT OF CODE 2022
# Day 1 - Calorie Counting

# init variables
elfCalorieTotals = set()       # list of total calories per elf

# open the provided input file
with open("01_Calorie_counting/input.txt", "r") as inFile:
    # temp var to store total.
    calorie_total = 0

    # for each line
    for l in inFile:
        # if line is empty.
        if l == '\n':
            # add current total to set
            elfCalorieTotals.add(calorie_total)

            # reset temp var
            calorie_total = 0
        else:
            # add to total
            calorie_total += int(l)

top_totals = sorted(elfCalorieTotals)
print(f"Top #3 - ", top_totals[-3:])

print(f"Total {sum(top_totals[-3:])}")
