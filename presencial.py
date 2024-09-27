import ast
from flask import Flask, request, jsonify

app = Flask(__name__)
#Primer cambio para ver que pasa con Jenkins
#Segunda prueba con 

#Otra prueba
# Ejercicio 1: Palíndromo
@app.route('/palindromo', methods=['GET', 'POST'])
def palindromo_endpoint():
    if request.method == 'POST':
        data = request.get_json()
        cadena = data['cadena']
    else:
        cadena = request.args.get('cadena', '')

    resultado = palindromo(cadena)
    return jsonify({"palindromo": resultado})

def palindromo(cadena):
    return cadena == cadena[::-1]

# Ejercicio 2: Invertir cadena
@app.route('/invertir', methods=['GET', 'POST'])
def invertir_endpoint():
    if request.method == 'POST':
        data = request.get_json()
        cadena = data['cadena']
    else:
        cadena = request.args.get('cadena', '')

    resultado = invertir(cadena)
    return jsonify({"invertida": resultado})

def invertir(cadena):
    invertida = ''
    for i in range(len(cadena)-1, -1, -1):
        invertida += cadena[i]
    return invertida

# Ejercicio 3: Coincidencia de palabra
@app.route('/coincidencia', methods=['GET', 'POST'])
def coincidencia_endpoint():
    if request.method == 'POST':
        data = request.get_json()
        palabra = data['palabra']
        frase = data['frase']
    else:
        palabra = request.args.get('palabra', '')
        frase = request.args.get('frase', '')

    resultado = coincidencia(palabra, frase)
    return jsonify({"coincidencias": resultado})

def coincidencia(palabra, frase):
    return frase.split().count(palabra)

# Ejercicio 4: Máximos en un arreglo
@app.route('/maximin', methods=['GET', 'POST'])
def maximin_endpoint():
    if request.method == 'POST':
        data = request.get_json()
        arreglo = data['arreglo']
    else:
        arreglo = request.args.getlist('arreglo', type=int)

    max_valor, posiciones = maximin(arreglo)
    return jsonify({"maximo": max_valor, "posiciones": posiciones})

def maximin(arreglo):
    max_valor = max(arreglo)
    posiciones = [i for i, valor in enumerate(arreglo) if valor == max_valor]
    return max_valor, posiciones

# Ejercicio 5: Búsqueda aproximada
@app.route('/posearch', methods=['GET', 'POST'])
def posearch_endpoint():
    if request.method == 'POST':
        data = request.get_json()
        arreglo = data['arreglo']
        valor = data['valor']
    else:
        arreglo = request.args.getlist('arreglo', type=int)
        valor = request.args.get('valor', type=int)

    posicion = posearch(arreglo, valor)
    return jsonify({"posicion": posicion})

def posearch(arreglo, valor):
    mas_cercano = min(arreglo, key=lambda x: abs(x - valor))
    return arreglo.index(mas_cercano)

# Ejercicio 6: Histograma
@app.route('/histograma', methods=['GET', 'POST'])
def histograma_endpoint():
    if request.method == 'POST':
        data = request.get_json()
        arreglo = data['arreglo']
    else:
        arreglo = request.args.getlist('arreglo', type=int)

    resultado = histograma(arreglo)
    return jsonify({"histograma": resultado})

def histograma(arreglo):
    return [f"{num}: {'*' * num}" for num in arreglo]

# Ejercicio 7: Intercalar arreglos
@app.route('/intercala', methods=['GET', 'POST'])
def intercala_endpoint():
    if request.method == 'POST':
        data = request.get_json()
        arreglo1 = data['arreglo1']
        arreglo2 = data['arreglo2']
    else:
        arreglo1 = request.args.getlist('arreglo1', type=int)
        arreglo2 = request.args.getlist('arreglo2', type=int)

    resultado = intercala(arreglo1, arreglo2)
    return jsonify({"resultado": resultado})

def intercala(arreglo1, arreglo2):
    return sorted(arreglo1 + arreglo2)

