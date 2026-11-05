import sys

def convert_Temperature(value, from_unit, to_unit):
    conversions = {
        ('c', 'f'): lambda v: (v * 9/5) + 32,
        ('c', 'k'): lambda v: v + 273.15,
        ('f', 'c'): lambda v: (v - 32) * 5/9,
        ('f', 'k'): lambda v: (v - 32) * 5/9 + 273.15,
        ('k', 'c'): lambda v: v - 273.15,
        ('k', 'f'): lambda v: (v - 273.15) * 9/5 + 32,
    }

    try:
        return conversions[(from_unit.lower(), to_unit.lower())](value)
    except KeyError:
        return  "Conversión no válida"

def convert_length(value, from_unit, to_unit):
    to_meters = {
        "mm": lambda v: v / 1000,
        "cm": lambda v: v / 100,
        "m": lambda v: v, #No se usa 
        "km": lambda v: v * 1000,
        "ft": lambda v: v / 3.28084,
        "mi": lambda v: v * 1609.34,
        "yd": lambda v: v / 1.09361,
        "in": lambda v: v / 39.3701,
    }
    
    from_meters = {
        "mm": lambda v: v * 1000,
        "cm": lambda v: v * 100,
        "m": lambda v: v, #No se usa
        "km": lambda v: v / 1000,
        "ft": lambda v: v * 3.28084,
        "mi": lambda v: v / 1609.34,
        "yd": lambda v: v * 1.09361,
        "in": lambda v: v * 39.3701,
    }

    try:
        meters = to_meters[from_unit.lower()](value)
        return from_meters[to_unit.lower()](meters)
    except KeyError:
        return "Conversión no válida"

def convert_mass(value, from_unit, to_unit):    
    to_grams = {
        "mg": lambda v: v/1000,
        "g": lambda v: v,
        "kg": lambda v: v*1000,
        "tn": lambda v: v*1000000,
        "lb": lambda v: v*453.6,
        "oz": lambda v: v*28.35
    }

    from_grams = {
        "mg": lambda v: v*1000,
        "g": lambda v: v,
        "kg": lambda v: v/1000,
        "tn": lambda v: v/1000000,
        "lb": lambda v: v/453.6,
        "oz": lambda v: v/28.35
    }

    try:
        grams = to_grams[from_unit.lower()](value)
        return from_grams[to_unit.lower()](grams)
    except KeyError:
        return "Conversión no válida"

def convert_time(value, from_unit, to_unit):
    to_minutes = {
        "s": lambda v: v / 60,
        "m": lambda v: v,
        "h": lambda v: v * 60,
        "d": lambda v: v * 1440,          # 24 * 60
        "sem": lambda v: v * 10080,         # 7 * 1440
        "mes": lambda v: v * 43829.1,       # 30.44 * 1440
        "año": lambda v: v * 525960         # 365.25 * 1440
    }

    from_minutes = {
        "s": lambda v: v * 60,
        "m": lambda v: v,
        "h": lambda v: v / 60,
        "d": lambda v: v / 1440,
        "sem": lambda v: v / 10080,
        "mes": lambda v: v / 43829.1,
        "año": lambda v: v / 525960
    }

    try:
        minutes = to_minutes[from_unit.lower()](value)
        return from_minutes[to_unit.lower()](minutes)    
    except KeyError:
        return "Conversión no válida"

def ask_data(unit1, unit2):
    print(f"CONVIRTIENDO DE {unit1} A {unit2}")
    while True:
        try: 
            value = float(input(f"INGRESE EL VALOR EN {unit1} (Números enteros o decimales, sin caracteres especiales): "))
            return value
        except ValueError:
            print("Ingrese un valor válido")

def menus():
    return """
    1. Conversor de temperaturas.
    2. Conversor de longitud.
    3. Conversor de masa.
    4. Conversor de tiempo.
    0. Salir."""

def convert_again():
    while True: 
        answer = input("Desea seguir usando el convetidor? /(si/no): ").strip().lower()

        if answer in ("si", "no"):
            return answer == "si"            
        else:
            print("Ingrese una respuesta valida (Si/No)")

def temperature_menu():
    units = {1: "c", 2: "f", 3: "k"}
    names = {1: "CELSIUS", 2: "FARENHEIT", 3: "KELVIN"}
    print("---CONVERSOR DE UNIDADES DE TEMPERATURAS---")
    while True:
        try:
            for k in units:
                print(f"{k}. {names[k]}")
            print("0. Salir")
            option = int(input("SELECCIONE UNA OPCIÓN: "))

            if option == 0:
                break
            elif option not in units:
                print("Opción no válida")
                continue

            from_unit = units[option]
            from_name = names[option]

            print("\n" + "-"*40 + "\n")
            print("A QUÉ UNIDAD DESEA CONVERTIR?")
            for k in units:
                if k != option:
                    print(f"{k}. {names[k]}")
            print("0. Salir")

            option2 = int(input("SELECCIONE LA UNIDAD DESTINO: "))
            if option2 == 0:
                continue
            if option2 not in units or option2 == option:
                print("Opción inválida")
                continue

            to_unit = units[option2]
            to_name = names[option2]

            print("\n" + "-"*40 + "\n")
            value = ask_data(from_name, to_name)
            result = convert_Temperature(value, from_unit, to_unit)
            print(f"RESULTADO: {value}º{from_unit.upper()} = {round(result, 2)}º{to_unit.upper()}")
            print("\n" + "-"*40 + "\n")

            if not convert_again():
                sys.exit("HASTA LA PRÓXIMA")

        except ValueError:
            print("Ingrese una opción válida")

