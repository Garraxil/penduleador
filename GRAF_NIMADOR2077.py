import tkinter as tk
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.animation import FuncAnimation
import numpy as np
import heapq as hd 
import sympy as sym
from PIL import ImageTk, Image 

# hola <BRIAN

x = sym.symbols('x') 
plt.style.use('dark_background')


interfaz = tk.Tk() 
interfaz.title("Graficador Animado")
interfaz.resizable(0,0)


traer_imagen1 = Image.open("backroom2.png") 
traer_imagen1 = traer_imagen1.resize((700,500)) 
img = ImageTk.PhotoImage(traer_imagen1) 
lbl_img = tk.Label(interfaz,image=img) 
lbl_img.pack() 

#''' -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- '''
def graficar():
    ventana1 = tk.Toplevel(interfaz) 
    ventana1.title("Graficador") 
    ventana1.resizable(0,0)

    traer_imagen2 = Image.open("backroom1.png") # Traer imagen
    traer_imagen2 = traer_imagen2.resize((760,400)) # Tamaño
    img = ImageTk.PhotoImage(traer_imagen2) # Mostrar la imagen
    lbl_img = tk.Label(ventana1,image=img) # Asignar ventana
    lbl_img.pack() 

    eti1 = tk.Label(ventana1,text="F(x)", fg="blue",bg="black")
    eti1.place(x=100,y=20) 
    entrada1 = tk.Entry(ventana1,bg="black",fg="white")
    entrada1.place(width=150,height=25,x=100,y=60)
    
    eti3 = tk.Label(ventana1,text="Intervalo inferior",fg="blue",bg="black")
    eti3.place(x=360,y=60) 
    entrada3=tk.Entry(ventana1,bg="black",fg="white")
    entrada3.place(width=100,height=25,x=480,y=60)
    
    eti4 = tk.Label(ventana1,text="Intervalo superior",fg="blue",bg="black")
    eti4.place(x=360,y=20)
    entrada4 = tk.Entry(ventana1,bg="black",fg="white")
    entrada4.place(width=100,height=25,x=480,y=20)
    
    eti5 = tk.Label(ventana1,text="Color",fg="blue",bg="black")
    eti5.place(x=280,y=20)
    entrada5 =tk.Entry(ventana1,bg="black",fg="white")
    entrada5.place(width=60,height=25,x=280,y=60)
    
    etift = tk.Label(ventana1,text="Donde quiere encontar \n la tangente de F(x) = ",fg="blue",bg="black")
    etift.place(x=100,y=200)
    entradaft = tk.Entry(ventana1,bg="black",fg="white")
    entradaft.place(x=100,y=260)

    eti6 = tk.Label(ventana1,text="G(x)",fg="green",bg="black")
    eti6.place(x=100,y=100)
    entrada6 =tk.Entry(ventana1,bg="black",fg="white")
    entrada6.place(width=150,height=25,x=100,y=140)
    
    eti7 = tk.Label(ventana1,text="Color",fg="green",bg="black")
    eti7.place(x=280,y=100)
    entrada7 =tk.Entry(ventana1,bg="black",fg="white")
    entrada7.place(width=60,height=25,x=280,y=140)
    
    eti8 = tk.Label(ventana1,text="Intervalo inferior",fg="green",bg="black")
    eti8.place(x=360,y=140)
    entrada8 =tk.Entry(ventana1,bg="black",fg="white")
    entrada8.place(width=100,height=25,x=480,y=140)
    
    eti9 = tk.Label(ventana1,text="Intervalo superior",fg="green",bg="black")
    eti9.place(x=360,y=100)
    entrada9 = tk.Entry(ventana1,bg="black",fg="white")
    entrada9.place(width=100,height=25,x=480,y=100)
    
    etigt = tk.Label(ventana1,text="Donde quiere encontar \n la tangente de G(x) = ",fg="green",bg="black")
    etigt.place(x=300,y=200)
    entradagt = tk.Entry(ventana1,bg="black",fg="white")
    entradagt.place(x=300,y=260)

    class Fx: # Clases u objetos.
        def __init__(self ,fx): 
           self.fx = fx
    class Gx:
        def __init__(self ,gx):
           self.gx = gx
    class Nombre_Titulo(Fx,Gx):
        def __init__(self ,fx,gx):
            Fx.__init__(self, fx)
            Gx.__init__(self, gx)
        def nombre(self):
            s = "F(x) = " + self.fx + "  - y -  G(x) = " + self.gx
            return s

    def graficar_ambas():
        funcion_simbolica = entrada1.get()
        funcion_simbolica2 = entrada6.get()
        f = sym.lambdify(x,funcion_simbolica,"numpy")
        g = sym.lambdify(x,funcion_simbolica2,"numpy")
        
        dom = np.arange( float( entrada3.get() ), float( entrada4.get() ) , 0.1)
        dom2 = np.arange( float( entrada8.get() ), float( entrada9.get() ) , 0.1)
        
        objeto = Nombre_Titulo(funcion_simbolica, funcion_simbolica2)
        titulo_dos_funciones = objeto.nombre()
        
        plt.plot(dom,f(dom),label="Su funcion es = "+funcion_simbolica,color=entrada5.get())
        plt.plot(dom2,g(dom2),label="Su funcion es = "+funcion_simbolica2,color=entrada7.get())
        plt.plot(0,0,"o",color="yellow")
        plt.xlabel('$x$',size=12)
        plt.ylabel('$y$',size=12)
        plt.title(titulo_dos_funciones)
        plt.grid(color="white")
        plt.legend()
        plt.show()

    def graficar_f():
        funcion_simbolica = entrada1.get()
        f = sym.lambdify(x,funcion_simbolica,"numpy")
        dom = np.arange(float(entrada3.get()), float(entrada4.get()),0.1)
        
        plt.plot(dom,f(dom),label="Su funcion es = "+funcion_simbolica,color=entrada5.get())
        plt.plot(0,0,"o",color="yellow")
        plt.xlabel('$x$',size=12)
        plt.ylabel('$y$',size=12)
        plt.grid(color="white")
        plt.legend()
        plt.show()

    def graficar_g():
        funcion_simbolica2 = entrada6.get()
        g = sym.lambdify(x,funcion_simbolica2,"numpy")
        dom2 = np.arange(float(entrada8.get()),float(entrada9.get()),0.1)  
        
        plt.plot(dom2,g(dom2),label="Su funcion es = "+funcion_simbolica2,color=entrada7.get())
        plt.plot(0,0,"o",color="yellow")
        plt.xlabel('$x$',size=12)
        plt.ylabel('$y$',size=12)
        plt.grid(color="white")
        plt.legend()
        plt.show()

    def grafica_tangenteg():
        funcion_simbolica2 = entrada6.get()
        derivada_simbolica2 = sym.diff(funcion_simbolica2,x)
        g = sym.lambdify(x,funcion_simbolica2,"numpy")
        derivadag = sym.lambdify(x,derivada_simbolica2,'numpy')
        
        dom2 = np.arange(float(entrada8.get()),float(entrada9.get()),0.1)
        
        valor_derivada = float(entradagt.get())
        pendiente = derivadag(valor_derivada)
        funcion_definida_2 = pendiente * (dom2 - valor_derivada) + g(valor_derivada)
        punto_encuentro = (valor_derivada , g(valor_derivada))
        
        plt.plot(dom2,g(dom2),label="G(x) = "+funcion_simbolica2,color=entrada7.get())
        plt.plot(dom2 , funcion_definida_2,label="Tagente = "+str(derivada_simbolica2))
        plt.plot(valor_derivada,g(valor_derivada),'o',label="Punto de encuentro"+str(punto_encuentro))
        plt.plot(0,0,"o",color="yellow") # origen
        plt.xlabel('$x$',size=12)
        plt.ylabel('$y$',size=12)
        plt.legend()
        plt.grid(color="white")
        plt.show()

    def grafica_tangentef():
        funcion_simbolica = entrada1.get()
        derivada_simbolica = sym.diff(funcion_simbolica,x)
        f = sym.lambdify(x,funcion_simbolica,"numpy")
        derivadaf = sym.lambdify(x,derivada_simbolica,'numpy')
        
        dom = np.arange(float(entrada3.get()), float(entrada4.get()),0.1)
        
        valor_derivada = float(entradaft.get())
        pendiente = derivadaf(valor_derivada)
        funcion_definida_2 = pendiente * (dom - valor_derivada) + f(valor_derivada)
        punto_encuentro = (valor_derivada , f(valor_derivada))
        
        plt.plot(dom,f(dom),label="F(x) = "+funcion_simbolica,color=entrada5.get())
        plt.plot(dom , funcion_definida_2,label="Tagente = "+str(derivada_simbolica))
        plt.plot(valor_derivada,f(valor_derivada),'o',label="Punto de encuentro"+str(punto_encuentro))
        plt.plot(0,0,"o",color="yellow")
        plt.xlabel('$x$',size=12)
        plt.ylabel('$y$',size=12)
        plt.legend()
        plt.grid(color="white")
        plt.show()

    def grafica_areaf():
        funcion_simbolica = entrada1.get()
        f = sym.lambdify(x,funcion_simbolica,"numpy")
        
        dom = np.arange(float(entrada3.get()), float(entrada4.get()),0.1)
        
        integral_sin_definir = sym.integrate(funcion_simbolica,x)
        integral_definida = sym.integrate(funcion_simbolica,(x,float(entrada3.get()),float(entrada4.get())))
        integral_todo = 'integral = ' , integral_sin_definir , 'valor del area = ' ,  integral_definida
        
        plt.plot(dom,f(dom),label="Su funcion es = "+funcion_simbolica,color=entrada5.get())
        plt.fill_between(dom,f(dom),color="skyblue",label="area = "+str(integral_todo))
        plt.legend()
        plt.show()

    def grafica_areag():
        funcion_simbolica2 = entrada6.get()
        g = sym.lambdify(x,funcion_simbolica2,"numpy")
        
        dom2 = np.arange(float(entrada8.get()),float(entrada9.get()),0.1)
        
        integral_sin_definir = sym.integrate(funcion_simbolica2,x)
        integral_definida = sym.integrate(funcion_simbolica2,(x,float(entrada8.get()),float(entrada9.get())))
        integral_todo = 'integral = ' , integral_sin_definir , 'valor del area = ' ,  integral_definida
        
        plt.plot(dom2,g(dom2),label="Su funcion es = "+funcion_simbolica2,color=entrada7.get())
        plt.fill_between(dom2,g(dom2),color="skyblue",label="area = "+str(integral_todo)) # dibuja el relleno
        plt.legend()
        plt.show()

    botona = tk.Button(ventana1,text="Graficar Ambas Funciones",command=graficar_ambas,bg="white")
    botona.place(x=600,y=200,width=150,height=30)

    botonf = tk.Button(ventana1,text="Graficar F(x)",command=graficar_f,bg="white")
    botonf.place(x=600,y=30,width=100,height=30)

    botonft = tk.Button(ventana1,text="F(x) y Tangente",command=grafica_tangentef,bg="white")
    botonft.place(x=100,y=300,width=150,height=30)

    botonft = tk.Button(ventana1,text="F(x) y Area",command=grafica_areaf,bg="white")
    botonft.place(x=100,y=350,width=150,height=30)

    botong = tk.Button(ventana1,text="Graficar G(x)",command=graficar_g,bg="white")
    botong.place(x=600,y=120,width=100,height=30)

    botongt = tk.Button(ventana1,text="G(x) y Tangente",command=grafica_tangenteg,bg="white")
    botongt.place(x=300,y=300,width=150,height=30)

    botonft = tk.Button(ventana1,text="G(x) y Area",command=grafica_areag,bg="white")
    botonft.place(x=300,y=350,width=150,height=30)

    def borrar():
        entrada1.delete(0,tk.END)
        entrada3.delete(0,tk.END)
        entrada4.delete(0,tk.END)
        entrada5.delete(0,tk.END)
        entrada6.delete(0,tk.END)
        entrada7.delete(0,tk.END)
        entrada8.delete(0,tk.END)
        entrada9.delete(0,tk.END)
        entradagt.delete(0,tk.END)
        entradaft.delete(0,tk.END)
    botonm = tk.Button(ventana1,text="VACIAR TODO", command = borrar)
    botonm.place(x=550,y=350)

    def salir():
        ventana1.destroy()
    botondx = tk.Button(ventana1,text="VOLVER", command = salir)
    botondx.place(x=10,y=10)

    ventana1.mainloop()
