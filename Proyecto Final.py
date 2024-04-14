
class Deposito:
    def __init__(self,Nombre,CapacidadMax,Almacenado,PrecioAlmacenamiento):
        self.Nombre = Nombre
        self.CapacidadMax = CapacidadMax
        self.Almacenado = Almacenado
        self.PrecioAlmacenamiento = PrecioAlmacenamiento
    
    def MostrarCapacidad (self):
        print("La cantidad almacenada en el deposito de combustible", self.Nombre, "actualmente es:", self.Almacenado,"Galones")

    def AgregarCombustible (self):
        CantidadGalones = int(input("Cuántos galones desea agregar? "))
        if CantidadGalones >= 0:
            if self.Almacenado + CantidadGalones <= self.CapacidadMax:
                print("Se agregaron", CantidadGalones, "galones de combustible al deposito", self.Nombre)
                self.Almacenado = self.Almacenado + CantidadGalones
                self.MostrarCapacidad()
            else:
                print("La cantidad por agregar supera el límite del deposito")
        else:
            print("La cantidad ingresada debe ser positiva")

#Crear depósitos
DepositoRegular = Deposito("Regular", 80, 40, 7) 
DepositoSuper = Deposito("Super", 80,40, 8) 
DepositoDiesel = Deposito("Diesel", 80, 40, 6) 

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
    DepositoRegular.MostrarCapacidad()
    DepositoSuper.MostrarCapacidad()
    DepositoDiesel.MostrarCapacidad()
    #Agregar Gasolina
    RellenarDepositos = input("Desea agregar gasolina a los depósitos ? Si/No ").lower()
    if RellenarDepositos == "si":
        DepositoRegular.AgregarCombustible()
        DepositoSuper.AgregarCombustible()
        DepositoDiesel.AgregarCombustible()

#Venta de Combustible
elif MenuNumero == 2:
    #Función por implementar, se mostrará el nivel de los depósitos.
    print("1. Regular")
    print("2. Super")
    print("3. Diesel")
    TipodeCombustibleVenta = int(input("Elija el número del tipo de combustible por vender: "))
    if TipodeCombustibleVenta == 1:
        pausa = 0
        #Vender Regular
    elif TipodeCombustibleVenta == 2:
        pausa = 0
        #Vender Super
    elif TipodeCombustibleVenta == 3:
        #Vender Diesel
        pausa = 0


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
    pausa = 0

#Salida
elif MenuNumero == 5:
    print("El programa ha terminado, gracias por preferirnos.")

else:
    print("Ingrese una opción valida")