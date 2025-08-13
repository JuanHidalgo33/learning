import tkinter as tk
from tkinter import *

 #Definir app como instancia de Tk
app = tk.Tk()
#Dimensiones de la ventana
app.geometry("320x480")
#Establecer fondo de la ventana
app.configure(background="gray")
#Establecer titulo de la ventana
tk.Wm.wm_title(app, "Calculadora")

exp = ""
entry = tk.StringVar(app)

def presionar(valor):
    global exp
    exp += str(valor)
    entry.set(exp)

def calcular():
    global exp
    try:
        answer = str(eval(exp))
        entry.set(answer)
        exp = answer
    except:
        entry.set("Error")
        exp = ""

#Creacion de entrada de texto
tk.Entry(
    app,
    fg='black',
    bg='white',
    justify='center',
    textvariable=entry
).grid( 
    row= 0,
    column= 0,
    columnspan= 4,
)

botones = [('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('+', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('-', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('/', 3, 3),
    ('=', 4, 1)]

for (text, row, column) in botones:
    if text == "=":
        cmd = calcular
    else: 
        cmd = lambda x = text: presionar(x)
    
    tk.Button(app, text= text, command=cmd, width=5, 
        height=5, cursor="hand2"   
    ).grid(
        row=row,
        column=column,
        sticky="nsew"
    )

# Hacer que las columnas y filas se expandan
for i in range(6):
    app.grid_rowconfigure(i, weight=1)
for i in range(4):
    app.grid_columnconfigure(i, weight=1)

app.mainloop()
