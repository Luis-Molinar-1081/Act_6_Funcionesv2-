print("Mas sobre funciones")
# Aqui se escriben las funciones 
def suma_ab(a,b):
    s=a+b 

    return s

def resta_ab(a,b):
    r=a-b
    
    return r

def mul_ab(a,b):
    m=a*b

    return m

def div_ab(a,b):
    d=a/b

    return d

#Llamadas a funciones 
print("Calculando suma")
n1=int(input("Ingresa el Primer numero"))
n2=int(input("Ingresa el Segundo numero"))
suma=suma_ab(n1,n2)
print(f"La suma de {n1} + {n2} es {suma}")

print("Calculando la resta")
n3=int(input("Ingresa el Primer numero"))
n4=int(input("Ingresa el Segundo numero"))
resta=resta_ab(n3,n4)
print(f"La resta de {n3} - {n4} es {resta}")

print("Calculando Multiplicacion")
n5=int(input("Ingresa el Primer numero"))
n6=int(input("Ingresa el Segundo numero"))
mul=mul_ab(n5,n6)
print(f"La Multiplicacion de {n5} * {n6} es {mul}")

print("Calculando la Divicion")
n7=int(input("Ingresa el Primer numero"))
n8=int(input("Ingresa el Segundo numero"))
div=div_ab(n7,n8)
print(f"La divicion de {n7} / {n8} es {resta}")