#''' -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- '''
def animar():
    ventana2 = tk.Toplevel(interfaz)
    ventana2.title("Graficador animado")
    ventana2.resizable(0,0)
    
    traer_imagen4 = Image.open("dera.png")
    traer_imagen4 = traer_imagen4.resize((830,500)) 
    img = ImageTk.PhotoImage(traer_imagen4)
    lbl_img = tk.Label(ventana2,image=img)
    lbl_img.pack()

    letra_3_1 = tk.Label(ventana2 , text = "Ingrese su funcion = " , font = ("arial" , 12))
    letra_3_1.place(x = 75 , y = 75)
    entrada_3_1 = tk.Entry(ventana2)
    entrada_3_1.place(x = 225 , y = 75)

    letra_3_2 = tk.Label(ventana2 , text = "Ingrese el inicio de su funcion = " , font = ("arial" , 12))
    letra_3_2.place(x = 75 , y = 150)
    entrada_3_2 = tk.Entry(ventana2)
    entrada_3_2.place(x = 325 , y = 150)

    letra_3_3 = tk.Label(ventana2 , text = "Ingrese el final de su funcion = " , font = ("arial" , 12))
    letra_3_3.place(x = 75 , y = 225)
    entrada_3_3 = tk.Entry(ventana2)
    entrada_3_3.place(x = 325 , y = 225)

    letra_3_4 = tk.Label(ventana2 , text = "Donde quiere encontar \n la tangente de su funcion ? = \n (solo funciona para la tangente)" , font = ("arial" , 12))
    letra_3_4.place(x = 65 , y = 275)
    entrada_3_4 = tk.Entry(ventana2)
    entrada_3_4.place(x = 325 , y = 275)

    def grafica_animada():
        funcion_pregunta = entrada_3_1.get()
        simbolo = sym.simplify(funcion_pregunta)
        funcion_numpy = sym.lambdify(x , simbolo , "numpy")
        
        xmin = float(entrada_3_2.get())
        xmax = float(entrada_3_3.get())
        dominio = np.linspace(xmin , xmax)
        
        funcion_animada = funcion_numpy(dominio)
        min_funcion = hd.nsmallest(1,funcion_animada)
        max_funcion = hd.nlargest(1,funcion_animada)
        
        figura, funcion = plt.subplots()
        funcion.set_xlim(xmin , xmax)
        funcion.set_ylim(min_funcion[0] - 2, max_funcion[0] + 2)
        linea, = funcion.plot([], [],color="red", lw = 2 , label = "Funcion animada = " + str(simbolo))
        def init():
            linea.set_data([], [])
            return linea ,
        def funcion_normal(frame):
            dominio_2 = np.linspace(xmin, frame , 10000)
            y = funcion_numpy(dominio_2)
            linea.set_data(dominio_2, y)
            return linea ,
        funcion_animada = animation.FuncAnimation(figura, funcion_normal, frames = np.linspace(xmin, xmax, 25), init_func=init, blit=True )
        plt.plot(dominio,funcion_numpy(dominio),"-",color="yellow",lw=0.2)
        plt.plot(0,0,"o",color="yellow")
        plt.legend()
        plt.grid()
        plt.show()

    def grafica_tangente_animada():
        funcion_pregunta = entrada_3_1.get()
        simbolo = sym.simplify(funcion_pregunta)
        derivada_1 = sym.diff(simbolo , x)
        funcion_numpy = sym.lambdify(x , simbolo , "numpy")
        derivada_numpy = sym.lambdify(x , derivada_1 , "numpy")
        
        xmin = float(entrada_3_2.get())
        xmax = float(entrada_3_3.get())
        valor_derivada = float(entrada_3_4.get())
        pendiente = derivada_numpy(valor_derivada)
        dominio = np.linspace(xmin , xmax)
        
        funcion_animada = funcion_numpy(dominio)
        min_funcion = hd.nsmallest(1,funcion_animada)
        max_funcion = hd.nlargest(1,funcion_animada)
        
        figura, funcion = plt.subplots()
        funcion.set_xlim(xmin , xmax)
        funcion.set_ylim(min_funcion[0] - 2, max_funcion[0] + 2)
        linea_1, = funcion.plot([], [], lw = 2 , label =  "Funcion animada = " + str(simbolo))
        linea_2, = funcion.plot([], [],color="red", lw = 2 , label = "Derivada funcion" + str(derivada_1))
        punto, = funcion.plot([] ,[], 'o' , label = "punto de encuentro")
        def init():
            linea_1.set_data([], [])
            linea_2.set_data([], [])
            punto.set_data([], [])
            return linea_1 , linea_2 , punto
        def update(frame):
            dominio_2 = np.linspace(xmin, frame , 10000)
            y1 = pendiente * (dominio_2 - valor_derivada) + funcion_numpy(valor_derivada)
            y2 = funcion_numpy(dominio_2)
            punto_2 = funcion_numpy(valor_derivada)
            linea_1.set_data(dominio_2 , y1)
            linea_2.set_data(dominio_2 , y2)
            punto.set_data(valor_derivada, punto_2)
            return linea_1 , linea_2 , punto
        animacion = animation.FuncAnimation(figura, update, frames= np.linspace(xmin, xmax, 25), init_func=init, blit=True)
        plt.plot(dominio,funcion_numpy(dominio),"-",color="yellow",lw=0.2)
        plt.grid()
        plt.legend()
        plt.show()

    def area():
        funcion_pregunta = entrada_3_1.get()
        simbolo = sym.simplify(funcion_pregunta)
        funcion_numpy = sym.lambdify(x , simbolo , "numpy")
        
        xmin = float(entrada_3_2.get())
        xmax = float(entrada_3_3.get())
        dominio = np.linspace(xmin , xmax)
        
        funcion_animada = funcion_numpy(dominio)
        min_funcion = hd.nsmallest(1,funcion_animada)
        max_funcion = hd.nlargest(1,funcion_animada)
        figura, funcion = plt.subplots()
        funcion.set_xlim(xmin , xmax)
        funcion.set_ylim(min_funcion[0] - 2, max_funcion[0] + 2)
        linea, = funcion.plot([], [],color="red", lw = 2 , label = "Funcion animada = " + str(simbolo))
        def init():
            linea.set_data([], [])
            return linea ,
        def funcion_normal(frame):
            dominio_2 = np.linspace(xmin, frame , 10000)
            y = funcion_numpy(dominio_2)
            linea.set_data(dominio_2, y)
            return linea ,
        funcion_animada = animation.FuncAnimation(figura, funcion_normal, frames = np.linspace(xmin, xmax, 25), init_func=init, blit=True )
        plt.plot(dominio,funcion_numpy(dominio),"-",color="yellow",lw=0.2)
        plt.fill_between(dominio,funcion_numpy(dominio),color="skyblue" , label = "area" )
        plt.plot(0,0,"o",color="yellow")
        plt.legend()
        plt.grid()
        plt.show()

    boton_3_1 = tk.Button(ventana2 , text = "Graficar funcion " , command = grafica_animada , bg = "blue")
    boton_3_1.place(x = 500 , y = 20 , width = 250 , height = 75)

    boton_3_2 = tk.Button(ventana2 , text = "Graficar funcion y su tangente " , command = grafica_tangente_animada , bg = "blue")
    boton_3_2.place(x = 500 , y = 125 , width = 250 , height = 75)

    boton_3_3 = tk.Button(ventana2 , text = "Graficar funcion y su area " , command = area, bg = "blue")
    boton_3_3.place(x = 500 , y = 225 , width = 250 , height = 75)

    def borrar():
        entrada_3_1.delete(0,tk.END)
        entrada_3_2.delete(0,tk.END)
        entrada_3_3.delete(0,tk.END)
        entrada_3_4.delete(0,tk.END)
    botom = tk.Button(ventana2,text="VACIAR TODO", command = borrar)
    botom.place(x=100,y=10)

    def salir():
        ventana2.destroy()
    botondx = tk.Button(ventana2,text="VOLVER", command = salir)
    botondx.place(x=10,y=10)

    ventana2.mainloop()
