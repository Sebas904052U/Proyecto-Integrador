import socket
import sys

ip = sys.argv[1] if len(sys.argv) > 1 else "192.168.1.10"   # argumento solo para pruebas

c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    c.connect((ip, 5000))
    print("Conectado al servidor")

    # INICIO|v1=3;v2=3;b1=0;b2=0
    d = c.recv(1024).decode().split("|")[1].split(";")
    v1 = int(d[0][3:]); v2 = int(d[1][3:]); b1 = int(d[2][3:]); b2 = int(d[3][3:])

    ganador = 0
    while ganador == 0:
        print(f"\nVaquero 1: {v1} vidas, {b1} balas | Vaquero 2: {v2} vidas, {b2} balas")

        # Jugada del Jugador 2 (DF2: formato y reglas)
        ok = 0
        while ok != 1:
            t = input("Vaquero 2 - 1 Disparar, 2 Recargar, 3 Defenderse: ")
            if not t.isdigit() or int(t) < 1 or int(t) > 3:
                print("Accion no valida, elige solo entre 1, 2, 3")
            elif b2 == 0 and int(t) == 1:
                print("No tienes balas, debes recargar")
            else:
                a2 = int(t); ok = 1

        c.send(f"ACCION|{a2}".encode())
        print("Esperando al Jugador 1...")
        msg = c.recv(1024).decode()
        if msg == "":
            raise ConnectionError("El servidor se desconecto")
        if msg.startswith("ERROR"):
            print(msg)
            continue

        # RESULTADO|ronda=1|v1=3|v2=3|b1=1|b2=1|msg=...
        p = msg.split("|")
        v1 = int(p[2][3:]); v2 = int(p[3][3:]); b1 = int(p[4][3:]); b2 = int(p[5][3:])
        texto = p[6][4:]
        print("Ronda terminada.", texto)
        if texto == "Gano el vaquero 1": ganador = 1
        if texto == "Gano el vaquero 2": ganador = 2
except (ConnectionError, OSError) as e:
    print("Error de red:", e)
c.close()
