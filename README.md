# Proyecto-Integrador
Python
Pisto Pistolero

Proyecto integrador de primer nivel · Lógica de Programación · UIDE · Paralelo [C]

Juego por turnos para dos jugadores con modo local y, más adelante, modo multijugador cliente-servidor en red LAN.

En cada ronda, los dos vaqueros eligen a la vez una acción: disparar, recargar o defenderse. Cada vaquero empieza con 3 vidas y 0 balas. Gana quien deje al rival sin vidas; si ambos llegan a 0 a la vez, se juega una muerte súbita con 1 vida y 1 bala para cada uno.

Integrantes
Mateo Diaz
Emilliano Roman

Cómo ejecutarlo


python juego.py          (menú)
python game_logic.py     (validación de la jugada y fin de la partida)

Modo en red LAN (en desarrollo): el Jugador 1 inicia el servidor y el Jugador 2 se conecta como cliente indicando la IP del servidor (puerto 5000).

python server.py                 (Jugador 1 · espera la conexión)
python cliente.py [IP_servidor]  (Jugador 2 · por defecto 192.168.1.10)
Reglas y acciones
Opción	Acción	Efecto
1	Disparar	Gasta una bala. Quita una vida al rival si este no se defendió. Se rechaza si no tienes balas.
2	Recargar	Suma una bala.
3	Defender	Te protege del disparo del rival en esa ronda.

Cualquier otra entrada se rechaza con un mensaje y se vuelve a pedir la jugada.

Estructura del repositorio:

juego.py	Menú que se repite hasta «Salir»: 1 Jugar / 2 Salir; al jugar se elige el modo (Local, Servidor o Cliente) y se ejecuta el script correspondiente (parte de DF1)	Terminado

game_logic.py	Validación de la jugada (DF2: acción válida y balas suficientes) y fin de la partida (DF3: ganador y muerte súbita)	Terminado

server.py	Servidor TCP en el puerto 5000 para el Jugador 1: recibe la jugada del Jugador 2, valida, resuelve la ronda y le envía el resultado	Iniciado

cliente.py	Cliente TCP para el Jugador 2: se conecta al servidor, envía su acción y muestra el resultado de cada ronda	Iniciado

Diseno/	Diagramas .rap de la Fase 2	[Subido / Pendiente de subir]

LICENSE	Licencia MIT	Subido

Del diseño al código

DF1 Partida completa (solo el menú)	juego.py, líneas [1-23]	[El ciclo del menú pasó a ser un while opcion != 2 que se repite hasta elegir «Salir»; la entrada no numérica se trata como opción inválida.]

DF2 Validación de la jugada	game_logic.py, líneas [...]	[El Loop del diagrama pasó a ser un while que repite la pregunta mientras la acción no sea 1, 2 o 3, o se intente disparar sin balas.]

DF3 Fin de la partida	game_logic.py, líneas [...]	[Las decisiones del diagrama pasaron a if que revisan las vidas: ambos en 0 activa la muerte súbita (1 vida y 1 bala); solo uno en 0 declara ganador al otro.]


Video explicativo
https://drive.google.com/file/d/15Lho12QJb34_ETsrVE7p_YaFI0AeFm95/view?usp=sharing


</details>
Licencia

Este proyecto se distribuye bajo la licencia [MIT]. El texto completo está en el archivo LICENSE.

Declaración de autoría

Declaramos que el código de este repositorio fue escrito por los integrantes del equipo, salvo los recursos citados en la sección «Créditos».

Créditos
Recurso (código, librería, imagen…)	Autor o fuente	Dónde se usa	Licencia
Biblioteca estándar de Python (socket, etc.)	Python Software Foundation	server.py, cliente.py	PSF
Uso de IA

Herramienta	Para qué la usamos	Qué revisamos o cambiamos nosotros
Claude (Anthropic)	Corrección del código de juego.py	[Qué revisamos o cambiamos nosotros: ej. probamos el menú y comprobamos que los cambios sugeridos funcionaran]
Claude| Correcion del Codigo|Las fallas presentadas en el menu y desarrollo del juego fueron consultadas y arregladas con la ayuda de Claude.