# Ejercicio 8: Serie de Fibonacci
@app.route('/fibo', methods=['GET', 'POST'])
def fibo_endpoint():
    if request.method == 'POST':
        data = request.get_json()
        n = data['n']
    else:
        n = request.args.get('n', type=int)

    resultado = fibo(n)
    return jsonify({"fibonacci": resultado})

def fibo(n):
    serie = [0, 1]
    while len(serie) < n:
        serie.append(serie[-1] + serie[-2])
    return serie[:n]

# Ejercicio 9: Verificar matriz cuadrada
@app.route('/esCuadrada', methods=['GET', 'POST'])
def es_cuadrada_endpoint():
    if request.method == 'POST':
        data = request.get_json()
        matriz = data['matriz']
    else:
        matriz = request.args.getlist('matriz')

    resultado = esCuadrada(matriz)
    return jsonify({"esCuadrada": resultado})

def esCuadrada(matriz):
    return len(matriz) == len(matriz[0])

# Ejercicio 10: Calcular traza de matriz
@app.route('/traza', methods=['GET', 'POST'])
def traza_endpoint():
    if request.method == 'POST':
        data = request.get_json()
        matriz = data['matriz']
        izquierda_a_derecha = data.get('izquierda_a_derecha', True)
    else:
        # Uso  ast.literal_eval para convertir la cadena en una lista
        matriz = ast.literal_eval(request.args.get('matriz', '[]'))
        izquierda_a_derecha = request.args.get('izquierda_a_derecha', 'true').lower() == 'true'

    resultado = traza(matriz, izquierda_a_derecha)
    return jsonify({"traza": resultado})

def traza(matriz, izquierda_a_derecha=True):
    n = len(matriz)
    if izquierda_a_derecha:
        return sum(matriz[i][i] for i in range(n))
    else:
        return sum(matriz[i][n-1-i] for i in range(n))

# Ejercicio 11: Suma del borde de una matriz
@app.route('/sumarBorde', methods=['GET', 'POST'])
def sumar_borde_endpoint():
    if request.method == 'POST':
        data = request.get_json()
        matriz = data['matriz']
    else:
        matriz = ast.literal_eval(request.args.get('matriz', '[]'))

    resultado = sumarBorde(matriz)
    return jsonify({"sumaBorde": resultado})

def sumarBorde(matriz):
    filas = len(matriz)
    columnas = len(matriz[0])
    suma = sum(matriz[0]) + sum(matriz[-1])  # Primera y última fila
    suma += sum(matriz[i][0] + matriz[i][-1] for i in range(1, filas-1))  # Bordes verticales
    return suma

# Ejercicio 12: Suma de esquinas

#Otra prueba con jenkins

#PRobando de nuevo 
@app.route('/sumaEsquinas', methods=['GET', 'POST'])
def suma_esquinas_endpoint():
    if request.method == 'POST':
        data = request.get_json()
        matriz = data['matriz']
    else:
        matriz = ast.literal_eval(request.args.get('matriz', '[]'))

    resultado = sumaEsquinas(matriz)
    return jsonify({"sumaEsquinas": resultado})

def sumaEsquinas(matriz):
    filas = len(matriz)
    columnas = len(matriz[0])
    return matriz[0][0] + matriz[0][-1] + matriz[-1][0] + matriz[-1][-1]

# Ejercicio 13: Punto de silla
@app.route('/silla', methods=['GET', 'POST'])
def silla_endpoint():
    if request.method == 'POST':
        data = request.get_json()
        matriz = data['matriz']
    else:
        matriz = request.args.getlist('matriz')

    resultado = silla(matriz)
    return jsonify({"puntosDeSilla": resultado})

def silla(matriz):
    puntos_de_silla = []
    for i, fila in enumerate(matriz):
        min_fila = min(fila)
        columna = fila.index(min_fila)
        if all(min_fila >= matriz[k][columna] for k in range(len(matriz))):
            puntos_de_silla.append((i, columna))
    return puntos_de_silla

