
class Deposito:
    def __init__(self,Nombre,CapacidadMax,Almacenado,PrecioAlmacenamiento,PrecioVenta):
        self.Nombre = Nombre
        self.CapacidadMax = CapacidadMax
        self.Almacenado = Almacenado
        self.PrecioAlmacenamiento = PrecioAlmacenamiento
        self.PrecioVenta = PrecioVenta
    
    def MostrarCapacidad (self):
        print("La cantidad almacenada en el deposito de combustible", self.Nombre, "actualmente es:", self.Almacenado,"Galones")

    def AgregarCombustible (self):
        CantidadGalones = int(input("Cuantos galones desea agregar? "))
        if CantidadGalones >= 0:
            if self.Almacenado + CantidadGalones <= self.CapacidadMax:
                print("Se agregaron", CantidadGalones, "galones de combustible al deposito", self.Nombre)
                self.Almacenado = self.Almacenado + CantidadGalones
                self.MostrarCapacidad()
            else:
                print("La cantidad por agregar supera el limite del deposito")
        else:
            print("La cantidad ingresada debe ser positiva")
        
    def MostrarValorCombustible (self):
        print("La cantidad de combustible", self.Nombre, "disponible actualmente es de", self.Almacenado,"Galones y el precio por galon es de Q", self.PrecioVenta)
    
    def VentaCombustible (self):
        GalonesVender = 0
        TipodeVenta = input("Elija el tipo de venta: (Galones) / (Valor)? ").lower()
        #Consultar la cantidad de combustible a vender
        if TipodeVenta == "galones":
            GalonesVender = int(input("Cuantos galones desea vender? "))
        elif TipodeVenta == "valor":
            GalonesVender = int(input("Qué valor desea vender? "))
            GalonesVender = GalonesVender/self.PrecioVenta #Se calculo la cantidad de galones por vender
        
        #Comprobar que respuestas del usuario sean validas
        if GalonesVender != 0 and GalonesVender >= 1:
            if self.Almacenado - GalonesVender <= 5: 
                print("No se puede vender por disponibilidad de inventario")
            else:
                print("Se puede proceder con la venta")
                Nombre = input("Ingrese el nombre del cliente: ")
                Nit = input("Ingrese el NIT del cliente: ")
                NumBomba = int(input("Ingrese el número de bomba a utilizar:"))
                if NumBomba > 0 and NumBomba < 5:
                    print("")
                    print("--------------------------------------------------------------")
                    print("Nombre:", Nombre)
                    print("NIT:", Nit)
                    print("Numero de bomba:", NumBomba)
                    print("Se vendieron", GalonesVender, "galones, por un valor de Q", GalonesVender * self.PrecioVenta)
                    print("--------------------------------------------------------------")
                    print("")
                    self.Almacenado = self.Almacenado - GalonesVender
                else:
                    print("Ingrese una bomba valida.")
        else:
            print("Su respuesta no es valida.")



#Crear depósitos
DepositoRegular = Deposito("Regular", 80, 40, 7, 29) 
DepositoSuper = Deposito("Super", 80,40, 8, 30) 
DepositoDiesel = Deposito("Diesel", 80, 40, 6, 26.50) 

#Menu
print("Bienvenido a Gasolineras Jaguar")
print("1. Gestion de Inventario")
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
    RellenarDepositos = input("Desea agregar combustible a los depositos ? Si/No ").lower()
    if RellenarDepositos == "si":
        DepositoRegular.AgregarCombustible()
        DepositoSuper.AgregarCombustible()
        DepositoDiesel.AgregarCombustible()

#Venta de Combustible
elif MenuNumero == 2:
    DepositoRegular.MostrarValorCombustible()
    DepositoSuper.MostrarValorCombustible()
    DepositoDiesel.MostrarValorCombustible()
    #Vender
    VenderCombustible = input("Desea vender combustible ? Si/No ").lower()
    if VenderCombustible == "si":
        print("1. Regular")
        print("2. Super")
        print("3. Diesel")
        TipodeCombustibleVenta = int(input("Elija el numero del tipo de combustible por vender: "))
        if TipodeCombustibleVenta == 1:
            #Vender Regular
            DepositoRegular.VentaCombustible()
        elif TipodeCombustibleVenta == 2:
            #Vender Super
            DepositoSuper.VentaCombustible()
        elif TipodeCombustibleVenta == 3:
            #Vender Diesel
            DepositoDiesel.VentaCombustible()


#Gestion de Turnos
elif  MenuNumero == 3:
    #Función por implementar, se mostrará la cantidad de empleados por jornada.
    AgregarOperadores = int(input("Cuantos operadores desea agregar ?"))
    #Asignar operadores a cada jornada.
    EliminarOperadores = int(input("Cuantos operadores desea eliminar ?"))
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
    print("Ingrese una opcion valida")