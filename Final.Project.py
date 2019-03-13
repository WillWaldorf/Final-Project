# Asking amount of shots wanted to be averaged
total = 0
totals = 0
for i in range(how_many_games):
    number_of_shots = int(input('\n''How many shots did you take in this game?: '))
    number_of_made_shots = int(input('\n''How many shots did you make in this game?: '))
    total = total + number_of_shots
    totals = totals + number_of_made_shots

print("")