def lenght_menu():
    units = {1: "mm", 2: "cm", 3: "m", 4: "km", 5: "ft", 6: "mi", 7: "yd", 8: "in",}
    names = {1: "MILIMETROS", 2: "CENTIMETROS", 3: "METROS", 4: "KILOMETROS", 5: "PIES", 6: "MILLAS", 7: "YARDAS", 8: "PULGADAS"}
    print("---CONVERSOR DE UNIDADES DE LONGITUD---")
    while True:
        try:
            for k in units:
                print(f"{k}. {names[k]}")
            print("0. SALIR")
            option = int(input("SELECCIONE UNA OPCIÓN: "))

            if option == 0:
                break
            elif option not in units:
                print("Opción no válida")
                continue
                
            from_unit = units[option]
            from_name = names[option]

            print("\n" + "-"*40 + "\n")
            print("A QUÉ UNIDAD DESEA CONVERTIR?")
            for k in units:
                if k != option:
                    print(f"{k}. {names[k]}")
            print("0. SALIR")        

            option2 = int(input("SELECCIONE LA UNIDAD DESTINO: "))
            if option2 == 0:
                break
            elif option2 not in units or option2 == option:
                print("Opción no válida")
                continue

            to_unit = units[option2]
            to_name = names[option2]

            print("\n" + "-"*40 + "\n")
            value = ask_data(from_name, to_name)
            result = convert_length(value, from_unit, to_unit)
            print(f"RESULTADO: {value}{from_unit.upper()} = {round(result, 2)}{to_unit.upper()}")
            print("\n" + "-"*40 + "\n")

            if not convert_again():
                sys.exit("HASTA LA PRÓXIMA")

        except ValueError:
            print("Ingrese una opción válida")

def mass_menu():
    units = {1: "mg", 2: "g", 3: "kg", 4: "tn", 5: "lb", 6: "oz"}
    names = {1: "MILIGRAMOS", 2: "GRAMOS", 3: "KILOGRAMOS", 4: "TONELADAS", 5: "LIBRAS", 6: "ONZAS"}
    print("---CONVERSOR DE UNIDADES DE MASA---")
    while True:
        try:
            for k in units:
                print(f"{k}. {names[k]}")
            print("0. SALIR.")

            option = int(input("SELECCIONE UNA OPCION: "))

            if option == 0:
                break
            elif option not in units:
                print("Opción no válida")
                continue

            from_unit = units[option]
            from_name = names[option]
            
            print("\n" + "-"*40 + "\n")
            print("A QUÉ UNIDAD DESEA CONVERTIR?")
            for k in units:
                if k != option:
                    print(f"{k}. {names[k]}")
            print("0. SALIR.")

            option2 = int(input("SELECCIONE LA UNIDAD DESTINO: "))

            if option2 == 0:
                break
            elif option2 not in units or option2 == option:
                print("Opción no válida")
                continue

            to_unit = units[option2]
            to_name = names[option2]

            print("\n" + "-"*40 + "\n")
            value = ask_data(from_name, to_name)
            result = convert_mass(value, from_unit, to_unit)
            print(f"RESULTADO: {value}{from_unit.upper()} = {round(result, 2)}{to_unit.upper()}")
            print("\n" + "-"*40 + "\n")

            if not convert_again():
                sys.exit("HASTA LA PRÓXIMA")

        except ValueError:
            print("Ingrese una opción válida")

def time_menu():
    units = {1: "s", 2: "m", 3: "h", 4: "d", 5: "sem", 6: "mes", 7: "año"}
    names = {1: "SEGUNDOS", 2: "MINUTOS", 3: "HORAS", 4: "DIAS", 5: "SEMANAS", 6: "MESES", 7: "AÑOS",}
    print("---CONVERSOR DE UNIDADES DE TIEMPO---")
    while True:
        try:
            for k in units:
                print(f"{k}. {names[k]}")
            print("0. SALIR")

            option = int(input("SELECCIONE UNA OPCIÓN: "))

            if option == 0:
                break
            elif option not in units:
                print("Opción no válida")
                continue

            from_unit = units[option]
            from_name = names[option]

            print("A QUÉ UNIDAD DESEA CONVERTIR?")
            for k in units:
                if k != option:
                    print(f"{k}. {names[k]}")
            print("0. SALIR")

            option2 = int(input("SELECCIONE LA UNIDAD DESTINO: "))

            if option2 == 0:
                break
            elif option2 not in units or option2 == option:
                print("Opción no válida")
                continue

            to_unit = units[option2]
            to_name = names[option2]
            
            print("\n" + "-"*40 + "\n")
            value = ask_data(from_name, to_name)
            result = convert_time(value, from_unit, to_unit)
            print(f"RESULTADO: {value}{from_unit.upper()} = {round(result, 2)}{to_unit.upper()}")
            print("\n" + "-"*40 + "\n")

            if not convert_again():
                sys.exit("HASTA LA PRÓXIMA")
            
        except ValueError:
            print("Ingrese una opción válida")

def choose_menu(menu):
    if menu == 1:
        temperature_menu()
    elif menu == 2:
        lenght_menu()
    elif menu == 3:
        mass_menu()
    elif menu == 4:
        time_menu()

def main():
    while True:     
        print(f"---SELECCIONE EL CONVERSOR QUE DESEA---{menus()}")
        try:
            menu = int(input("SELECCIONE UNA OPCIÓN: "))
        except ValueError:
            print("Ingrese una opción válida")
            continue

        if menu == 0:
            print("HASTA LA PRÓXIMA")
            break
        elif menu in (1, 2, 3, 4):
            print("\n" + "-"*40 + "\n")
            choose_menu(menu)
        else: 
            print("Ingrese una opción válida\n")
            
if __name__ == "__main__":
    main()