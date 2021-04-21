import os
import sys

import unittest

root_folder = os.path.abspath(os.path.dirname(os.path.dirname((__file__))))
sys.path.append(root_folder)

from codigo.blockchaincode  import Bloque
from codigo.blockchaincode import BlockManager
class ChainTest(unittest.TestCase):
    #(django project standard)
    #Nombre de Tests: test_[Feature being tested]
   
    #Test de la creacion del bloque genesis
    def test_BlockGenesisIsCreated(self):
        cadenita=[]
        Test = BlockManager(cadenita)
        Test._crear_bloque_genesis_()
        bloq1 = Bloque("","","","")
        self.assertEqual(bloq1.hash,Test.get_block(0).hash)
        Test.remove_chain()
        

    #Test de la funcion "AgregarBloque", serializacion de bloques   
    def test_AgregarBloqueCreatesBlocks(self):
        cadenita = []
        Test = BlockManager(cadenita)
        Test._crear_bloque_genesis_()
        b1 = Bloque("hola@out.com","mot1","file1.rar")
        b2 = Bloque("adios@out.com","mot3","file2.zip")
        Test.agregar_nuevo(b1)
        Test.agregar_nuevo(b2)
        self.assertEqual(Test.get_block(1).hash, Test.get_block(2).hashant)
        Test.remove_chain()

    #Test patron singleton
    def test_Singleton(self):
        cadenita = []
        test1 = BlockManager(cadenita)
        test2 = BlockManager(cadenita)
        test1._crear_bloque_genesis_()
        b1 = Bloque("hola@out.com","mot1","file1.rar")
        test1.agregar_nuevo(b1)
        self.assertEqual(b1.hash, test2.get_block(1).hash)
        test1.remove_chain()



    #Test de la busqueda por indice (get_block)
    def test_IndexedSearchWorks(self):
        cadenita = []
        Test = BlockManager(cadenita)
        Test._crear_bloque_genesis_()
        b1 = Bloque("buendia@in.com","mot65","file7.py")
        b2 = Bloque("adios@out.com","mot3","file2.zip")
        Test.agregar_nuevo(b1)
        Test.agregar_nuevo(b2)
        self.assertEqual("adios@out.com", Test.get_block(2).email)
        Test.remove_chain()

    #Test de la busqueda por hash
    def test_HashSearchWorks(self):
        cadenita = []
        Test = BlockManager(cadenita)
        Test._crear_bloque_genesis_()
        b1 = Bloque("buendia@in.com","mot65","file7.py")
        b2 = Bloque("buenastardes@jd.com","mot8","arch1.zip")
        Test.agregar_nuevo(b1)
        Test.agregar_nuevo(b2)
        bt = Bloque("buendia@in.com","mot65","file7.py")
        ht = bt.hash
        self.assertEqual(Test.busqueda_hash(ht).hash,ht)
        Test.remove_chain()

    #Calculando hashes bloque por bloque verificamos la cadena
    def test_ChainVerification(self):
        cadenita = []
        test = BlockManager(cadenita)
        test._crear_bloque_genesis_()

        for m in range(1,101):
            btest = Bloque(str(m) + "ia@gmail.com","mot65","file3.exe","2021-04-19 20:48")
            test.agregar_nuevo(btest)

        for j in range(1,101):
            self.assertEqual(test.get_block(j).hashant,test.get_block(j-1).hash)
            btest = Bloque(str(j) + "ia@gmail.com","mot65","file3.exe","2021-04-19 20:48")
            self.assertEqual(btest.hash,test.get_block(j).hash)
        test.remove_chain()

    #Prueba que el archivo de los hash funcione correctamente        
    def test_HashFile(self):
        cadenita = []
        test = BlockManager(cadenita)
        test._crear_bloque_genesis_()
        btest = Bloque("uioo@gmail.com","mot25","file5.exe","2021-04-19 20:48")
        test.agregar_nuevo(btest)
        test.hashes_to_file()
        file1 = open("file.txt","r")
        file1.seek(0)
        self.assertEqual(test.cadena[0].hash+test.cadena[1].hash, file1.readline())
        file1.close()
        test.remove_chain()

if __name__ == "__main__":
    unittest.main()