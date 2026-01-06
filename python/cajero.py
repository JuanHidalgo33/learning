import sys

def menu():
    print("\n" + "-"*40 + "\n")
    print("---BIENVENIDO AL CAJERO AUTOMÁTICO---")
    while True:
        print("1. Ver saldo. \n2. Transferir dinero. \n3. Retirar dinero. \n4. Cambiar clave. \n0. Salir.")
        try:
            option = int(input("INGRESE EL NÚMERO DE LA OPCIÓN QUE DESEA: "))
            if option in [0, 1, 2, 3, 4, ]:
                return option
            else:
                print("Ingrese una opción válida.")
        except ValueError:
            print("Por favor ingrese una opción válida ") 

def validatePassword(password):
    while True:
        if len(password) != 4 or not password.isdigit() or password in ('1234', '4321'):
            print("EL PIN DEBE TENER 4 DÍGITOS")
            password = input("Ingrese su PIN: ")
            continue
        return password

def changePassword(password):
    while True: 
        newPassword = input("Ingrese su nueva contraseña (4 Dígitos): ")

        if not newPassword.isdigit():
            print("Ingrese un PIN de 4 dígitos")
            continue
        elif newPassword == password:
            print("Ingrese un PIN diferente a la actual.")
            continue
        elif len(newPassword) != 4:
            print("El PIN debe ser de 4 digitos.")
            continue
        else:
            confirmPassword = input("Confirme su nuevo PIN: ")
            if not confirmPassword.isdigit():
                print("Ingrese un PIN de 4 dígitos")
                continue
            elif confirmPassword == newPassword:
                password = newPassword
                return password
            else:
                print("El PIN no es igual, vuelva a intentarlo.")

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

def again():
    while True:
        answer = input("Desea realizar otra operación? (Si/No):").strip().lower()

        if answer not in ('si', 'no'):
            print("Respuesta no válida. Por favor ingrese 'Si' o 'No'.")
            continue
        elif answer != 'si':
            print("    GRACIAS POR USAR NUESTRO SERVICIO!")
            sys.exit()
        else:
            break
            
        
def atm(option, password, balance):
        if option == 0:
            print("    GRACIAS POR USAR NUESTRO SERVICIO!")
            sys.exit()

        if option == 1:
            print(f"\nSu saldo actual es de {balance}")
            print("\n" + "-"*40 + "\n")
            again()
            return password, balance
        
        elif option == 2:
            balance = transferMoney(balance)
            print("\n" + "-"*40 + "\n")
            again()
            return password, balance


def main():
    print("---BIENVENIDO AL CAJERO AUTOMÁTICO---")
    print("SI ES SU PRIMERA VEZ USANDO EL SERVICIO DEBE CREAR UN NUEVO PIN")  
    balance = 1_500_000 
    while True:
        optionPIN = input("1. Ya tengo un PIN\n2. Crear un nuevo PIN\nIngrese su opción: ")
        if optionPIN == "1":
            password = input("Ingrese su PIN: ")
            password = validatePassword(password)
        elif optionPIN == "2":
            password = changePassword('')
        else:
            print("Opción no válida.")
            continue
        break    

    while True:
        option = menu()
        password, balance = atm(option, password, balance)

if __name__ == "__main__":
    main()