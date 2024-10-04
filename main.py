import tkinter as tk
from tkinter import ttk, IntVar
from tkinter import messagebox as alert
try:
    from ctypes import windll
    windll.shcore.SetProcessDpiAwareness(1)
except:
    pass
from PIL import Image, ImageTk
import random

def menu():
    root.resizable(False, False)
    root.title("Juegos AlexSoft")
    root.geometry("512x512")

    canvas = tk.Canvas(root, width=512, height=512)
    canvas.pack(fill="both", expand=True)
    logo_juego = Image.open("imagenes/logo.jpeg").resize((512,512))
    logo_juego_photo = ImageTk.PhotoImage(logo_juego)
    canvas.create_image(0, 0, image=logo_juego_photo, anchor="nw")
    canvas.create_text(256, 60, font="Helvetica 22 bold", fill="black", text="¡Elige el juego!")

    boton_juego1 = ttk.Button(root, text="Piedra papel tijera", command=juego1)
    canvas.create_window(256, 200, anchor="center", width="150", window=boton_juego1)

    boton_juego2 = ttk.Button(root, text="Adivinar del inglés", command=juego2)
    canvas.create_window(256, 235, anchor="center", width="150", window=boton_juego2)

    boton_juego3 = ttk.Button(root, text="Adivinar el número", command=juego3)
    canvas.create_window(256, 270, anchor="center", width="150", window=boton_juego3)

    estilos = ttk.Style()
    estilos.configure(
        style="Salir.TButton",
        foreground="red"
    )

    boton_salir = ttk.Button(root, text="Salir", style="Salir.TButton", command=root.destroy)
    canvas.create_window(256, 305, anchor="center", width="150", window=boton_salir)

    root.mainloop()

def cambiar_imagen_juego1(opcion_maquina, indice):
    imagenes_maquina = ["imagenes/piedra.jpg", "imagenes/papel.jpg", "imagenes/tijera.jpg"]
    imagen_nombre = imagenes_maquina[indice % 3]
    imagen_seleccionada = Image.open(imagen_nombre).resize((256, 256))
    imagen_final = ImageTk.PhotoImage(imagen_seleccionada)
    opcion_maquina.config(image=imagen_final)
    opcion_maquina.image = imagen_final

def resultado_juego1(opcion_jugador, opcion_maquina, resultado, boton_jugar):
    opcion_maquina_resultado = random.randint(0, 2)
    cambiar_imagen_juego1(opcion_maquina, opcion_maquina_resultado)
    resultados = [[0, -1, 1],
                  [1, 0, -1],
                  [-1, 1, 0]]
    if resultados[opcion_jugador.get()][opcion_maquina_resultado] == 0:
        resultado["text"] = "Has empatado."
    elif resultados[opcion_jugador.get()][opcion_maquina_resultado] == 1:
        resultado["text"] = "Has ganado."
    else:
        resultado["text"] = "Has perdido."
    boton_jugar["state"] = "normal"

imagen_indice = 0
def efecto_eleccion_maquina(opcion_maquina):
    global imagen_indice
    cambiar_imagen_juego1(opcion_maquina, imagen_indice)
    imagen_indice += 1

def logica_juego1(opcion_jugador, opcion_maquina, resultado, boton_jugar, ventana):
    # print(f"Jugador elige: {opcion_jugador.get()}")
    resultado["text"] = "Jugando..."
    boton_jugar["state"] = "disabled"
    timeline = 500
    for x in range(10):
        ventana.after(timeline, lambda: efecto_eleccion_maquina(opcion_maquina))
        timeline += 500
    ventana.after(timeline, lambda: resultado_juego1(opcion_jugador, opcion_maquina, resultado, boton_jugar))

