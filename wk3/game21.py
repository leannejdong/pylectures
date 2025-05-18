#---------Step 1  SET UP ------------#
import random
import time
import pyfiglet

while True:
    
#     print(r"""Welcome to the 21 Game!
#     - Take turns by adding 1, 2 or 3.
#     - Do NOT exceed 21!
#     - Th player who lands exactly on 21 **loses**.
#     """)

    print(pyfiglet.figlet_format("The 21 Game"))
    
    current_number = 1
    
    # Human or Computer
    if random.randint(0,1) == 0:
        current_player = "human"
    else:
        current_player = "computer"
        
    # Set up another while loop to track current score
    
    while current_number <= 21:
        print("The current number is " + str(current_number) + ".")
        print()
        
        # Player turn
        
        if current_player == "human":
            print("Add 1, 2, or 3. Do not pass 21. The player who lands on 21 loses")
            
            player_choice = ""
            while player_choice not in ["1", "2", "3"]:
                player_choice = input("What will you add? ")
                
            player_choice = int(player_choice)
            current_number = current_number + player_choice
            print()
            
            if current_number >=21:
                print("The current number is " + str(current_number) + ".")
                print()
                print("Sorry, you lose.")
                break
            current_player = "computer"
            
        else:
            computer_choice = random.randint(1,3)
            current_number = current_number + computer_choice
            print("Computer turn. The computer choses " + str(computer_choice) + ".")
            print()
            time.sleep(1)
            
            if current_number >= 21:
                print("The current number is " + str(current_number) + ".")
                print()
                print("Well done, you won!")
                break
            current_player = "human"
            
    # Do you want to play again? ---#
    print()
    play_again = input("Do you want to play again? ")
    if play_again.lower().startswith("y"):
        continue
    else:
        print("Goodbye")
        break 
    
