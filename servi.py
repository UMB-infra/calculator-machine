from machine import Pin, I2C
import ssd1306
import time

i2c = I2C(-1, Pin(22), Pin(21))
oled = ssd1306.SSD1306_I2C(128, 64, i2c)

def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    if b == 0:
        return "Error: No se puede dividir por cero"
    else:
        return a / b

def seleccion(opcion):
    resultado = None
    opcion = str(opcion)
    oled.fill(0)

    if opcion in ["0", "1", "2", "3"]:
        num1 = float(input("Ingresa el primer número: "))
        num2 = float(input("Ingresa el segundo número: "))

        if opcion == "0":
            resultado = suma(num1, num2)
        elif opcion == "1":
            resultado = resta(num1, num2)
        elif opcion == "2":
            resultado = multiplicacion(num1, num2)
        elif opcion == "3":
            resultado = division(num1, num2)

    else:
        print("Opción no válida. Elige una opción válida.")
        return(resultado)
    
    return(str(resultado))
