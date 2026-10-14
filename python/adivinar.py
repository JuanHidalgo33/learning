import random
def choose_difficult():

    difficulties = { 
        1:{"name": "Easy",
            "max": 10,
            "tries": 5
        },

        2:{"name": "Medium",
            "max": 25,
            "tries": 10
        },

        3:{"name": "Hard",
            "max": 50,
            "tries": 15
        }
    }

    print("---CHOOSE A DIFFICULTY---")

    for option, difficulty in difficulties.items():
        print(f"{option}.{difficulty['name']} (O to {difficulty['max']}, TRIES: {difficulty['tries']})")

    while True:
        try: 
            choice = int(input("Difficulty: "))
        except ValueError:
            print("Enter a valid answer.")
            continue

        if choice in difficulties:
            difficulty = difficulties[choice]
            max_range = difficulty["max"]
            tries = difficulty["tries"]
            secret_number = random.randint(0, max_range)

            return secret_number, max_range, tries   
     
        print("Enter a valid answer.")

def ask_number(max_range):
    while True:   
        try:
            user_number = int(input("Enter a number: "))
        except ValueError:
            print("Enter an integer.")
            continue

        if user_number < 0 or user_number > max_range:
            print(f"Number must be between 0 and {max_range}.")
        else:
            return user_number

def game():
    secret_number, max_range, tries  = choose_difficult()
    while tries > 0:
        user_number = ask_number(max_range)
        tries = tries_manager(tries)
        if secret_number == user_number:      
            win(tries) 
            return   
        elif secret_number < user_number:
            print(f"Try a lower number\nremain tries: {tries}")
        elif secret_number > user_number: 
            print(f"Try a higher number\nremain tries: {tries}")
    game_over(secret_number)    

def win(tries):
    print("\n" + "-"*40 + "\n")
    print(f"CONGRATS!! YOU'VE GUESSED THE SECRET NUMBER WITH {tries} TRIES REMAINING")

def game_over(secret_number):
    print("\n" + "-"*40 + "\n")
    print(f"SORRY, YOU'VE LOSE :(\nTHE SECRET NUMBER WAS {secret_number}")
    
def tries_manager(tries):
    tries -= 1
    return tries

def reset():
    while True:
        answer = input("WOULD YOU LIKE TO PLAY AGAIN? (Yes/No): ").strip().lower()  

        if answer in ("yes", "no"):
            print("\n" + "-"*40 + "\n")
            return answer == "yes"            
        else:
            print("Enter a valid answer (Yes/No)")

def games_count(games):
    print(f"YOU'VE PLAYED {games} {'TIME' if games == 1 else 'TIMES'}")

def main():
    print("---TRY TO GUESS THE SECRET NUMBER---")
    games = 0 
    while True:
        games += 1
        game()
        if not reset():
            print("THANKS FOR PLAYING") 
            games_count(games) 
            break 
if __name__ == "__main__":
    main()