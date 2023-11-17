# tabla de multiplicar con funciones
##FOR

inicio_r = int(input("Ingresa el inicio del rango: "))
final_r = int(input("Ingresa el final del rango: "))
inicio_t = int(input("Ingresa e inicio de la tabala"))
final_t = int(input("Ingresa el final de la tabla"))

for i in range (inicio_r,final_r + 1):
    print(f"La tabla del {i}")
    for j in range (inicio_t,final_t + 1):
        print(f"{i} x {j} = {i*j}")
