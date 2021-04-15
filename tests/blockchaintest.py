import os
import sys

import unittest

root_folder = os.path.abspath(os.path.dirname(os.path.dirname((__file__))))
sys.path.append(root_folder)

from codigo.blockchaincode  import Bloque
from codigo.blockchaincode import BlockManager
class ClassTest(unittest.TestCase):
    #(django project standard)
    #Nombre de Tests: test_[Feature being tested]


    #Test de la creacion de bloques
    def test_BlockClassCreatesABlock(self):
        Test = Bloque("hola@gmail.com","mot1","files1.txt")
        self.assertEqual(Test.email,"hola@gmail.com")
        self.assertEqual(Test.motive,"mot1")
        self.assertEqual(Test.archivo,"files1.txt")

    
    #Test de la funcion hashing
    def test_BlockHashFunctionWorks(self):
        Test = Bloque("Buendia@hola.com","mot6","file4.py")        
        self.assertEqual("0a0465b3bfdf37de3952f3919462f0d888c5c52ddfe06c4492199f7be9379df5",Test.hash)

    #Test de que dos bloques iguales tienen hash iguales y creacion de una cadena
    def test_HashFunctionAndBlockManagerWork(self):
        b1 = Bloque("hola@out.com","mot1","file1.rar")
        b2 = Bloque("hola@out.com","mot1","file1.rar")       
        self.assertEqual(b1.hash,b2.hash)


    #Test de la creacion del bloque genesis
    def test_BlockGenesisIsCreated(self):
        cadenita=[]
        Test = BlockManager(cadenita)
        Test.__crear_bloque_genesis__()
        self.assertEqual(Test.get_block(0).hashing(""),Test.get_block(0).hash)
        

    #Test de la funcion "AgregarBloque", serializacion de bloques   
    def test_AgregarBloqueCreatesBlocks(self):
        cadenita = []
        Test = BlockManager(cadenita)
        Test.__crear_bloque_genesis__()
        b1 = Bloque("hola@out.com","mot1","file1.rar")
        b2 = Bloque("adios@out.com","mot3","file2.zip")
        Test.agregar_nuevo(b1)
        Test.agregar_nuevo(b2)
        self.assertEqual(Test.get_block(1).hash, Test.get_block(2).hashant)

    #Test de la busqueda por indice (get_block)
    def test_IndexedSearchWorks(self):
        cadenita = []
        Test = BlockManager(cadenita)
        Test.__crear_bloque_genesis__()
        b1 = Bloque("buendia@in.com","mot65","file7.py")
        b2 = Bloque("adios@out.com","mot3","file2.zip")
        Test.agregar_nuevo(b1)
        Test.agregar_nuevo(b2)
        self.assertEqual(Test.get_block(2).email,"adios@out.com")

    #Test de la busqueda por hash
    def test_HashSearchWorks(self):
        cadenita = []
        Test = BlockManager(cadenita)
        Test.__crear_bloque_genesis__()
        b1 = Bloque("buendia@in.com","mot65","file7.py")
        b2 = Bloque("buenastardes@jd.com","mot8","arch1.zip")
        Test.agregar_nuevo(b1)
        Test.agregar_nuevo(b2)
        bt = Bloque("buendia@in.com","mot65","file7.py")
        ht = bt.hash
        self.assertEqual(Test.busqueda_hash(ht).hash,ht)

    #Calculando hashes bloque por bloque verificamos la cadena
    def test_ChainVerification(self):
        cadenita = []
        Test = BlockManager(cadenita)
        Test.__crear_bloque_genesis__()
        b1 = Bloque("buendia@in.com","mot65","file7.py")
        b2 = Bloque("buenastardes@jd.com","mot8","arch1.zip")
        b3 = Bloque("adios@uy.com", "mot20","arch4.mp3")
        Test.agregar_nuevo(b1)
        Test.agregar_nuevo(b2)
        Test.agregar_nuevo(b3)
        self.assertEqual(Test.get_block(1).hashant,Test.get_block(0).hash)
        self.assertEqual(Test.get_block(2).hashant, Test.get_block(1).hash)
        self.assertEqual(Test.get_block(3).hashant,Test.get_block(2).hash)

if __name__ == "__main__":
    unittest.main()