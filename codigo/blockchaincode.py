import json
from datetime import datetime

#Crea el array de la cadena de bloques
cadena  = []


class Bloque:
    def __init__(self, mail, motiv, arch):
        self.email = mail
        self.motive = motiv 
        self.archivo = arch
        self.timestamp = datetime.now()
        self.hashant = 0
        hasher = mail + motiv + arch
        self.hash = hash(hasher)

    def __hash__(self):
        return hash((self.email, self.motive, self.archivo,self.timestamp))

#Clase que maneja la cadena de bloques
class BlockManager:
    def __init__(self,cadena):
        self.cadena = cadena

#Metodo para crear bloque genesis
    def __crear_bloque_genesis__(self):
        bloqg = Bloque("","","")
        self.cadena.append(bloqg)


#Método para ingresar un bloque
    def __AgregarNuevo__(self, bloq):
            ct = [Bloque]* (len(self.cadena)+1)#Crea el nuevo arreglo más grande
            for i in range(len(self.cadena)):
                ct[i]= self.cadena[i]
            hant = self.cadena[len(self.cadena)-1].hash
            bloq.hashant = hant
            ct[len(self.cadena)]=bloq
            self.cadena = ct


