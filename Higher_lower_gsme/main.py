import random
from game_data import data
from art import logo
from art import vs
from replit import clear

# Function to randomly select an account from the dataset

def assign():
    return random.choice(data)
# Function to compare the follower counts of two accounts

def compare(p1,p2,user_input):
    sum1=p1['follower_count']

    sum2=p2['follower_count']
    max=""
    if sum1>sum2:
        max=p1['name']
    elif sum1<sum2:
        max=p2['name']
    return max == user_input # Check if the user's guess returns True if user's guess is correct, otherwise False

# Main function to run the Higher or Lower game

def play_higher_lower():
    playing_game = True
    while playing_game: # outer loop to allow restarting the game

        score=0 # initialize score for a new game
        # Select initial two accounts
        p1 = assign()
        p2 = assign()

        # Ensure p1 and p2 are not the same account

        while p1==p2:
            p1 = p2
            p2 = assign()
        still_playing = True
        while still_playing: # inner loop for the current game round

            clear() # clear console for a clean display
            print(logo) # display game logo

            # Show account details (without follower counts)

            print(f" Name:{p1['name']},Desc:{p1['description']}")
            print(vs) # display "vs" art
            print(f"Name:{p2['name']},Desc:{p2['description']}")
            print("---------------------------------------------")
            print(f"Your current score is: {score}")
            print("---------------------------------------------")
            guess=input("Enter name of person with Higher followers:")

            if compare(p1,p2,guess):
                score+=1
                p1=p2
                p2=assign()
                while p1==p2:
                    p2=assign()
            else:
                still_playing=False # end game if guess is wrong
                print(f"Wrong Final score is {score}")
        print('Do you want to keep playing the game:')
        answer=input('>')
        if answer == 'y':
            continue # restart the game
        elif answer == 'n':
            playing_game = False # exit outer loop and stop game
            clear()
            print("Game Exited successfully")

        else:
            print("Invalid input taken as no.")


#Testing the code
want_to_play = input("Want to play (y/n): ").lower()
if want_to_play == 'y':
    clear()
    play_higher_lower()
elif want_to_play == 'n':
    print("Program exit Successful.")
else:
    print("Wrong input. Try again.Program Exited")


