import random

def choose_difficult():
    difficutlies ={
        "1": 10,
        "2": 100,
        "3": 1000
    }
    
    print("---ELIGE LA DIFICULTAD PARA JUGAR---")

def ask_number(max_range):
    while True:   
        try:
            user_number = int(input("Ingrese un número: "))
        except ValueError:
            print("Ingrese un número entero.")
            continue

        if user_number < 0 or user_number > max_range:
            print(f"El número debe estar entre 0 y {max_range}.")
        else:
            return user_number

def game():
    tries = 0
    secret_number, max_range = choose_difficult()
    while True:
        tries += 1 
        user_number = ask_number(max_range)
        if secret_number == user_number:         
            print("Has adivinado el numero")
            print("Numero de intentos ", tries)
            break
        elif secret_number < user_number: 
            print("Intenta con un número menor")
        elif secret_number > user_number: 
            print("Intenta con un número mayor")

def reset():
    while True:
        answer = input("Quisiera volver a jugar? (Si/No): ").strip().lower()  

        if answer in ("si", "no"):
            print("\n" + "-"*40 + "\n")
            return answer == "si"            
        else:
            print("Ingrese una respuesta valida (Si/No)")

def games_count(games):
    print(f"JUGASTE {games} {'VEZ' if games == 1 else 'VECES'}")

def main():
    print("---INTENTA ADIVINAR EL NÚMERO ALEATORIO---")
    games = 0 
    while True:
        games += 1
        game()
        if not reset():
            print("GRACIAS POR JUGAR") 
            games_count(games) 
            break 
if __name__ == "__main__":
    main()