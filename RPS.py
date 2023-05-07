#RPS game 
#imports
import random


#List of choices for the cpu
choices = ['r', 'p', 's']


#function that plays the game
def evaluate_game(user_input):
    #computer chooses what to play, then we look at what the user chose and play the game accordingly
    cpu_choice = random.sample(choices, 1)[0]
    if user_input.lower().strip() not in choices:
        #assuming the user does something dumb we kill the function here and deal with things later
        return 'invalid choice'
    
    if user_input == cpu_choice:
        #the values are wrapped in a tuple so we can move them around later
        return ('t', cpu_choice, 'you tied!')    
    #I think the logic here could be more concise, however this is still an important part of the learning process to share
    if (user_input == 'r' and cpu_choice == 'p') or (user_input == 'p' and cpu_choice == 's') or (user_input == 's' and cpu_choice == 'r'):
        return ('l', cpu_choice, 'you lost!')
    
    return ('w', cpu_choice, 'you won!')

#let's really play now
#This is everything I need to know for later
playing = True
wins = 0
ties = 0
losses = 0
already_played = False


while playing:
    #While this is nested to all hell, this avoids asking the user if the want to play twice on replay
    if not already_played:
        ask = input("would you like to play rock paper scissors? Y/N\n")
        if ask.lower().strip() == 'n':
            playing = False
            break
        elif ask.lower().strip() != 'y':
            print("answer Y/N, try again")
            continue
            

    user_choice = input("Choose: R/P/S\n")
    info = evaluate_game(user_choice)
    
    #need all if/elifs to avoid counting invalid inputs as losses
    if info[0] == 'w':
        wins += 1
    elif info[0] == 't':
        ties += 1
    elif info[0] == 'l':
        losses += 1
    if info == 'invalid choice':
        print('Invalid input, try again')
        continue
    else:
        print(info[2], f'your opponent chose {info[1]}, your current record against them is:\n{wins}-{ties}-{losses}')
        
    
    replay = input('would you like to play again? Y/N\n')
    if replay.lower().strip() == 'n':
        print('Good Game!')
        playing = False
        break
    else:
        already_played = True
        continue