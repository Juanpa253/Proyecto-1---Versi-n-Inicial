#Menu
print("Bienvenido a Gasolineras Jaguar")
print("1. Gestión de Inventario")
print("2. Venta de Combustible")
print("3. Gestion de Turnos")
print("4. Reporte de Rentabilidad")
print("5. Salida")
MenuNumero = int(input("ingrese la opcion deseada: "))

#Gestión de Inventario
if MenuNumero == 1:
    #Función por implementar, se mostrará el nivel de los depósitos.
    RellenarDepositos = input("Desea agregar gasolina a los depósitos ? Sí/No ")
    if RellenarDepositos == "Sí":
        #La función para rellenar depósitos va aquí


#Venta de Combustible
elif MenuNumero == 2:
    #Función por implementar, se mostrará el nivel de los depósitos.
    print("1. Regular")
    print("2. Super")
    print("3. Diesel")
    TipodeCombustibleVenta = int(input("Elija el número del tipo de combustible por vender: "))
    if TipodeCombustibleVenta == 1:
        #Vender Regular
    elif TipodeCombustibleVenta == 2:
        #Vender Super
    elif TipodeCombustibleVenta == 3:
        #Vender Diesel


#Gestion de Turnos
elif  MenuNumero == 3:
    #Función por implementar, se mostrará la cantidad de empleados por jornada.
    AgregarOperadores = int(input("Cuántos operadores desea agregar ?"))
    #Asignar operadores a cada jornada.
    EliminarOperadores = int(input("Cuántos operadores desea eliminar ?"))
    #Desasignar operadores de cada jornada.
    print(" Salario Total Jornada Diurna: ")
    print(" Salario Total Jornada Vespertina: ")
    print(" Salario Total Jornada Nocturna: ")

#Reporte de Rentabilidad
elif MenuNumero == 4:
    #Función por implementar, gastos totales.

#Salida
elif MenuNumero == 5:
    print("El programa ha terminado, gracias por preferirnos.")

else:
    print("Ingrese una opción valida")