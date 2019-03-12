# Will Waldorf
# Python Final Project
# Average of soccer shots

#Greeting
name = input("What is your name: ")

def greeting():
    print("Hi there " + name + "!")
    print ('Its nice to meet you ! ')

greeting()

# Asking amount of games that are wanted to be averaged

try:
    how_many_games = int(input("Enter how many games you would like to average?: "))
    print('Your amount of games you would like to average: ', str(how_many_games))

except ValueError:
    print('That was not a proper number')

print("")

# Asking amount of shots wanted to be averaged
total = 0
totals = 0
for i in range(how_many_games):
    number_of_shots = int(input('\n''How many shots did you take in this game?: '))
    number_of_made_shots = int(input('\n''How many shots did you make in this game?: '))
    total = total + number_of_shots
    totals = totals + number_of_made_shots

print("")

# Average Number of shots per games
average = total / totals
print('\n')

x = total


print ('Shot Percentage: ' + str(round(average, 2)))


print('The average number of shots you made was ', str(round(average, 2)), 'goals per game')