import pandas as pd
import time
from tkinter import Tk
from tkinter.filedialog import askopenfilename
import pywhatkit as pwk

def enviar_mensaje(telefono, mensaje):
    pwk.sendwhatmsg_instantly(telefono, mensaje)

def leer_csv(archivo):
    df = pd.read_csv(archivo)
    columnas = df.columns.tolist()
    if 'telefono' in columnas and 'mensaje' in columnas:
        telefonos = df['telefono'].tolist()
        mensajes = df['mensaje'].tolist()
        for telefono, mensaje in zip(telefonos, mensajes):
            time.sleep(5)
            enviar_mensaje(telefono, mensaje)
            time.sleep(5)
            print(f"Mensaje enviado a {telefono}: {mensaje}")
    else:
        print("El archivo CSV no tiene las columnas 'telefono' y 'mensaje'.")

# Abrir ventana de búsqueda de archivos
Tk().withdraw()
archivo_csv = askopenfilename(filetypes=[('Archivos CSV', '*.csv')])

if archivo_csv:
    leer_csv(archivo_csv)
else:
    print("No se seleccionó ningún archivo.")
