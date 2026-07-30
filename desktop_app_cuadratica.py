import tkinter as tk
from tkinter import messagebox

ventana = tk.Tk()
ventana.title("Calculadora de Ecuaciones Cuadráticas")
ventana.geometry("1080x720")
ventana.configure(bg="#ffffff")

#=============================
# TITULO
#=============================

titulo = tk.Label(
    ventana,
    text="Resolutor de Ecuaciones Cuadráticas",
    font=("Arial",20,"bold"),
    bg="#f4f6f9",
    fg="#222222"
)
titulo.pack(pady=15)

#=============================
# FRAME IZQUIERDO
#=============================

frame_izq = tk.Frame(
    ventana,
    bg="white",
    bd=1,
    relief="solid"
)

frame_izq.place(x=50,y=80,width=420,height=560)

lbl_coef = tk.Label(
    frame_izq,
    text="Coeficientes",
    font=("Arial",16,"bold"),
    bg="white"
)
lbl_coef.pack(pady=15)

#=============================
# COEFICIENTE A
#=============================

lblA = tk.Label(
    frame_izq,
    text="Coeficiente a (cuadrático)",
    font=("Arial",11),
    bg="white"
)

lblA.pack(anchor="w", padx=25)

entryA = tk.Entry(
    frame_izq,
    font=("Arial",14),
    justify="center"
)

entryA.pack(padx=25,pady=8,fill="x")

#=============================
# COEFICIENTE B
#=============================

lblB = tk.Label(
    frame_izq,
    text="Coeficiente b (lineal)",
    font=("Arial",11),
    bg="white"
)

lblB.pack(anchor="w", padx=25)

entryB = tk.Entry(
    frame_izq,
    font=("Arial",14),
    justify="center"
)

entryB.pack(padx=25,pady=8,fill="x")

#=============================
# COEFICIENTE C
#=============================

lblC = tk.Label(
    frame_izq,
    text="Coeficiente c (independiente)",
    font=("Arial",11),
    bg="white"
)

lblC.pack(anchor="w", padx=25)

entryC = tk.Entry(
    frame_izq,
    font=("Arial",14),
    justify="center"
)

entryC.pack(padx=25,pady=8,fill="x")

#=============================
# BOTONES
#=============================

btnCalcular = tk.Button(
    frame_izq,
    text="Calcular Raíces",
    font=("Arial",13,"bold"),
    bg="#1f2937",
    fg="white",
    cursor="hand2",
    height=2
)

btnCalcular.pack(fill="x", padx=30, pady=35)

btnLimpiar = tk.Button(
    frame_izq,
    text="Limpiar Campos",
    font=("Arial",13),
    bg="white",
    fg="black",
    cursor="hand2",
    height=2
)

btnLimpiar.pack(fill="x", padx=30)

#=============================
# FRAME DERECHO
#=============================

frame_der = tk.Frame(
    ventana,
    bg="white",
    bd=1,
    relief="solid"
)

frame_der.place(x=500,y=80,width=530,height=560)

tituloResultado = tk.Label(
    frame_der,
    text="Resultados del Cálculo",
    font=("Arial",16,"bold"),
    bg="white"
)

tituloResultado.pack(pady=15)

#=============================
# RAICES
#=============================

frameRaices = tk.Frame(frame_der,bg="white")
frameRaices.pack()

#------ Raíz X1 ------

caja1 = tk.Frame(
    frameRaices,
    bg="#f8f9fa",
    bd=1,
    relief="solid"
)

caja1.grid(row=0,column=0,padx=15)

tk.Label(
    caja1,
    text="Raíz X₁",
    font=("Arial",11),
    bg="#f8f9fa"
).pack(pady=8)

lblX1 = tk.Label(
    caja1,
    text="0.0000",
    font=("Arial",22,"bold"),
    bg="#f8f9fa"
)

lblX1.pack(pady=12,padx=40)

#------ Raíz X2 ------

caja2 = tk.Frame(
    frameRaices,
    bg="#f8f9fa",
    bd=1,
    relief="solid"
)

caja2.grid(row=0,column=1,padx=15)

tk.Label(
    caja2,
    text="Raíz X₂",
    font=("Arial",11),
    bg="#f8f9fa"
).pack(pady=8)

lblX2 = tk.Label(
    caja2,
    text="0.0000",
    font=("Arial",22,"bold"),
    bg="#f8f9fa"
)

lblX2.pack(pady=12,padx=40)

#=============================
# TIPO DE SOLUCION
#=============================

tk.Label(
    frame_der,
    text="Tipo de Solución",
    font=("Arial",13,"bold"),
    bg="white"
).pack(anchor="w",padx=20,pady=(30,5))

lblTipo = tk.Label(
    frame_der,
    text="Esperando cálculo...",
    font=("Arial",12),
    bg="#eef2ff",
    width=48,
    anchor="w"
)

lblTipo.pack(padx=20)

#=============================
# PROCEDIMIENTO
#=============================

tk.Label(
    frame_der,
    text="Proceso de Resolución",
    font=("Arial",13,"bold"),
    bg="white"
).pack(anchor="w",padx=20,pady=(30,5))

txtProceso = tk.Text(
    frame_der,
    width=55,
    height=11,
    font=("Consolas",10),
    bd=1,
    relief="solid"
)

txtProceso.pack(padx=20,pady=5)


Frame_1 = tk.Frame(ventana, borderwidth=1, relief="solid", bg="#F3F3F3")


ventana.mainloop()

