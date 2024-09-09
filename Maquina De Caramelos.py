class   MaquinaDeCaramelos():
    def __init__(self):
        self._azucar = 3
        self._agua = 2
        self._saborizante_limon = 5
        self._saborizante_naranja = 5
        self._colorante_limon = 2
        self._colorante_naranja = 2
        self._cantidad_por_hora = 500
        self._mezcla_ingredientes={}

    def fabricar_caramelo_limon(self):
        cantidad_caramelos = int(input("ingrese la cantidad de caramelos que necesita"))
        self._mezcla_ingredientes = {"azucar": self._azucar * cantidad_caramelos,"agua":self._agua*cantidad_caramelos
            ,"colorante amarillo":self._colorante_limon*cantidad_caramelos,"saborizante de limon":self._saborizante_limon*cantidad_caramelos}
        return f"SE ESTAN PRODUCIENDO {cantidad_caramelos} CARAMELOS SABOR A LIMÓN"

    def fabricar_caramelo_naranja(self):
        cantidad_caramelos = int(input("ingrese la cantidad de caramelos que necesita"))
        self._mezcla_ingredientes = {"azucar": self._azucar*cantidad_caramelos, "colorante anaranjado": self._colorante_naranja*cantidad_caramelos,
                         "saborizante de naranja": self._saborizante_naranja*cantidad_caramelos, "agua": self._agua*cantidad_caramelos}
        return f"SE ESTAN PRODUCIENDO {cantidad_caramelos} CARAMELOS SABOR A NARANJA"

    def eleccion_caramelo(self):
        while True:
            try:
                elegir = int(input("elija el sabor de caramelo que desea producir\n 1: caramelo de limon  \n2: caramelo de naranja"))
                if elegir == 1:
                    return self.fabricar_caramelo_limon()
                elif elegir == 2:
                    return self.fabricar_caramelo_naranja()
                else:
                    print("OPCION INCORRECTA, INTENTE NUEVAMENTE")
            except ValueError:
                        print ("ingrese un numero valido")

    def aumentar_produccion(self):
        self._cantidad_por_hora += 100
        return self._cantidad_por_hora

    def Produccion(self):
        while True:
            try:
                opciones = int(input("1: detener produccion \n 2: aumentar ritmo de produccion \n 3: mostrar cantidad de materia prima utilizada \n 4: salir del programa"))
                if opciones == 1:
                    print("SE HA DETENIDO LA PRODUCCION")
                    break

                elif opciones == 2:
                    self._cantidad_por_hora += 100
                    print("SE HA AUMENTADO EL RITMO DE PRODUCCION A",self._cantidad_por_hora, "CARAMELOS POR HORA")
                elif opciones == 3:
                    print(self._mezcla_ingredientes)
                elif opciones == 4:
                    print("SALIENDO DEL PROGRAMA")
                    break
                else:
                    print("OPCION INCORRECTA INTENTE NUEVAMENTE")
            except ValueError:
                print("ingrese un numero valido")
FabricaDeCaramelos = MaquinaDeCaramelos()
print(FabricaDeCaramelos.eleccion_caramelo())
FabricaDeCaramelos.Produccion()