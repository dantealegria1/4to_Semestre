import math
import tkinter as tk

def f(x):
    return eval(user_function)

def Simpson():
    Limite_inferior = int(entry_limite_inferior.get())
    Limite_superior = int(entry_limite_superior.get())
    n = int(entry_intervalos.get())
    h = (Limite_superior - Limite_inferior) / n
    array = []
    array.append(Limite_inferior)
    for i in range(1, n + 1):
        array.append(array[i - 1] + h)

    suma = 0   
    for i in range(1, n):
        if i % 2 == 0:
            suma = suma + 2 * f(array[i])
        else:
            suma = suma + 4 * f(array[i])
    suma = suma + f(array[0]) + f(array[n]) 
    result = (h / 3) * suma
    label_result.config(text="El resultado de la integral es: " + str(result))

def calculate_integral():
    global user_function
    user_function = entry_function.get()
    Simpson()

# Crear la ventana de la interfaz gráfica
window = tk.Tk()
window.title("Cálculo de Integral")

# Estilos de la interfaz gráfica
window.configure(bg='#F4F4F4')
window.geometry("500x400")

# Centrar la ventana en la pantalla
window_width = window.winfo_reqwidth()
window_height = window.winfo_reqheight()
position_right = int(window.winfo_screenwidth() / 2 - window_width / 2)
position_down = int(window.winfo_screenheight() / 2 - window_height / 2)
window.geometry("+{}+{}".format(position_right, position_down))

title_label = tk.Label(window, text="Cálculo de Integral", font=("Arial", 16), bg='#F4F4F4')
title_label.pack(pady=20)

frame = tk.Frame(window, bg='#F4F4F4')
frame.pack()

# Etiqueta y entrada para la función
label_function = tk.Label(frame, text="Función:", font=("Arial", 12), bg='#F4F4F4')
label_function.grid(row=0, column=0, padx=10, pady=10)
entry_function = tk.Entry(frame, width=20, font=("Arial", 12))
entry_function.grid(row=0, column=1, padx=10, pady=10)

# Etiquetas y entradas para los límites y el número de intervalos
label_limite_inferior = tk.Label(frame, text="Limite inferior:", font=("Arial", 12), bg='#F4F4F4')
label_limite_inferior.grid(row=1, column=0, padx=10, pady=10)
entry_limite_inferior = tk.Entry(frame, width=10, font=("Arial", 12))
entry_limite_inferior.grid(row=1, column=1, padx=10, pady=10)

label_limite_superior = tk.Label(frame, text="Limite superior:", font=("Arial", 12), bg='#F4F4F4')
label_limite_superior.grid(row=2, column=0, padx=10, pady=10)
entry_limite_superior = tk.Entry(frame, width=10, font=("Arial", 12))
entry_limite_superior.grid(row=2, column=1, padx=10, pady=10)

label_intervalos = tk.Label(frame, text="Número de intervalos:", font=("Arial", 12), bg='#F4F4F4')
label_intervalos.grid(row=3, column=0, padx=10, pady=10)
entry_intervalos = tk.Entry(frame, width=10, font=("Arial", 12))
entry_intervalos.grid(row=3, column=1, padx=10, pady=10)

# Botón para calcular la integral
button_calcular = tk.Button(window, text="Calcular integral", font=("Arial", 12), command=calculate_integral)
button_calcular.pack(pady=20)

# Etiqueta para mostrar el resultado
label_result = tk.Label(window, text="", font=("Arial", 12), bg='#F4F4F4')
label_result.pack()

# Ejecutar la ventana de la interfaz gráfica
window.mainloop()
