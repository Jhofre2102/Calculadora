from flask import Flask, request

app=Flask(__name__)

def suma(a,b):
    return a+b

@app.route("/")
def home ():
    return '''
        Aplicación web con flask-afsr
        <h1>Calculadora</h1>
        <h3>Opciones Disponibles</h3>
        <ul>
            <li><a href="/Suma">Suma</a></li>
            <li>Resta</li>
            <li>Multiplicacion</li>
            <li>Division</li>
        
        
        
        </ul>


'''
@app.route("/suma")
def ruta_suma():
    print(request.args)
    num1 = request.arg.get("num1",type=float)
    num2 = request.arg.get("num2", type=float)
    if num1 is None or num2 is None:
        return "Faltan parametros"
    return f"<p>La suma de {num1} + {num2} es {suma(num1,num2)}</p>"

if __name__ == "__main__":
    app.run(debug=True)