def juego1():
    root.destroy()

    juego1_ventana = tk.Tk()
    juego1_ventana.resizable(False, False)
    juego1_ventana.title("Juegos AlexSoft - Piedra, papel o tijera")
    juego1_ventana.geometry("512x450")

    frame_titulo = tk.Frame(juego1_ventana)
    frame_titulo.pack(side="top")
    label = ttk.Label(frame_titulo, text="Piedra papel tijera", font=("Segoe UI", 20), padding=20)
    label.pack()

    frame_juego = tk.Frame(juego1_ventana)
    frame_juego.pack(side="top")

    frame_jugador = tk.Frame(frame_juego)
    frame_jugador.pack(side="left", fill="both", expand=True)
    tk.Label(frame_jugador, text="Elige opción").pack()
    opcion_jugador = tk.IntVar(master=juego1_ventana, value=0)

    frame_piedra = tk.Frame(frame_jugador)
    frame_piedra.pack(side="top", pady=(10,0))
    piedra = ttk.Radiobutton(frame_piedra, text="Piedra", variable=opcion_jugador, value=0)
    piedra_imagen_foto = ImageTk.PhotoImage(Image.open("imagenes/piedra.jpg").resize((64,64)))
    piedra_imagen = ttk.Label(frame_piedra, image=piedra_imagen_foto)
    piedra_imagen.pack(side="left")
    piedra.pack(side="left")

    frame_papel = tk.Frame(frame_jugador)
    frame_papel.pack(side="top", pady=(10,0))
    papel = ttk.Radiobutton(frame_papel, text="Papel", variable=opcion_jugador, value=1)
    papel_imagen_foto = ImageTk.PhotoImage(Image.open("imagenes/papel.jpg").resize((64,64)))
    papel_imagen = ttk.Label(frame_papel, image=papel_imagen_foto)
    papel_imagen.pack(side="left")
    papel.pack(side="left")

    frame_tijera = tk.Frame(frame_jugador)
    frame_tijera.pack(side="top", pady=(10,0))
    tijera = ttk.Radiobutton(frame_tijera, text="Tijera", variable=opcion_jugador, value=2)
    tijera_imagen_foto = ImageTk.PhotoImage(Image.open("imagenes/tijera.jpg").resize((64,64)))
    tijera_imagen = ttk.Label(frame_tijera, image=tijera_imagen_foto)
    tijera_imagen.pack(side="left")
    tijera.pack(side="left")

    boton_jugar = ttk.Button(frame_jugador, text="Jugar", command=lambda: logica_juego1(opcion_jugador, opcion_maquina, resultado_texto, boton_jugar, frame_maquina))
    boton_jugar.pack(side="top", pady=(15,0))

    frame_maquina = tk.Frame(frame_juego)
    frame_maquina.pack(side="right", fill="both", expand=True, padx=(60,0))
    tk.Label(frame_maquina, text="Opción máquina").pack(side="top")
    opcion_maquina_imagen_foto = ImageTk.PhotoImage(Image.open("imagenes/maquina_juego1.jpg").resize((256,256)))
    opcion_maquina = ttk.Label(frame_maquina, image=opcion_maquina_imagen_foto)
    opcion_maquina.pack(side="top")

    frame_resultado = tk.Frame(juego1_ventana)
    frame_resultado.pack(side="top")

    resultado_texto = ttk.Label(frame_resultado, text="Empieza a jugar, suerte novato.")
    resultado_texto.pack()

    ttk.Separator(frame_resultado, orient="horizontal").pack(fill="x", pady=(10, 10))

    boton_salir = ttk.Button(frame_resultado, text="Salir", command=juego1_ventana.destroy)
    boton_salir.pack()

    juego1_ventana.mainloop()

def get_palabra_ingles():
    return list(palabras.keys())[random.randint(0, 19)]

def is_palabra_ok(palabra, palabra_jugador):
    return palabras[palabra.get()] == palabra_jugador.get()

def logica_juego2(palabra_jugador, palabra_maquina, puntuacion, intentos, entrada, respuesta, boton):
    try:
        # print(f"Intentos: {intentos.get()} - Puntuación: {puntuacion.get()} - Palabra_J: {palabra_jugador.get()} - Palabra_M: {palabra_maquina.get()}")
        intentos.set(intentos.get() - 1)
        if is_palabra_ok(palabra_maquina, palabra_jugador):
            puntuacion.set(puntuacion.get() + 1)
        else:
            puntuacion.set(puntuacion.get() - 1)
        palabra_maquina.set(get_palabra_ingles())
        entrada["text"] = f"Adivina la palabra \"{palabra_maquina.get()}\""
        if intentos.get() > 1:
            respuesta["text"] = f"Sigue jugando, te quedan {intentos.get()} palabras."
        elif intentos.get() == 1:
            respuesta["text"] = f"Última palabra."
        else:
            respuesta["text"] = f"Has obtenido un {puntuacion.get()} puntos."
            boton["state"] = "disabled"
    except Exception:
        alert.showerror("Error", "Introduzca valores numéricos.")

