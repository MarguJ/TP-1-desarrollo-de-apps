#Llegar a la esquina
#(Semaforo en verde (peaton)
#Autos frenados/bicicletas
#Obstaculos)
#Si todo () es falso entonces cruzar

semaforo = input("¿De que color es el semaforo?").lower()
vehiculosFrenados = bool(input("¿Frenaron los vehiculos? (0=No 1=Si)"))
obstaculos = bool(input("¿Hay obstaculos en el camino?(0=No 1=Si)"))


if semaforo == "verde" and vehiculosFrenados:
    if not obstaculos:
        print("Es seguro para cruzar *Cruza🚶*")
    else:
        print("Cruzá pero ojo con los obstaculos *Cruza con cuidado🚶*")
else:
    print("No es seguro para cruzar, esperar a que lo sea *Se queda esperando y farmeando aura god +2000 aura⏳*")

