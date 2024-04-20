#Juan Pablo Meléndez 1134224
#Mario Andrés Sutuc 1176124


class Deposito:
    def __init__(self,Nombre,CapacidadMax,Almacenado,PrecioAlmacenamiento,PrecioVenta):
        self.Nombre = Nombre
        self.CapacidadMax = CapacidadMax
        self.Almacenado = Almacenado
        self.CostoAlmacenamiento = PrecioAlmacenamiento
        self.PrecioVenta = PrecioVenta
        self.GalonesVendidos = 0
    
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
                    self.GalonesVendidos = self.GalonesVendidos + GalonesVender
                else:
                    print("Ingrese una bomba valida.")
        else:
            print("Su respuesta no es valida.")
    
    def CalcularVentas (self):
        ValorVentas = self.GalonesVendidos * self.PrecioVenta
        return ValorVentas
    
    def CalcularCostoAlmacenamiento (self):
        ValorAlmacenamiento = self.Almacenado * self.CostoAlmacenamiento
        return ValorAlmacenamiento

class Turno:
    def __init__(self, Jornada, CantidadTrabajadores, SalarioPorHora):
        self.Jornada = Jornada
        self.CantidadTrabajadores = CantidadTrabajadores
        self.SalarioPorHora = SalarioPorHora

    def MostrarCantidadTrabajadores (self):
        print("La cantidad de trabajadores en la jornada", self.Jornada, "es de", self.CantidadTrabajadores, "trabajadores")

    def AgregarTrabajadores (self):
        AgregarOperadores = int(input("Cuantos operadores desea agregar en la jornada", self.Jornada, "?"))
        if AgregarOperadores >= 0:
            self.CantidadTrabajadores = self.CantidadTrabajadores + AgregarOperadores
            print("La cantidad de trabajadores en esta jornada es de:", self.CantidadTrabajadores)
        else:
            print("Agregue una cantidad valida")
    
    def RetirarTrabajadores (self):
        RetirarOperadores = int(input("Cuantos operadores desea retirar en la jornada", self.Jornada, "?"))
        if RetirarOperadores >= 0:
            if self.CantidadTrabajadores > RetirarOperadores and self.CantidadTrabajadores - RetirarOperadores >= 1:
                self.CantidadTrabajadores = self.CantidadTrabajadores - RetirarOperadores
                print("La cantidad de trabajadores en esta jornada es de:", self.CantidadTrabajadores)
            else:
                print("Agregue una cantidad valida")
    
    def CalcularSalario (self):
        Salario = self.CantidadTrabajadores * self.SalarioPorHora * 8
        return Salario


            
#Jornadas
JornadaDiurna = Turno("Diurna", 4, 14)
JornadaVespertina = Turno("Vespertina", 4, 14.50)
JornadaNocturna = Turno("Nocturna", 4, 15.50)

#Crear depósitos
DepositoRegular = Deposito("Regular", 80, 40, 7, 29) 
DepositoSuper = Deposito("Super", 80,40, 8, 30) 
DepositoDiesel = Deposito("Diesel", 80, 40, 6, 26.50) 

Continuar = True
while Continuar == True:
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
        JornadaDiurna.MostrarCantidadTrabajadores()
        JornadaNocturna.MostrarCantidadTrabajadores()
        JornadaVespertina.MostrarCantidadTrabajadores()
        print("Modificación de jornadas: Agregar trabajadores")
        JornadaDiurna.AgregarTrabajadores()
        JornadaVespertina.AgregarTrabajadores()
        JornadaNocturna.AgregarTrabajadores()
        print("Modificación de jornadas: Retirar trabajadores")
        JornadaDiurna.RetirarTrabajadores()
        JornadaVespertina.RetirarTrabajadores()
        JornadaNocturna.RetirarTrabajadores()
        #Costo trabajadores
        SalarioJornada = JornadaDiurna.CalcularSalario()
        print("El salario total de la jornada diurna es de Q", SalarioJornada )
        SalarioJornada = JornadaVespertina.CalcularSalario()
        print("El salario total de la jornada vespertina es de Q", SalarioJornada  )
        SalarioJornada = JornadaNocturna.CalcularSalario()
        print("El salario total de la jornada nocturna es de Q", SalarioJornada  )
    
    #Reporte de Rentabilidad
    elif MenuNumero == 4:
        IngresosTotales = DepositoRegular.CalcularVentas() + DepositoSuper.CalcularVentas() + DepositoDiesel.CalcularVentas()
        MateriaPrima = DepositoRegular.CalcularCostoAlmacenamiento() + DepositoSuper.CalcularCostoAlmacenamiento() + DepositoDiesel.CalcularCostoAlmacenamiento()
        ManoDeObra = JornadaDiurna.CalcularSalario() + JornadaVespertina.CalcularSalario() + JornadaNocturna.CalcularSalario()
        CostosFijos = 10
        UtilidadBruta = IngresosTotales - MateriaPrima - ManoDeObra - CostosFijos

        CostoCombustibleRegular = DepositoRegular.CalcularCostoAlmacenamiento()
        CostoCombustibleSuper = DepositoSuper.CalcularCostoAlmacenamiento()
        CostoCombustibleDiesel = DepositoDiesel.CalcularCostoAlmacenamiento()

        SalarioJornadaDiurna = JornadaDiurna.CalcularSalario()
        SalarioJornadaVespertina = JornadaVespertina.CalcularSalario()
        SalarioJornadaNocturna = JornadaNocturna.CalcularSalario()

        print("")
        print("--------------------------------------------------------------")
        print("Ingresos Totales:                   Q", IngresosTotales)
        print("Materia Prima:")
        print("Costo Combustible Regular:          Q",CostoCombustibleRegular )
        print("Costo Combustible Super:            Q",CostoCombustibleSuper )
        print("Costo Combustible Diesel:           Q",CostoCombustibleDiesel )
        print("Mano de obra:")
        print("Salario Jornada Diurna:             Q",SalarioJornadaDiurna )
        print("Salario Jornada Vespertina:         Q",SalarioJornadaVespertina )
        print("Salario Jornada Nocturna:           Q",SalarioJornadaNocturna)
        print("Costos Fijos:                       Q",CostosFijos)
        print("--------------------------------------------------------------")
        print("Utilidad Bruta:                     Q",UtilidadBruta)
        print("")
        print("")


    #Salida
    elif MenuNumero == 5:
        print("El programa ha terminado, gracias por preferirnos.")
        Continuar = False

    else:
        print("Ingrese una opcion valida")