def juego2():
    root.destroy()

    juego2_ventana = tk.Tk()
    juego2_ventana.resizable(False, False)
    juego2_ventana.title("Juegos AlexSoft - Adivinar del inglés")
    juego2_ventana.geometry("450x350")

    label = ttk.Label(juego2_ventana, text="Adivinar del inglés", font=("Segoe UI", 20), padding=20)
    label.pack()

    logo_juego2 = Image.open("imagenes/logo_juego2.jpeg").resize((124, 124))
    logo_juego2_photo = ImageTk.PhotoImage(logo_juego2)
    imagen_juego = ttk.Label(image=logo_juego2_photo)
    imagen_juego.pack(pady=(0,20))

    frame_input = tk.Frame(juego2_ventana)
    frame_input.pack()

    palabra_maquina = tk.StringVar(master=juego2_ventana, value=get_palabra_ingles())
    palabra_jugador = tk.StringVar(master=juego2_ventana)
    puntuacion_juego2 = tk.IntVar(master=juego2_ventana, value=0)
    intentos_juego2 = tk.IntVar(master=juego2_ventana, value=10)

    entrada_texto = ttk.Label(frame_input, text=f"Adivina la palabra \"{palabra_maquina.get()}\"")
    entrada_texto.pack(side="left")
    entrada = ttk.Entry(frame_input, width=10, textvariable=palabra_jugador)
    entrada.pack(side="left", padx=(5,0))
    entrada.focus()
    boton_jugar = ttk.Button(frame_input, text="Jugar", command=lambda: logica_juego2(palabra_jugador, palabra_maquina, puntuacion_juego2, intentos_juego2, entrada_texto, respuesta_texto, boton_jugar))
    boton_jugar.pack(side="left", padx=(10,0))

    ttk.Separator(juego2_ventana, orient="horizontal").pack(fill="x", pady=(10,10))

    respuesta_texto = ttk.Label(juego2_ventana, text=f"Empieza a jugar, tienes que adivinar {intentos_juego2.get()} palabras.")
    respuesta_texto.pack()

    boton_salir = ttk.Button(juego2_ventana, text="Salir", command=juego2_ventana.destroy)
    boton_salir.pack(pady=(10,0))

    juego2_ventana.mainloop()

def logica_juego3(numero: IntVar, aleatorio: int, intentos: IntVar, respuesta, boton_jugar):
    try:
        # print(f"Numero {numero.get()} intentos {intentos.get()} aleatorio {aleatorio}")
        intentos.set(intentos.get() - 1)
        if intentos.get() > 0:
            if numero.get() == aleatorio:
                respuesta["text"] = "¡Has ganado!"
                boton_jugar["state"] = "disabled"
            elif numero.get() > aleatorio:
                respuesta["text"] = f"Tu número es mayor, te quedan {intentos.get()} intentos."
            else:
                respuesta["text"] = f"Tu número es menor, te quedan {intentos.get()} intentos."
        else:
            respuesta["text"] = "Has agotado los intentos."
            boton_jugar["state"] = "disabled"
    except Exception:
        alert.showerror("Error", "Introduzca valores numéricos.")

def juego3():
    root.destroy()

    juego3_ventana = tk.Tk()
    juego3_ventana.resizable(False, False)
    juego3_ventana.title("Juegos AlexSoft - Adivinar el número")
    juego3_ventana.geometry("450x400")

    numero_juego3 = tk.IntVar(master=juego3_ventana, value=0)
    intentos_juego3 = tk.IntVar(master=juego3_ventana, value=4)
    numero_aleatorio = random.randint(0, 200)

    titulo = ttk.Label(juego3_ventana, text="Adivinar el número del 0 al 200", font=("Segoe UI", 20), padding=20)
    titulo.pack()

    logo_juego3 = Image.open("imagenes/logo_juego3.jpeg").resize((124, 124))
    logo_juego3_photo = ImageTk.PhotoImage(logo_juego3)
    imagen_juego = ttk.Label(image=logo_juego3_photo)
    imagen_juego.pack(pady=(0,20))

    frame_input = tk.Frame(juego3_ventana)
    frame_input.pack()

    entrada_texto = ttk.Label(frame_input, text="Número: ")
    entrada_texto.pack(side="left")
    entrada = ttk.Entry(frame_input, width=5, textvariable=numero_juego3)
    entrada.pack(side="left", padx=(5,0))
    entrada.focus()

    boton_jugar = ttk.Button(frame_input, text="Jugar", command=lambda: logica_juego3(numero_juego3, numero_aleatorio, intentos_juego3, respuesta_texto, boton_jugar))
    boton_jugar.pack(side="left", padx=(20,0))

    ttk.Separator(juego3_ventana, orient="horizontal").pack(fill="x", pady=(10,10))

    respuesta_texto = ttk.Label(juego3_ventana, text=f"Empieza a jugar, tienes {intentos_juego3.get()} intentos.")
    respuesta_texto.pack()

    ttk.Separator(juego3_ventana, orient="horizontal").pack(fill="x", pady=(10,10))

    boton_salir = ttk.Button(juego3_ventana, text="Salir", command=juego3_ventana.destroy)
    boton_salir.pack()

    juego3_ventana.mainloop()

palabras = {
    "hello":"hola",
    "bye":"adios",
    "spoon":"cuchara",
    "fork":"tenedor",
    "apple":"manzana",
    "banana":"platano",
    "name":"nombre",
    "airport":"aeropuerto",
    "helicopter":"helicoptero",
    "flower":"flor",
    "classroom":"aula",
    "computer":"ordenador",
    "screen":"pantalla",
    "wire":"cable",
    "mouse":"raton",
    "keyboard":"teclado",
    "cat":"gato",
    "dog":"perro",
    "strawberry":"fresa",
    "shoe":"zapato",
}
root = tk.Tk()
menu()
