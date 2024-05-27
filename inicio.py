from flask import Flask, render_template, request, redirect, url_for, flash
import pymysql

app = Flask(__name__)

@app.route('/')
def home():
    # return render_template("HOla mundo")
    return render_template("menu.html")

@app.route('/Triangulos')
def Triangulos():
    return render_template("AreaT.html")

@app.route('/Calificaciones')
def Calificaciones():
    return render_template("Califs.html")

@app.route('/Grados')
def Grados():
    return render_template("Grados.html")

@app.route('/Multiplicar')
def Multiplicar():
    return render_template("TablaMult.html")

@app.route('/Viaje')
def Viaje():
    return render_template("Viaje.html")

@app.route('/Operaciones', methods=['POST'])
def Operaciones():
    if request.method != 'POST':
        return None
    
    h = (request.form['hidden'])#este nos va a servir de id
    
    if h=="Triangulo":
        base = float(request.form['base'])
        altura = float(request.form['altura'])
        ar=base*altura/2
        return render_template("AreaT.html",res=ar,base=base,altura=altura)
    
    elif h=="Calificaciones":
#         Solicitar un número de 0 a 10 e imprimir un mensaje de acuerdo a lo siguiente:

# si la calificación es mayor o igual a o y menor o igual a 5 mandar mensaje con
# "REPROBADO"
# con calificación =6 mensaje de "SUFICIENTE"
# calificación =7 mensaje de "REGULAR"
# calificación = 8  ó 9 mensaje de "NOTABLE"
# calificación = 10 mensaje de "EXCELENTE"
        
# * si el número introducido difiere de estos rangos, mandar mensaje de:
# "SOLO INTRODUCIR NÚMEROS ENTEROS DE 0 a 10"
        calif=float(request.form['calificacion'])

        mensjs=['REPROBADO','SUFICIENTE','REGULAR','NOTABLE','EXCELENTE']
        cursor=0

        cursor=calif-5
        if(calif==9 or calif==10):
            cursor-=1
        elif(calif<6):
            cursor=0
         
        return render_template("Califs.html",base=calif,res=mensjs[int(cursor)])
    
    elif h=="Grados":
#         Convertir de grados Fahrenheit a Centígrados, utilizando la siguiente
# formula:  C= 5/9 (F – 32). Mostrar los grados Centígrados  y
# los  Fahrenheit  obtenidos.
        faren=float(request.form['grados'])

        centi=(5/9)*(faren-32)
        return render_template("Grados.html",res=centi,farenheit=faren)
    
    elif h=="Multiplicar":
#         Solicitar un número entero positivo del 2 al 10 y mostrar su tabla de
# multiplicación correspondiente
        base=int(request.form['numero'])
        tabla=""
        for c in range(0,11):
            tabla+=f"{base} X {c} = {base*c}"
            if(c!=10):
                tabla+="\n"

        return render_template("TablaMult.html",res=tabla,base=base)
    
    elif h=="Viaje":
#         El director de una escuela está organizando
# un viaje de estudios y requiere determinar cuánto debe cobrar a cada alumno y
# cuanto debe pagar a la compañía de viajes por el servicio. La forma de cobrar
# es la siguiente: de 50 a 99 alumnos el costo es de $70, de 30 a 49 es de $95 y
# si son menos de 30 alumnos, el costo de la renta del autobús es de $3500 sin
# importar el número de alumnos. Se debe obtener el pago a la compañía de
# autobuses y lo que debe pagar cada alumno por el viaje.
        numAlumnos=int(request.form['alumnos'])
        if(numAlumnos>=50):
            costo=70
        elif(numAlumnos>=30):
            costo=95
        else:
            costo=3500/numAlumnos

        total=costo*numAlumnos

        return render_template("Viaje.html",alumnos=numAlumnos,ppa=costo, res=total)
    
if __name__ == "__main__":
    app.run(debug=True)
