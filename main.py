import random
import string



def game_guesser():
    
     return random.choice("RPS") 
com_choice = game_guesser()
user_choice = input("Select your option(in Caps): ")

# def game_choice():
#     globals()["com_choice"] = game_guesser
#     globals()["user_choice"] = input("Select either 'R', 'P', or 'S'")

def check():
    
  
    if(com_choice == user_choice):
        print("IT'S A DRAW")
    elif((com_choice == "P") and (user_choice == "R")):
        print("You lose")
    elif((com_choice == "R") and (user_choice == "S")):
        print("You lose")
    elif((com_choice == "S") and (user_choice == "P")):
        print("You lose")
    elif((com_choice == "P") and (user_choice == "S")):
        print("You won")
    elif((com_choice == "R") and (user_choice == "P")):
        print("You won")
    elif((com_choice == "S") and (user_choice == "R")):
        print("You won")
    else:
        print("sorry better luck next time")

# print(game_guesser())

def game_fun():
   
    print("***Welcome to Rock-Paper-Scissors***")
    print(" R is for Rock. P is for paper. and S is for Scissors")
    com_choice = game_guesser()
    user_choice = input("Select your option(in Caps): ")
    
    

    valid_option = False
    while(valid_option == False):
        print(" R is for Rock. P is for paper. and S is for Scissors")
        com_choice = game_guesser()
        user_choice = input("Select your option(in Caps): ")
    
        # game_choice()
        
    

        if (user_choice == "R"):
            valid_option = True
            print("You have chosen Rock")
            print("COM says:" + com_choice)
            check()

        elif(user_choice == "P"):
            valid_option =True
            print("You have chosen Paper")
            print("COM says:" + com_choice)
            check()

        elif( user_choice == "S"):
            valid_option = True
            print("You have chosen Scissors")
            print("COM says:" + com_choice)
            check()

        else:
            print("You have selected the wrong option")
       
        
   
       


game_fun()