#//////////////////////////////////////////////////////////////////
def curvas_paras():

    ventana7 = tk.Toplevel(interfaz)
    ventana7.title("Curvas parametricas")
    ventana7.resizable(0,0)

    traer_imagen5 = Image.open("awa.png")
    traer_imagen5 = traer_imagen5.resize((690,320)) 
    img = ImageTk.PhotoImage(traer_imagen5)
    lbl_img = tk.Label(ventana7,image=img)
    lbl_img.pack()

    letra_7_1 = tk.Label(ventana7 , text = "Ingrese su funcion f(x) = " , font = ("arial" , 12))
    letra_7_1.place(x = 100 , y = 100)
    entrada_7_1 = tk.Entry(ventana7)
    entrada_7_1.place(x = 300 , y = 100)
    letra_7_5 = tk.Label(ventana7 , text = "Ingrese su funcion g(x) = " , font = ("arial" , 12))
    letra_7_5.place(x = 100 , y = 150)
    entrada_7_5 = tk.Entry(ventana7)
    entrada_7_5.place(x = 300 , y = 150)
    letra_7_2 = tk.Label(ventana7 , text = "Ingrese el inicio de su funcion = " , font = ("arial" , 12))
    letra_7_2.place(x = 100 , y = 200)
    entrada_7_2 = tk.Entry(ventana7)
    entrada_7_2.place(x = 350 , y = 200)
    letra_7_3 = tk.Label(ventana7 , text = "Ingrese el final de su funcion = " , font = ("arial" , 12))
    letra_7_3.place(x = 100 , y = 250)
    entrada_7_3 = tk.Entry(ventana7)
    entrada_7_3.place(x = 350 , y = 250)
    
    def curvas_paras_animacion():

        funcion_pregunta_f_x = entrada_7_1.get()
        simbolo_f_x = sym.simplify(funcion_pregunta_f_x)
        funcion_numpy_f_x = sym.lambdify(x , simbolo_f_x , "numpy")
        funcion_pregunta_g_x = entrada_7_5.get()
        simbolo_g_x = sym.simplify(funcion_pregunta_g_x)
        funcion_numpy_g_x = sym.lambdify(x , simbolo_g_x , "numpy")
        xmin = float(entrada_7_2.get())
        xmax = float(entrada_7_3.get())
        dominio = np.linspace(xmin , xmax)
        funcion_animada_f_x = funcion_numpy_f_x(dominio)
        funcion_animada_g_x = funcion_numpy_g_x(dominio)
        min_funcion_f_x = hd.nsmallest(1,funcion_animada_f_x)
        max_funcion_f_x = hd.nlargest(1,funcion_animada_f_x)
        min_funcion_g_x = hd.nsmallest(1,funcion_animada_g_x)
        max_funcion_g_x = hd.nlargest(1,funcion_animada_g_x)


        figura, funcion = plt.subplots() 

        funcion.set_xlim(min_funcion_f_x[0] - 2  , max_funcion_f_x[0] + 2)
        funcion.set_ylim(min_funcion_g_x[0] - 2, max_funcion_g_x[0] + 2)

        linea, = funcion.plot([], [], lw = 2)

        def init():     #Incluir la linea en la funcion
            linea.set_data([], [])
            return linea ,

        def funcion_normal(frame):
            dominio_2 = np.linspace(-5, frame , 10000)
            x = funcion_numpy_f_x(dominio_2)
            y = funcion_numpy_g_x(dominio_2) 
            linea.set_data(x, y)
            return linea ,

        funcion_animada = animation.FuncAnimation(figura, funcion_normal, frames = np.linspace(xmin, xmax, 20), init_func=init, blit=True )

        plt.plot(funcion_numpy_f_x(dominio),funcion_numpy_g_x(dominio),"-",color="yellow",lw=0.2)
        plt.grid()
        plt.show()

    def borrar_2():
        entrada_7_1.delete(0,tk.END)
        entrada_7_2.delete(0,tk.END)
        entrada_7_3.delete(0,tk.END)
        entrada_7_5.delete(0,tk.END)
    botom_2 = tk.Button(ventana7,text="VACIAR TODO", command = borrar_2)
    botom_2.place(x=100,y=10)

    def salir_2():
        ventana7.destroy()
    botondx_2 = tk.Button(ventana7,text="VOLVER", command = salir_2)
    botondx_2.place(x=10,y=10)

    boton_7_1 = tk.Button(ventana7 , text = "Graficar funcion parametrica " , command = curvas_paras_animacion , bg = "blue")
    boton_7_1.place(x = 440 , y = 100 , width = 250 , height = 75)

    ventana7.mainloop()


