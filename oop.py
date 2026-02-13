import random

class Game:
    def __init__(self):
        self.choices = ["r", "p", "s"]
        self.player_score = 0
        self.computer_score = 0
    def player_choice(self):
        choice = input("pick (r,p,s):")

        while choice not in self.choices:
            print("invalit choise")
            choice = input("pick (r,p,s):")
        return choice
    def computer_choice(self):
        choice = random.choice(self.choices)
        print(f"computer chose {choice}")
        return choice
    def winner(self, player, computer):
        if player == computer:
            print("it's a tie!")
            return "tie"
        elif (player == "r" and computer == "s") or \
             (player == "p" and computer == "r") or \
             (player == "s" and computer == "p"):
            print("you win")
            self.player_score += 1
            return "player"
        else:
            print("computer win")
            self.computer_score += 1
            return "computer"
    def show(self):
        print(f"you: {self.player_score}")
        print(f"computer: {self.computer_score}")
    def play(self):
        while self.player_score < 3 and self.computer_score < 3:
            player_choice = self.player_choice()
            computer_choice = self.computer_choice()
            
            self.winner(player_choice, computer_choice)
            self.show()

        print("game over")
        if self.player_score > self.computer_score:
            print("you won")
        else:
            print("computer won")
if __name__ == "__main__":
    game = Game()
    game.play()
    
    play_again = input("Play again (y,n) ")
    if play_again == "y":
        game = Game()
        game.play()