import sys

def menu():
    print("\n" + "-"*40 + "\n")
    while True:
        print("1. Ver saldo. \n2. Transferir dinero. \n3. Retirar dinero. \n4. Cambiar PIN. \n0. Salir.")
        try:
            option = int(input("INGRESE EL NÚMERO DE LA OPCIÓN QUE DESEA: "))
            if option in [0, 1, 2, 3, 4]:
                return option
            else:
                print("Ingrese una opción válida.")
        except ValueError:
            print("Por favor ingrese una opción válida ") 

def createPassword():
    x = 0
    while x < 3: 
        password = input("Ingrese su nuevo PIN(4 Dígitos): ")

        if not password.isdigit() or len(password) != 4 or password in ('1234', '4321'):
            print("Ingrese un PIN de 4 dígitos")
            x += 1
            continue
        
        break

    if x == 3:
        print("Ha excedido el número de intentos. Intente más tarde.") 
        return None
        
    x = 0
    while x < 3: 
        confirmPassword = input("Confirme su nuevo PIN: ")

        if not confirmPassword.isdigit() or len(confirmPassword) != 4:
            print("Ingrese un PIN de 4 dígitos")
            x += 1
            continue
        
        if confirmPassword != password:
            print("El PIN no es igual, vuelva a intentarlo.")
            x += 1
            continue
        
        print("Su PIN ha sido creado exitosamente.")
        return password
        
    print("Ha excedido el número de intentos. Intente más tarde.") 
    return None

def validatePassword(password):
    x = 0
    while x < 2: 
        if len(password) != 4 or not password.isdigit() or password in ('1234', '4321'):
            print("EL PIN DEBE TENER 4 DÍGITOS")
            password = input("Ingrese su PIN: ")
            x += 1
            continue

        return password
    
    print("Ha excedido el número de intentos. Intente más tarde.") 
    return None

def changePassword(password):
    x = 0
    while x < 3: 
        newPassword = input("Ingrese su nuevo PIN(4 Dígitos): ")

        if not newPassword.isdigit():
            print("Ingrese un PIN de 4 dígitos")
            x += 1
            continue
        
        if newPassword == password:
            print("Ingrese un PIN diferente a la actual.")
            x += 1
            continue
        
        if len(newPassword) != 4:
            print("El PIN debe ser de 4 dígitos.")
            x += 1
            continue

        confirmPassword = input("Confirme su nuevo PIN: ")
        if not confirmPassword.isdigit():
            print("Ingrese un PIN de 4 dígitos")
            x += 1
            continue
        
        if confirmPassword == newPassword:
            password = newPassword
            print("Su PIN ha sido cambiado exitosamente.")
            return password
        else:
            print("El PIN no es igual, vuelva a intentarlo.")
            x += 1

def validateAmountToTransfer(balance):
    while True:
        try:
            amount = int(input("Ingrese la cantidad que desea transferir: "))
        except ValueError:
            print("Ingrese una cantidad válida.")
            continue
        if amount < 1000:
            print("La cantidad mínima para transferir es de 1000.")
            continue
        elif amount > balance:
            print("No tiene saldo suficiente para realizar la transferencia.")
            continue

        return amount
    
def validateAccountNumber():
    while True:  
        to_account = input("Ingrese la cuenta a la que va a transferir el dinero: ")      
        if len(to_account) != 10 or not to_account.isdigit():
            print("Ingrese un numero de cuenta valido (10 digitos)") 
            continue

        return to_account

def transferMoney(balance):
    amount = validateAmountToTransfer(balance)

    to_account = validateAccountNumber()

    balance -= amount
    print(f"Se han transferido {amount} a la cuenta {to_account}. \nSu saldo actual es de {balance}.")

    return balance

def withdrawMoney(balance, password):
    while True:
        try:
            amount = int(input("Ingrese la cantidad que desea retirar: "))
        except ValueError:
            print("Ingrese una cantidad válida.")
            continue

        if amount < 5000:
            print("La cantidad mínima para retirar es de 5000.")
            continue
        elif amount > balance:
            print("No tiene saldo suficiente para realizar el retiro.")
            continue
        break

    pin = input("Ingrese su PIN para confirmar el retiro: ")
    if pin == password:
        print(f"Su saldo anterior era de {balance}. ")
        balance -= amount
        print(f"Ha retirado {amount}. \nSu saldo actual es de {balance}.")
        return balance
    else:
        print("Pin incorrecto. La transacción ha sido cancelada.")
        return balance

def again():
    while True:
        answer = input("Desea realizar otra operación? (Si/No):").strip().lower()

        if answer not in ('si', 'no'):
            print("Respuesta no válida. Por favor ingrese 'Si' o 'No'.")
            continue
        
        if answer != 'si':
            print("    GRACIAS POR USAR NUESTRO SERVICIO!")
            return None
        else:
            return True
            
        
def atm(option, password, balance):
        if option == 1:
            print(f"\nSu saldo actual es de {balance}")
            print("\n" + "-"*40 + "\n")
            answerAgain = again()
            return password, balance, answerAgain
        
        elif option == 2:
            balance = transferMoney(balance)
            print("\n" + "-"*40 + "\n")
            answerAgain = again()
            return password, balance, answerAgain
        
        elif option == 3:
            balance = withdrawMoney(balance, password)
            print("\n" + "-"*40 + "\n")
            answerAgain = again()
            return password, balance, answerAgain
        
        elif option == 4:
            password = changePassword(password)
            print("\n" + "-"*40 + "\n")
            answerAgain = again()
            return password, balance, answerAgain

def main():
    print("---BIENVENIDO AL CAJERO AUTOMÁTICO---")
    print("SI ES SU PRIMERA VEZ USANDO EL SERVICIO DEBE CREAR UN NUEVO PIN")  
    balance = 1_500_000 
    x = 0
    while x < 3: 
        optionPIN = input("1. Ya tengo un PIN\n2. Crear un nuevo PIN\nIngrese su opción: ")
        if optionPIN == "1":
            password = input("Ingrese su PIN: ")
            password = validatePassword(password)
        elif optionPIN == "2":
            password = createPassword()
        else:
            print("Opción no válida.")
            x += 1
            continue
        break    

    if x == 3:
        print("Ha excedido el número de intentos. Intente más tarde.") 
        sys.exit()

    if password is None:
        sys.exit()

    while True:
        option = menu()
        if option == 0:
            sys.exit()

        password, balance, answerAgain = atm(option, password, balance)
        
        if answerAgain is None :
            sys.exit() 
     

if __name__ == "__main__":
    main()