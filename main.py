from services.agenda import AgendaLogica

def mostrar_menu():
    print("\n" + "="*40)
    print("   🕵️ AGENDA SECRETA DE SHERLOCK HOLMES")
    print("="*40)
    print("1. Cargar agenda desde archivo")
    print("2. Agregar contacto")
    print("3. Buscar contacto por nombre")
    print("4. Buscar contacto por teléfono")
    print("5. Mostrar el promedio de edad de los contactos")
    print("6. Mostrar todos los contactos cargados")
    print("7. Salir del programa")
    print("="*40)

def main():
    agenda = AgendaLogica()

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción (1-7): ")

        if opcion == '1':
            print("\nOpciones de carga:")
            print("a. Cargar desde archivo JSON")
            print("b. Cargar desde archivo CSV")
            sub_op = input("Elige (a/b): ").lower()
            
            if sub_op == 'a':
                ruta = input("Ingresa el nombre del archivo (ej. datos.json): ")
                agenda.cargar_desde_archivo('json', ruta)
            elif sub_op == 'b':
                ruta = input("Ingresa el nombre del archivo (ej. datos.csv): ")
                agenda.cargar_desde_archivo('csv', ruta)
            else:
                print("\n[!] Opción inválida.")

        elif opcion == '2':
            print("\n--- Nuevo Contacto ---")
            nombre = input("Nombre: ")
            telefono = input("Teléfono: ")
            email = input("Email: ")
            edad = input("Edad: ")
            residencia = input("Residencia: ")
            
            if edad.isdigit():
                agenda.agregar_contacto(nombre, telefono, email, edad, residencia)
            else:
                print("\n[!] Error: La edad debe ser un número entero.")

        elif opcion == '3':
            nombre_parcial = input("\nIngrese el nombre (o fragmento) a buscar: ")
            resultados = agenda.buscar_por_nombre(nombre_parcial)
            if resultados:
                print(f"\nSe encontraron {len(resultados)} coincidencia(s):")
                for r in resultados: print(r)
            else:
                print("\n[-] No se encontraron coincidencias.")

        elif opcion == '4':
            telefono_parcial = input("\nIngrese el teléfono (o fragmento) a buscar: ")
            resultados = agenda.buscar_por_telefono(telefono_parcial)
            if resultados:
                print(f"\nSe encontraron {len(resultados)} coincidencia(s):")
                for r in resultados: print(r)
            else:
                print("\n[-] No se encontraron coincidencias.")

        elif opcion == '5':
            promedio = agenda.promedio_edad()
            print(f"\n📊 El promedio de edad de los contactos es: {promedio:.2f} años")

        elif opcion == '6':
            contactos = agenda.mostrar_todos()
            if contactos:
                print(f"\n--- Lista de Contactos ({len(contactos)}) ---")
                for c in contactos: print(c)
            else:
                print("\n[-] La agenda está vacía o no se ha cargado ningún archivo.")

        elif opcion == '7':
            print("\nSaliendo del sistema... ¡Elemental, mi querido Watson! 🔎")
            break

        else:
            print("\n[!] Opción inválida, por favor intenta de nuevo.")

if __name__ == "__main__":
    main()
