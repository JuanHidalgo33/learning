import random
import string

def randomPassword(length):
    while True: 
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for _ in range(length))
        
        if(any(c.islower() for c in password) and
        any(c.isupper() for c in password) and
        any(c.isdigit() for c in password) and
        any(c in string.punctuation for c in password)):
            return password

def askLength():
    while True:
        try:
            length = int(input("INGRESE EL TAMAÑO DE SU CONTRASEÑA\n(caracteres: Min: 8, Max: 20): ")) 
            if 8 <= length <= 20: 
                return length
            else:
                print("Ingrese nuevamente el tamaño de su contraseña")
        except ValueError:
            print("Ingrese unicamente números.")

def main():
    length = askLength()
    password = randomPassword(length)
    print(f"Su contraseña es: {password}")
    
if __name__ == "__main__":
    main()