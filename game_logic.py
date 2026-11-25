v1 = 3
v2 = 3
b1 = 0
b2 = 0
ganador = 0
muerte = 0

print("ESTADO INICIAL")
print(f"Vaquero 1: {v1} vidas, {b1} balas")
print(f"Vaquero 2: {v2} vidas, {b2} balas")


while ganador == 0:
    print("\n----------------------------")
    if muerte == 1:
        print("Ronda de muerte súbita: 1 vida y 1 bala")

    
    print(f"Estado Vaquero 1 -> Vidas: {v1} | Balas: {b1}")
    print(f"Estado Vaquero 2 -> Vidas: {v2} | Balas: {b2}\n")

    
    ok1 = 0
    while ok1 != 1:
        a1 = int(input(f"Vaquero 1 ({v1} vidas, {b1} balas) - 1 Disparar, 2 Recargar, 3 Defenderse: "))
        if b1 == 0 and a1 != 2:
            print("No tiene balas debes recargar")
        elif a1 < 1 or a1 > 3:
            print("Accion no valida elige solo entre 1, 2, 3")
        else:
            ok1 = 1

    
    ok2 = 0
    while ok2 != 1:
        a2 = int(input(f"Vaquero 2 ({v2} vidas, {b2} balas) - 1 Disparar, 2 Recargar, 3 Defenderse: "))
        if b2 == 0 and a2 != 2:
            print("No tienes balas, debes recargar")
        elif a2 < 1 or a2 > 3:
            print("Accion no valida, solo elige entre 1, 2, 3")
        else:
            ok2 = 1

    
    if a1 == 2:
        b1 = b1 + 1
    if a1 == 1:
        b1 = b1 - 1

    if a2 == 2:
        b2 = b2 + 1
    if a2 == 1:
        b2 = b2 - 1

    if a1 == 1 and a2 != 3:
        v2 = v2 - 1
    if a2 == 1 and a1 != 3:
        v1 = v1 - 1

    print("\nRonda terminada. Se actualizaron las vidas y balas:")
    print(f"Vaquero 1: {v1} vidas, {b1} balas | Vaquero 2: {v2} vidas, {b2} balas")

    
    if v1 <= 0 and v2 <= 0:
        print("¡Muerte subita!")
        v1 = 1
        v2 = 1
        b1 = 1
        b2 = 1
        muerte = 1
    elif v2 <= 0:
        print("Gano el vaquero 1")
        ganador = 1
    elif v1 <= 0:
        print("Gano el vaquero 2")
        ganador = 2
    else:
        print("Continua la partida")