#''' -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- '''
def pendulador():
    ventana3 = tk.Toplevel(interfaz)
    ventana3.title('Movimiento de un Pendulo')
    ventana3.resizable(0,0)

    traer_imagen3 = Image.open("backroom3.png")
    traer_imagen3 = traer_imagen3.resize((500,270)) 
    img = ImageTk.PhotoImage(traer_imagen3)
    lbl_img = tk.Label(ventana3,image=img)
    lbl_img.pack()

    etiqueta11 = tk.Label(ventana3, text="longitud del pendulo", fg="red")
    etiqueta11.place(x=70,y=20)
    entrada11 = tk.Entry(ventana3)
    entrada11.place(width=50,x=70,y=60)
    
    etiqueta22 = tk.Label(ventana3, text="gravedad", fg="red")
    etiqueta22.place(x=200,y=20)
    entrada22 = tk.Entry(ventana3)
    entrada22.place(width=50,x=200,y=60)
    
    etiqueta44 = tk.Label(ventana3, text="paso del tiempo", fg="red")
    etiqueta44.place(x=300,y=20)
    entrada44 = tk.Entry(ventana3)
    entrada44.place(width=50,x=300,y=60)
    
    etiqueta55 = tk.Label(ventana3, text="angulo inicial", fg="red")
    etiqueta55.place(x=400,y=20)
    entrada55 = tk.Entry(ventana3)
    entrada55.place(width=50,x=400,y=60)

    def movimiento(frame,longitud,gravedad,angulo_inicial,dt):
        t = frame * dt
        angulo = angulo_inicial * np.cos(np.sqrt(gravedad / longitud) * t)
        x = longitud * np.sin(angulo)
        y = -longitud * np.cos(angulo)
        pendulo.set_data([0, x], [0, y])
        return pendulo,
    fig, ax = plt.subplots()
    pendulo, = ax.plot([], [], 'o-', lw=3)
    def iniciar_animacion():
        longitud = float(entrada11.get())
        gravedad = float(entrada22.get())
        angulo_inicial = float(entrada55.get())
        dt = float(entrada44.get())
        ax.set_xlim(-1.5 * longitud, 1.5 * longitud)
        ax.set_ylim(-1.5 * longitud, 0.5 * longitud)
        animacion = FuncAnimation(fig, movimiento, frames=np.arange(0, 200, 1), interval=50, blit=True, fargs=(longitud, gravedad, angulo_inicial, dt))
        plt.show()

    botonpendulo = tk.Button(ventana3,text="pendulear", command =iniciar_animacion,bg="black",fg="white")
    botonpendulo.place(x=250,y=180,width=100,height=50)
    def borrar():
        entrada11.delete(0,tk.END)
        entrada22.delete(0,tk.END)
        entrada44.delete(0,tk.END)
        entrada55.delete(0,tk.END)
    boton333 = tk.Button(ventana3,text="VACIAR TODO", command = borrar)
    boton333.place(x=100,y=200)
    def salir():
        ventana3.destroy()
    botondx = tk.Button(ventana3,text="VOLVER", command = salir)
    botondx.place(x=10,y=10)

    ventana3.mainloop()

