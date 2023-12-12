from tkinter import *
root=Tk()
root.title("Mi calculadora")

def sumar():
    resultado.set(int(var1.get())+int(var2.get()))

def restar():
    resultado.set(int(var1.get())-int(var2.get()))

def multiplicar():
    resultado.set(int(var1.get()) * int(var2.get())) 

def dividir():
    resultado.set(int(var1.get())/ int(var2.get()))

frame = Frame(root)
frame.pack()

var1= StringVar()
var2= StringVar()
resultado= StringVar()

entrada1 = Entry(frame)
entrada1.pack()
entrada1.config(bd=10, font=("Curier, 20"), textvariable=var1)

entrada2 = Entry(frame)
entrada2.pack()
entrada2.config(bd=10, font=("Curier, 20"), textvariable=var2)

entrada3 = Entry(frame)
entrada3.pack()
entrada3.config(bd=10, font=("Curier, 20"), state="disabled", textvariable=resultado)

boton1 = Button(frame)
boton1.pack()
boton1.config(bg="Blue", bd=10, font=("Curier, 20"), text="Suma", command=sumar)

boton2 = Button(frame)
boton2.pack()
boton2.config(bg="Red", bd=10, font=("Curier, 20"), text="Resta", command=restar)

boton3 = Button(frame)
boton3.pack()
boton3.config(bg="Green", bd=10, font=("Curier, 20"), text="Multuplicar", command=multiplicar)

boton4 = Button(frame)
boton4.pack()
boton4.config(bg="Yellow", bd=10, font=("Curier, 20"), text="Dividir", command=dividir)

root.mainloop()