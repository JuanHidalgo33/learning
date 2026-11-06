import sys

def menu():
    print("---GESTOR DE CONTACTOS---")  
    contacts = createAgenda()

    while True:
        print("1. Agregar contactos. \n2. Eliminar contactos. \n3. Editar contactos. \n0. Salir.")
        option = input("SELECIONE UNA OPCIÓN: ")

        if option == "0":
            print("\nGRACIAS POR USAR EL GESTOR DE CONTACTOS")
            print("           HASTA LA PROXIMA           ")
            break
        elif option == "1":
            addContact(contacts)
        elif option == "2":
            deleteContact(contacts)
        elif option == "3":
            editContact(contacts)
        else:
            print("INGRESE UNA OPCIÓN VÁLIDA\n")

def createAgenda():
    return []

def showContacts(contacts):
    if not contacts:
        print("No hay contactos guardados")
    else:   
        print("\n--- CONTACTOS GUARDADOS ---")
        for contact in contacts:
            name = contact["name"]
            lastName = contact["lastName"]
            phoneNumber = contact["phoneNumber"]
            print(f"{name} {lastName} {phoneNumber}\n")

def addContact(contacts):
    keep = True
    while keep:
        name = input("INGRESE EL NOMBRE DE SU CONTACTO: ").strip().lower()
        lastName = input("INGRESE EL APELLIDO DE SU CONTACTO: ").strip().lower()
        phoneNumber = input("INGRESE EL NÚMERO DE SU CONTACTO: ").strip()
        
        if not name and not lastName:
            print("Por favor ingrese un nombre válido\n")
            continue
        elif not phoneNumber or len(phoneNumber) < 10:
            print("Ingrese un número de contacto válido (min 10 digitos).\n")
            continue

        exists = any(c["name"] == name and c["lastName"] == lastName
                     for c in contacts)
        
        if exists: 
            print("Ya existe este contacto.")
            continue
        else:
            contacts.append({"name": name, 
                             "lastName": lastName,
                             "phoneNumber": phoneNumber})
            print("Contacto registrado con éxito")

        while True:           
            again = input("Desea agregar otro contacto? (si/no): ").strip().lower()
            if again not in ["si", "no"]:
                print("Ingrese una respuesta válida.")
                continue
            elif again != "si":
                keep = False
                break
            break
    showContacts(contacts)
     
def deleteContact(contacts):
    keep = True
    while keep:
        if not contacts:
            print("No hay contactos almacenados.\n")
            break
        else:
            for idx, contact in enumerate(contacts, 1):
                print(f"{idx}. {contact['name']} {contact['lastName']} {contact['phoneNumber']}")
            
            while True:
                try:
                    delIndex = int(input("Seleccione con un número el contacto que desea eliminar?: "))

                    if 1 <= delIndex <= len(contacts):
                        del contacts[delIndex - 1]
                        print("Contacto eliminado con éxito.")

                        if contacts: 
                            while True:           
                                again = input("Desea eliminar otro contacto? (si/no): ").strip().lower()
                                if again not in ["si", "no"]:
                                    print("Ingrese una respuesta válida.")
                                    continue
                                elif again != "si":
                                    keep = False
                                    break
                        else:
                            print("No quedan más contactos.")
                            keep = False  
                    else: 
                        print("Opción no válida.")
                        continue        
                except ValueError:
                    print("Seleccione con un número.")
    showContacts(contacts)
             
def editContact(contacts):
    keep = True
    while keep:
        if not contacts:
            print("No hay contactos almacenados.\n")
            break
        else:
            for idx, contact in enumerate(contacts, 1):
                print(f"{idx}. {contact['name']} {contact['lastName']} {contact['phoneNumber']}")
            print("0. Cancelar acción.")

            try:
                editIndex = int(input("Seleccione con un número el contacto que desea editar?: "))

                if editIndex == 0:
                    keep = False
                    continue

                if 1 <= editIndex <= len(contacts):
                    contact = contacts[editIndex - 1]
                    while True:
                        print(f"EDITANDO A: {contact['name']} {contact['lastName']} {contact['phoneNumber']}")
                        print("1. Cambiar nombre. \n2. Cambiar apellido. \n3. Cambiar número. \n0. Salir")
                        try: 
                            editOption = int(input("SELECCIONE UNA OPCIÓN: "))
                        except ValueError:
                            print("Seleccione con un número.")
                            continue

                        if editOption == 0:
                            break
                        elif editOption == 1:
                            newName = input("INGRESE EL NUEVO NOMBRE DE SU CONTACTO: ").strip().lower()

                            if newName:
                                oldName = contact['name']
                                contact['name'] = newName
                                print(f"{oldName} se ha cambiado por {contact['name']} exitosamente")
                            else:
                                print("Nombre no válido")
                        
                        elif editOption == 2:
                            newLastName = input("INGRESE EL NUEVO APELLIDO DE SU CONTACTO: ").strip().lower()

                            if newLastName:
                                oldLastName = contact['lastName']
                                contact['lastName'] = newLastName
                                print(f"{oldLastName} se ha cambiado por {contact['lastName']} exitosamente")
                            else:
                                print("Apellido no válido")

                        elif editOption == 3:
                            newPhoneNumber = input("INGRESE EL NUEVO NUMERO DE SU CONTACTO: ").strip()

                            if newPhoneNumber and len(newPhoneNumber) >= 10:
                                oldPhoneNumber = contact['phoneNumber']
                                contact['phoneNumber'] = newPhoneNumber
                                print(f"{oldPhoneNumber} se ha cambiado por {contact['phoneNumber']} exitosamente")
                            else:
                                print("Número no válido")
                        else: 
                            print("Ingrese una opción válida. ")
                            
                    showContacts(contacts)

                    while True:
                        again = input("¿Desea editar otro contacto? (si/no): ").strip().lower()
                        if again in ["si", "no"]:
                            break
                        else:
                            print("Ingrese una respuesta válida.")
                    if again != "si":
                        keep = False
                else: 
                    print("Opción no válida.")
                    continue
            except ValueError:
                print("Seleccione con un número.")

def main():
    menu()

if __name__ == "__main__":
    main()