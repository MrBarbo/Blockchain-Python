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
        self.hash = hash(self)

    def __hash__(self):
        return hash((self.email, self.motive, self.archivo,self.timestamp))

#Clase que maneja la cadena de bloques
class BlockManager:
    def __init__(self,cadena):
        self.cadena = cadena


cadena.append(Bloque("adios@gmail","mot2","files2.txt"))