# Ejercicio 14: Traspuesta de una matriz
@app.route('/traspuesta', methods=['GET', 'POST'])
def traspuesta_endpoint():
    if request.method == 'POST':
        data = request.get_json()
        matriz = data['matriz']
    else:
        # Convierto la cadena en una lista usando ast.literal_eval
        matriz = ast.literal_eval(request.args.get('matriz', '[]'))

    resultado = traspuesta(matriz)
    return jsonify({"traspuesta": resultado})

def traspuesta(matriz):
    # REalizo la traspuesta intercambiando filas por columnas
    return [[fila[i] for fila in matriz] for i in range(len(matriz[0]))]

# Ejercicio 15: Suma sobre la diagonal principal
@app.route('/dpSuma', methods=['GET', 'POST'])
def dp_suma_endpoint():
    if request.method == 'POST':
        data = request.get_json()
        matriz = data['matriz']
    else:
        # Convierto la cadena de la matriz a una lista usando ast.literal_eval, igual que los otros arriba
        matriz = ast.literal_eval(request.args.get('matriz', '[]'))

    resultado = dpSuma(matriz)
    return jsonify({"sumaDiagonal": resultado})

def dpSuma(matriz):
    # Sumo los elementos que están por encima de la diagonal principal
    suma = 0
    for i in range(len(matriz)):
        for j in range(i+1, len(matriz[i])):
            suma += matriz[i][j]
    return suma

# Ejercicio 16: Contar subcadena
@app.route('/contarSubcadena', methods=['GET', 'POST'])
def contar_subcadena_endpoint():
    if request.method == 'POST':
        data = request.get_json()
        cadena = data['cadena']
        subcadena = data['subcadena']
    else:
        cadena = request.args.get('cadena', '')
        subcadena = request.args.get('subcadena', '')

    resultado = contarSubcadena(cadena, subcadena)
    return jsonify({"ocurrencias": resultado})

def contarSubcadena(cadena, subcadena):
    return cadena.count(subcadena)

# Ejercicio 17: Número primo
@app.route('/esPrimo', methods=['GET', 'POST'])
def es_primo_endpoint():
    if request.method == 'POST':
        data = request.get_json()
        numero = data['numero']
    else:
        numero = request.args.get('numero', type=int)

    resultado = esPrimo(numero)
    return jsonify({"esPrimo": resultado})

def esPrimo(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Ejercicio 18: Factorial
@app.route('/factorial', methods=['GET', 'POST'])
def factorial_endpoint():
    if request.method == 'POST':
        data = request.get_json()
        numero = data['numero']
    else:
        numero = request.args.get('numero', type=int)

    resultado = factorial(numero)
    return jsonify({"factorial": resultado})

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

# Ejercicio 19: Ordenar por longitud de cadena
@app.route('/ordenarPorLongitud', methods=['GET', 'POST'])
def ordenar_por_longitud_endpoint():
    if request.method == 'POST':
        data = request.get_json()
        cadenas = data['cadenas']
    else:
        cadenas = request.args.getlist('cadenas')

    # Ordenar las cadenas de menor a mayor longitud
    resultado = ordenarPorLongitud(cadenas)
    return jsonify({"ordenado": resultado})

def ordenarPorLongitud(cadenas):
    return sorted (cadenas, key=len)  # Ordenar por la longitud de las cadenas

# Ejercicio 20: Calcular media y desviación estándar
import math

@app.route('/estadistica', methods=['GET', 'POST'])
def estadistica_endpoint():
    if request.method == 'POST':
        data = request.get_json()
        arreglo = data['arreglo']
    else:
        arreglo = request.args.getlist('arreglo', type=float)

    media, desviacion_estandar = estadistica(arreglo)
    return jsonify({"media": media, "desviacionEstandar": desviacion_estandar})

def estadistica(arreglo):
    media = sum(arreglo) / len(arreglo)
    varianza = sum((x - media) ** 2 for x in arreglo) / len(arreglo)
    desviacion_estandar = math.sqrt(varianza)
    return media, desviacion_estandar

if __name__ == '__main__':
    app.run(debug=True)
#Larry Tesler Idols (Grupo 3)