#''' -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- '''

def AbrirPaginaOnline():
    import webbrowser
    webbrowser.open("https://sites.google.com/correounivalle.edu.co/graf2d")
BarraMenu = tk.Menu(interfaz)
interfaz.config(menu=BarraMenu)
Opciones = tk.Menu(BarraMenu, tearoff=0)
BarraMenu.add_cascade(label="Menu", menu=Opciones)
Opciones.add_command(label="Pagina Web",command=AbrirPaginaOnline)
Opciones.add_separator()
Opciones.add_command(label="salir",command=interfaz.quit)

def salir():
        interfaz.destroy()

#''' -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- '''
etiquetaB1 = tk.Label(interfaz,text="GRAFICADOR",bg="purple",font=("arial",14),fg="black")
etiquetaB1.place(x=50,y=50)
botonB1 = tk.Button(interfaz,text="Ir",command=graficar,bg="black",fg="white")
botonB1.place(x=90,y=100,width=50,height=50)

etiquetaB2 = tk.Label(interfaz,text="ANIMADOR",bg="purple",font=("arial",14),fg="black")
etiquetaB2.place(x=350,y=50)
botonB2 = tk.Button(interfaz,text="Ir",command=animar,bg="black",fg="white")
botonB2.place(x=380,y= 100,width=50,height=50)

etiquetaB3 = tk.Label(interfaz,text="PENDULO",bg="purple",font=("arial",14),fg="black")
etiquetaB3.place(x=350,y=200)
botonB3 = tk.Button(interfaz,text="Ir",command=pendulador,bg="black",fg="white")
botonB3.place(x=380,y= 250,width=50,height=50)

botonB3 = tk.Button(interfaz,text="Salir",command=salir,bg="black",fg="white")
botonB3.place(x=50,y=250,width=150,height=50)

etiquetaB2 = tk.Label(interfaz,text="Curvas parametricas",bg="purple",font=("arial",14),fg="black")
etiquetaB2.place(x=200,y=350)
botonB4 = tk.Button(interfaz ,text="Curvas parametricas", command = curvas_paras, bg = "black", fg = "white")
botonB4.place(x=210,y=400,width=150,height=50)



interfaz.mainloop()
