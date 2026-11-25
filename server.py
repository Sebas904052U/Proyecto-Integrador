import socket
# (el menu 1 Jugar / 2 Salir lo da juego.py)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(("0.0.0.0", 5000))
s.listen(1)
print("Esperando al Jugador 2 en el puerto 5000...")
conn, addr = s.accept()
try:
    v1 = 3; v2 = 3; b1 = 0; b2 = 0; ganador = 0; muerte = 0; ronda = 1
    conn.send(f"INICIO|v1={v1};v2={v2};b1={b1};b2={b2}".encode())

    while ganador == 0:
        print(f"\nVaquero 1: {v1} vidas, {b1} balas | Vaquero 2: {v2} vidas, {b2} balas")

        # Jugada del Jugador 1 (DF2: formato y reglas)
        ok = 0
        while ok != 1:
            t = input("Vaquero 1 - 1 Disparar, 2 Recargar, 3 Defenderse: ")
            if not t.isdigit() or int(t) < 1 or int(t) > 3:
                print("Accion no valida, elige solo entre 1, 2, 3")
            elif b1 == 0 and int(t) == 1:
                print("No tienes balas, debes recargar")
            else:
                a1 = int(t); ok = 1

        # Jugada del Jugador 2 (se valida otra vez en el servidor)
        print("Esperando al Jugador 2...")
        ok = 0
        while ok != 1:
            msg = conn.recv(1024).decode()
            if msg == "":
                raise ConnectionError("El Jugador 2 se desconecto")
            a2 = int(msg.split("|")[1])
            if a2 < 1 or a2 > 3 or (b2 == 0 and a2 == 1):
                conn.send("ERROR|Accion no valida".encode())
            else:
                ok = 1

        # Resolver la ronda
        if a1 == 2: b1 = b1 + 1
        if a1 == 1: b1 = b1 - 1
        if a2 == 2: b2 = b2 + 1
        if a2 == 1: b2 = b2 - 1
        if a1 == 1 and a2 != 3: v2 = v2 - 1
        if a2 == 1 and a1 != 3: v1 = v1 - 1

        # Decidir resultado (DF3)
        if v1 <= 0 and v2 <= 0:
            texto = "¡Muerte subita!"
            v1 = 1; v2 = 1; b1 = 1; b2 = 1; muerte = 1
        elif v2 <= 0:
            texto = "Gano el vaquero 1"; ganador = 1
        elif v1 <= 0:
            texto = "Gano el vaquero 2"; ganador = 2
        else:
            texto = "Continua la partida"

        print("Ronda terminada.", texto)
        conn.send(f"RESULTADO|ronda={ronda}|v1={v1}|v2={v2}|b1={b1}|b2={b2}|msg={texto}".encode())
        ronda = ronda + 1
except (ConnectionError, OSError) as e:
    print("Error de red:", e)
conn.close()
s.close()
