import random
def roll():
    min_value = 1
    max_value = 6
    roll = random.randint(min_value, max_value)
    return roll
value = roll()
print(value)

while True:
  players = input('Enter the number of player(2-4): ')
  if players.isdigit:
     
     players = int(players)
     if 2<= players <=4 :
        break
     else : 
        print("Must be between 2-4 players")
else:

        print("Invalid , Try again.")

max_score = 50
players_score = [0 for _ in range(players)]

while max(players_score) < max_score:
    for players_idx in range(players):
        print("\n player number", players_idx + 1,"turn has just started!")
        print("Your total score is :", players_score[players_idx], )
        current_score = 0
        while True:
            should_roll = input("would you like to roll(y) ?")
            if should_roll.lower() != "y":
                break
            
            value = roll()
            if value == 1:
                print("You rolled a 1, Turn done!")
                break

            else:
                current_score += value
                print("You rolled a: ", value)
            print("Your score is: ", current_score)
        players_score[players_idx] += current_score
        print("Your total score is : ", players_score[players_idx])
            
max_score = max(players_score)       
winning_idx = players_score.index(max_score)   
print("Player number", winning_idx+1, "is the winner of the score of: ", max_score)
        

            



            


