# lopez ricardo NC = 0085
# ejemplos de variables
print("variables")

print("ejemplo 1 Creación de variables")
x = 5
y = "John"
print(x)
print(y)
print("ejemplo 2 ")

x = 4       # x is of type int
x = "Sally" # x is now of type str
print(x)

print("ejemplo 3 Fundición")
x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0
print("-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-")
print("variables multiples")
print("ejemplo 1 Creación de variables")
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

print("ejemplo 2 Un valor para múltiples variables")
x = y = z = "Orange"
print(x)
print(y)
print(z)

print("ejemplo 3 Fundición")
x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0
print("-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-")
print("tipos de datos integrados")
print("ejemplo 1")
cantidad = 3           
precio_unidad = 4.50  
total_pagar = cantidad * precio_unidad
print("El total a pagar es:")
print(total_pagar) 

print("ejemplo 2")
# Variables de texto
saludo = "Hola, "
nombre = "Carlos"
# Unir textos (Concatenación)
mensaje_bienvenida = saludo + nombre
print(mensaje_bienvenida)  # Resultado: Hola, Carlos
# Importancia del tipo: Convertir número a texto para poder unirlo
edad = 28
mensaje_edad = nombre + " tiene " + str(edad) + " años."
print(mensaje_edad)  # Resultado: Carlos tiene 28 años.
print("ejemplo 3")
# Variable numérica
edad_usuario = 20
# El operador ">=" compara los datos y devuelve un Booleano (True o False)
es_mayor_de_edad = edad_usuario >= 18  # Guarda: True
# Función: El flujo del código cambia según el tipo booleano
if es_mayor_de_edad:
    print("Acceso concedido: Eres mayor de edad.")
else:
    print("Acceso denegado: Eres menor de edad.")
print("-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-")
print("operadores aritmeticos")
print("ejemplo 1")
# Sumar y restar números directamente
resultado = 10 + 5 - 2
print(resultado)  # Resultado: 13
print("ejemplo 2")
# Multiplicar y dividir en una sola línea
resultado = 4 * 3 / 2
print(resultado)  # Resultado: 6.0
print("ejemplo 3")
# Elevar un número (potencia)
potencia = 3 ** 2  # 3 elevado al cuadrado (3 * 3)
print(potencia)   # Resultado: 9
# Obtener el residuo de una división
residuo = 10 % 3   # 10 dividido entre 3 es 3, y sobra 1
print(residuo)    # Resultado: 1
print("-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-")
print("operadores de comparacion")
print("ejemplo 1")
print(5>3)

print("ejemplo 2")
print(10<2)

print("ejemplo 3")
print(7==7)
print("-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-")
print("ejemplo 1")
x = 5

print(x > 0 and x < 10)
print("ejemplo 2")
x = 5

print(x < 5 or x > 10)
print("ejemplo 3")
x = 5

print(not(x > 3 and x < 10))

print("programa hecho por Lopez Ricardo NC = 0085")