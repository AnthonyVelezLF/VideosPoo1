from helpers import Helper
import os

#Repite el listado
helper = Helper()
lista = ["1) Hola Mundo","2) Variables","3) Conversiones","4) Numeros Operaciones","5) Concatenación","6) Cadenas","7)","8)","9)","10)","11)","12)","13)","14)","15)","16)","17)","18)","19)","20)","21)","22)","23)","24)","25)","26)","27)","28)","29)","30)","31)","32)","33)","34) Salir"]
opcion=""

#EJERCICIOS PYTHON
while opcion != "20":
  os.system("cls")
  opcion = helper.menu(lista,"*"*20+" EJERCICIOS PYTHON "+"*"*20)

  #EJERCICIOS
  if opcion == "1":
    print("Hola Mundo")
    input("Presione una tecla para continuar...")

  elif opcion == "2":
    nombre = "Anthony"
    print(nombre)
    edad = 25
    print(edad)
    edad = True
    print(edad)
    sueldo = 205.10
    print(sueldo)
    input("Presione una tecla para continuar...")

  elif opcion == "3":
    numero1 = "35"
    numero2 = "18"
    print(numero1 + numero2)
    num1 = int(numero1)
    num2 = int(numero2)
    print(num1 + num2)
    sueldo = 1200.43
    sueldoEntero = int(sueldo)
    print(sueldoEntero)
    valor = "4500.89"
    valorDecimal = float(valor)
    print(valorDecimal * 3 )
    edad = 100
    print(len(str(edad)))
    input("Presione una tecla para continuar...")

  elif opcion == "4":
    entero = 23
    decimal = 31.78
    entero = 12 + 5j
    # booleano = True
    '''
    print(entero) 
    print(decimal)
    print(complejo)
    print(booleano)
    '''
    num1 = 20
    num2 = 4
    print("Suma:", (num1 + num2))
    print("Resta:", (num1 - num2))
    print("Multiplicación:", (num1 * num2))
    print("División:", (num1 / num2))
    print("División Exacta:", (num1 // num2))
    print("Potencia:", (num1 ** num2))
    input("Presione una tecla para continuar...")

  elif opcion == "5":
    texto1 = "Hola"
    texto2 = "Mundo"
    textoFinal = texto1 + " " + texto2
    print(textoFinal)
    print("El saludo es: %s %s" % (texto1, texto2))
    saludoFinal = "Saludo: {0} {1}".format(texto1,texto2)
    print(saludoFinal)
    saludoFinal2 = "Saludo: {y} {x}".format(x=texto2, y=texto1)
    print(saludoFinal2)
    input("Presione una tecla para continuar...")

  elif opcion == "2":
    print()
    input("Presione una tecla para continuar...")

  elif opcion == "2":
    print()
    input("Presione una tecla para continuar...")

  elif opcion == "2":
    print()
    input("Presione una tecla para continuar...")

  elif opcion == "2":
    print()
    input("Presione una tecla para continuar...")

  elif opcion == "2":
    print()
    input("Presione una tecla para continuar...")

  elif opcion == "2":
    print()
    input("Presione una tecla para continuar...")

  elif opcion == "2":
    print()
    input("Presione una tecla para continuar...")

  elif opcion == "2":
    print()
    input("Presione una tecla para continuar...")

  elif opcion == "2":
    print()
    input("Presione una tecla para continuar...")

  elif opcion == "2":
    print()
    input("Presione una tecla para continuar...")

  elif opcion == "2":
    print()
    input("Presione una tecla para continuar...")

  elif opcion == "2":
    print()
    input("Presione una tecla para continuar...")
