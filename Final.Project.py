# Asking amount of games that are wanted to be averaged

try:
    how_many_games = int(input("Enter how many games you would like to average?: "))
    print('Your amount of games you would like to average: ', str(how_many_games))

except ValueError:
    print('That was not a proper number')

print("")
