class Vehiculo():
    def __init__(self, color, ruedas):
        self.color= color
        self.ruedas= ruedas
    def __str__(self):
        return "color: {} , ruedas: {}".format(self.color, self.ruedas)
class Coche(Vehiculo):
    def __init__(self, color, ruedas, velocidad, cilindrada):
        Vehiculo.__init__(self,color, ruedas)
        self.velocidad=velocidad
        self.cilindrada=cilindrada
    def __str__(self):
        return Vehiculo.__str__(self)+ ", {} km/h, {} cc".format(self.cilindrada, self.velocidad)
class Bicicleta(Vehiculo):
    def __init__(self, color, ruedas,tipo):
        Vehiculo.__init__(self,color, ruedas)
        self.tipo=tipo
    def __str__(self):
        return Vehiculo.__str__(self)+ ", tipo: {} ".format(self.tipo)
class Caminoneta(Coche):
    def __init__(self, color, ruedas, velocidad,cilindrada, carga):
        Coche.__init__(self,color,ruedas,velocidad,cilindrada)
        self.carga=carga
    def __str__(self):
        return Coche.__str__(self)+", carga: {} kg".format(self.carga)
class Motocicleta(Bicicleta):
    def __init__(self, color, ruedas, tipo, velocidad,cilindrada):
        Bicicleta.__init__(self,color,ruedas,tipo)
        self.velocidad=velocidad
        self.cilindrada=cilindrada
    def __str__(self):
        return Bicicleta.__str__(self)+", {} km/h, {} cc".format(self.velocidad,self.cilindrada)
a=Vehiculo("azul",4)
b=Coche("azul",4,180,225)
c=Bicicleta("azul",2,"urbana")
d=Caminoneta("azul",4,150,100,450)
e=Motocicleta("azul",2,"deportiva",260,1045)
def catalogar(lista):
    for vehiculo in lista:
        print(type(vehiculo).__name__, vehiculo.__dict__)
lista=[a,b,c,d,e]
def catalogar1(lista):
    contar=0
    nruedas=0
    for vehiculo in lista:
        if nruedas==vehiculo.ruedas:
            print(vehiculo)
            contar+=1
        print(f"Se ha encontrado {contar} vehículos con {nruedas} ruedas:")
catalogar(lista)
catalogar1(lista)

