import json
from datetime import datetime
import hashlib


#Clase que define la estructura del bloque
class Bloque:
    def __init__(self, mail, motiv, arch):
        self.email = mail
        self.motive = motiv 
        self.archivo = arch
        self.timestamp = datetime.now()
        self.hashant = 0
        hasher = mail + motiv + arch
        self.hash = self.hashing(hasher)

    def hashing(self, hashvar):
        hasp = hashlib.sha256(hashvar.encode('ascii')).hexdigest()
        hasp = '0' +hasp[1:]
        return hasp

#Clase que maneja la cadena de bloques
class BlockManager:
    def __init__(self,cadena):
        self.cadena = cadena

    #Metodo para crear bloque genesis
    def __crear_bloque_genesis__(self):
        bloqg = Bloque("","","")
        self.cadena.append(bloqg)


    #Método para ingresar un bloque
    def agregar_nuevo(self, bloq):
            ct = [Bloque]* (len(self.cadena)+1)#Crea el nuevo arreglo más grande
            for i in range(len(self.cadena)):
                ct[i]= self.cadena[i]
            hant = self.cadena[len(self.cadena)-1].hash
            bloq.hashant = hant
            ct[len(self.cadena)]=bloq
            self.cadena = ct
    #Metodo que devuelve un bloque por su indice
    def get_block(self,ind):
        return (self.cadena[ind])
        
    #Metodo que devuelve un bloque buscando su hash
    def busqueda_hash(self,hh):
        for i in range(len(self.cadena)-1):
                if (self.cadena[i].hash == hh):
                    ind = i
        return (self.cadena[i])