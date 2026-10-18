import random
def choose_difficult():

    difficulties = { 
        1:{"name": "Easy",
            "max": 10,
            "max_tries": 5
        },

        2:{"name": "Medium",
            "max": 25,
            "max_tries": 10
        },

        3:{"name": "Hard",
            "max": 50,
            "max_tries": 15
        }
    }

    print("---CHOOSE A DIFFICULTY---")

    for option, difficulty in difficulties.items():
        print(f"{option}.{difficulty['name']} (O to {difficulty['max']}, MAX TRIES: {difficulty['max_tries']})")

    while True:
        try: 
            choice = int(input("Difficulty: "))
        except ValueError:
            print("Enter a valid answer.")
            continue

        if choice in difficulties:
            difficulty = difficulties[choice]
            max_range = difficulty["max"]
            max_tries = difficulty["max_tries"]
            secret_number = random.randint(0, max_range)

            return difficulty, secret_number, max_range, max_tries   
     
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
    difficulty, secret_number, max_range, max_tries  = choose_difficult()
    tries_remaining = max_tries
    attempts = 0
    while tries_remaining > 0:
        user_number = ask_number(max_range)
        tries_remaining -= 1
        attempts += 1
        if secret_number == user_number:      
            win(tries_remaining) 
            return True, attempts, tries_remaining, difficulty
        elif secret_number < user_number and tries_remaining > 0:
            print(f"Try a lower number\nremain tries: {tries_remaining}")
        elif secret_number > user_number and  tries_remaining > 0: 
            print(f"Try a higher number\nremain tries: {tries_remaining}")
    game_over(secret_number)
    return False, attempts, tries_remaining, difficulty

def win(tries_remaining):
    print("\n" + "-"*40 + "\n")
    print(f"CONGRATS!! YOU'VE GUESSED THE SECRET NUMBER WITH {tries_remaining} TRIES REMAINING")

def game_over(secret_number):
    print("\n" + "-"*40 + "\n")
    print(f"SORRY, YOU'VE LOSE :(\nTHE SECRET NUMBER WAS {secret_number}")

def reset():
    while True:
        answer = input("WOULD YOU LIKE TO PLAY AGAIN? (Yes/No): ").strip().lower()  

        if answer in ("yes", "no"):
            print("\n" + "-"*40 + "\n")
            return answer == "yes"            
        else:
            print("Enter a valid answer (Yes/No)")

def games_count(games, wins, loses, total_attempts):
    print(f"YOU'VE PLAYED {games} {'TIME' if games == 1 else 'TIMES'}")
    print(f"YOUR RESULTS\nWins: {wins}\nLoses: {loses}\nTotal attempts: {total_attempts}")

def main():
    print("---TRY TO GUESS THE SECRET NUMBER---")
    games = 0
    wins = 0
    loses = 0 
    total_attempts = 0
    history = []
    while True:
        games += 1
        result, attempts, tries_remaining, difficulty = game()
        total_attempts += attempts

        if result:
            wins += 1
        else: 
            loses += 1

        result_text = "Win" if result else "Lose"

        history.append({"result": result_text, "difficulty": difficulty['name'], "attempts": attempts, "tries_remaining": tries_remaining})
        
        if not reset():
            print("THANKS FOR PLAYING") 
            games_count(games, wins, loses, total_attempts)
            print("GAME HISTORY")
            for numero, partida in enumerate(history, start=1):
                print(f"Game {numero}: {partida['result']} | Difficulty: {partida['difficulty']} | Attempts: {partida['attempts']} | Tries remaining: {partida['tries_remaining']}")
            break

if __name__ == "__main__":
    main()