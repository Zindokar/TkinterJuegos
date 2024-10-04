import tkinter as tk
from tkinter import ttk, IntVar
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
    canvas.create_window(180, 200, anchor="nw", window=boton_juego1)

    boton_juego2 = ttk.Button(root, text="Adivinar del inglés", command=juego2)
    canvas.create_window(180, 235, anchor="nw", window=boton_juego2)

    boton_juego3 = ttk.Button(root, text="Adivinar el número", command=juego3)
    canvas.create_window(178, 270, anchor="nw", window=boton_juego3)

    boton_salir = ttk.Button(root, text="Salir", command=root.destroy)
    canvas.create_window(210, 305, anchor="nw", window=boton_salir)

    root.mainloop()

def juego1():
    root.destroy()

    juego1_ventana = tk.Tk()
    juego1_ventana.resizable(False, False)
    juego1_ventana.title("Juegos AlexSoft - Piedra, papel o tijera")
    juego1_ventana.geometry("512x512")

    label = ttk.Label(juego1_ventana, text="Piedra papel tijera", padding=20)
    label.config(font=("Segoe UI", 20))  # Could be in the constructor instead.
    label.pack()

    boton_salir = ttk.Button(juego1_ventana, text="Salir", command=juego1_ventana.destroy)
    boton_salir.pack()

    juego1_ventana.mainloop()

def get_palabra_ingles():
    return list(palabras.keys())[random.randint(0, 19)]

def is_palabra_ok(palabra, palabra_jugador):
    return palabras[palabra.get()] == palabra_jugador.get()

def logica_juego2(palabra_jugador, palabra_maquina, puntuacion, intentos, entrada, respuesta, boton):
    print(f"Intentos: {intentos.get()} - Puntuación: {puntuacion.get()} - Palabra_J: {palabra_jugador.get()} - Palabra_M: {palabra_maquina.get()}")
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

def juego2():
    root.destroy()

    juego2_ventana = tk.Tk()
    juego2_ventana.resizable(False, False)
    juego2_ventana.title("Juegos AlexSoft - Adivinar del inglés")
    juego2_ventana.geometry("450x350")

    label = ttk.Label(juego2_ventana, text="Adivinar del inglés", padding=20)
    label.config(font=("Segoe UI", 20))  # Could be in the constructor instead.
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
    print(f"Numero {numero.get()} intentos {intentos.get()} aleatorio {aleatorio}")
    if intentos.get() > 0:
        intentos.set(intentos.get() - 1)
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

def juego3():
    root.destroy()

    juego3_ventana = tk.Tk()
    juego3_ventana.resizable(False, False)
    juego3_ventana.title("Juegos AlexSoft - Adivinar el número")
    juego3_ventana.geometry("450x400")

    numero_juego3 = tk.IntVar(master=juego3_ventana, value=0)
    intentos_juego3 = tk.IntVar(master=juego3_ventana, value=4)
    numero_aleatorio = random.randint(0, 200)

    titulo = ttk.Label(juego3_ventana, text="Adivinar el número del 0 al 200", padding=20)
    titulo.config(font=("Segoe UI", 20))
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
