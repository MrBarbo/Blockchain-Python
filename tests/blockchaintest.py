import os
import sys

import unittest

root_folder = os.path.abspath(os.path.dirname(os.path.dirname((__file__))))
sys.path.append(root_folder)

from codigo.blockchaincode  import Bloque
from codigo.blockchaincode import BlockManager
class ClassesTest(unittest.TestCase):
    #(django project standard)
    #Nombre de Tests: test_[Feature being tested]


    #Test de la creacion de bloques
    def test_BlockClassCreatesABlock(self):
        Test = Bloque("hola@gmail.com","mot1","files1.txt")
        self.assertEqual(Test.email,"hola@gmail.com")
        self.assertEqual(Test.motive,"mot1")
        self.assertEqual(Test.archivo,"files1.txt")

    
    #Test de la funcion hash
    def test_BlockHashFunctionWorks(self):
        Test = Bloque("Buendia@hola.com","mot6","file4.py")
        self.assertEqual(Test.hash,hash("Buendia@hola.commot6file4.py"))

    #Test de la funcion hash y creacion de la cadena
    def test_HashFunctionAndBlockManagerWork(self):
        cadenita = []
        cadenita.append (Bloque("adios@gmail","mot2","files2.txt"))
        Test = BlockManager(cadenita)
        self.assertEqual(Test.cadena[0].hash, Bloque("adios@gmail","mot2","files2.txt").hash)


    #Test de la creacion del bloque genesis
    def test_BlockGenesisIsCreated(self):
        cadenita=[]
        Test = BlockManager(cadenita)
        Test.__crear_bloque_genesis__()
        self.assertEqual(Test.cadena[0].hash, hash(""))
        

    #Test de la funcion "AgregarBloque"    
    def test_AgregarBloqueCreatesBlocks(self):
        cadenita = []
        Test = BlockManager(cadenita)
        Test.__crear_bloque_genesis__()
        b1 = Bloque("hola@out.com","mot1","file1.rar")
        b2 = Bloque("adios@out.com","mot3","file2.zip")
        Test.__AgregarNuevo__(b1)
        Test.__AgregarNuevo__(b2)
        self.assertEqual(Test.cadena[1].hash, Test.cadena[2].hashant)



if __name__ == "__main__":
    unittest.main()