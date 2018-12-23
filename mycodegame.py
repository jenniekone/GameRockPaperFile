"""
Created on Mon Dec 17 17:33:01 2018
@author: Jennie
"""

moves = ['rock', 'paper', 'scissors']

import random

#Create player class
class Player:
    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):
        pass
        
        
#Create random player class
class RandomPlayer:
    def __init__(self):
        Player.__init__(self)
            
    def move(self):
        
        #use imported random function & choice
        choices = ['Rock', 'Paper', 'Scissors']
        random_player = random.choice(choices)
        
        #Computer choice is either rock, paper, or scissors 
        if random_player == ("Rock"): 
            print("Opponent played Rock")
            
        elif random_player == ("Paper"): 
            print("Opponent played Paper")
            
        else: 
            print("Opponent played Scissors") 
        
        #return value 
        return random_player  
      
        
#Create human player class        
class HumanPlayer:
    def __init__(self):
        Player.__init__(self)
            
    def move(self):
        while True:
            human_player = input("'Rock', 'Paper', or 'Scissors' ")
        #Detect invalid entry
            if human_player.lower() not in moves:
                print('Please choose Paper, Rock or Scissors: ')
            else:
                break
            
        return human_player
      
    
            
##class that remembers what move the opponent played last round
class ReflectPlayer:
    def __init__(self, ReflectPlayer):
        Player.__init__(self)
        self.ReflectPlayer = ReflectPlayer
    
    # def move 
    def move(self, move):
        self.move = move
        
    def getmove(self, move):
        return self.move
      
            
#define cycleplayer class that remembers what move it played last round,
# and cycles through the different moves. 
class CyclePlayer:
    def __init__(self, CyclePlayer):
        Player.__init__(self)
        self.CyclePlayer = CyclePlayer
        
        self.human_player_history = {}  # stores the frequency of human player moves
        for move in moves:
            self.human_player_history[move] = 0


    def move(self, max_move):
        max_move = max(self.human_player_history.items(), key=lambda elem: elem[1])[0]
        if max_move == 'rock':
            return 'paper'
        if max_move == 'scissors':
            return 'rock'
        if max_move == 'paper':
            return 'rock' 


def beats(move1, move2):
    
    if ((move1 == 'rock' and move2 == 'rock') or

         (move1 == 'paper' and move2 == 'paper') or

         (move1 == 'scissors' and move2 == 'scissors')):

        return "** It's a TIE **"
    

    elif ((move1 == 'rock' and move2 == 'scissors') or

          (move1 == 'scissors' and move2 == 'paper') or

          (move1 == 'paper' and move2 == 'rock')):

        return "** Human WINS **"

    else:

        return "** Random Player WINS **"



#Create game class
class Game:
    def __init__(self, human_player, random_player):
        self.player1 = human_player
        self.player2 = random_player
        self.player1_score = 0
        self.player2_score = 0


    def play_round(self):            
        move1 = self.player1.move()
        move2 = self.player2.move()
        print(f"Player 1: {move1}  Player 2: {move2}")
        
        if (move1 == move2):
            print("it's a tie!")
            
        elif beats(move1, move2) is True:
                self.player1_score += 1
                
        elif beats(move2, move1) is True:
                self.player2_score += 1
                    
        print(f"Scores, HumanPlayer: {self.player1_score} RandomPlayer: {self.player2_score}")
    
    
    def play_game(self):    
        print("Game start!")
        for round in range(4):
            print(f"Round {round}:")
            self.play_round()
        print("Game over!")


if __name__ == '__main__':
    game = Game(HumanPlayer(), RandomPlayer())
    game.play_game()


