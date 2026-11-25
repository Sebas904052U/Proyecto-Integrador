
opcion = 0
while opcion != 2:
    print("\n1 Jugar, 2 Salir")
    t = input("Elige una opción: ")
    opcion = int(t) if t.isdigit() else 0

    if opcion == 1:
        print("\n1 Local (misma PC), 2 Servidor (Jugador 1), 3 Cliente (Jugador 2)")
        modo = input("Elige el modo: ")
        if modo == "1":
            exec(open("game_logic.py", encoding="utf-8").read())
        elif modo == "2":
            exec(open("server.py", encoding="utf-8").read())
        elif modo == "3":
            exec(open("client.py", encoding="utf-8").read())
        else:
            print("Modo no válido")
    elif opcion == 2:
        print("Juego finalizado")
    else:
        print("Opción no válida")

