import os
import sys

import unittest

root_folder = os.path.abspath(os.path.dirname(os.path.dirname((__file__))))
sys.path.append(root_folder)

from codigo.blockchaincode  import Bloque
from codigo.blockchaincode import BlockManager
class Test(unittest.TestCase):
    def test_bloque(self):
        Test = Bloque("hola@gmail.com","mot1","files1.txt")
        self.assertEqual(Test.email,"hola@gmail.com")
        self.assertEqual(Test.motive,"mot1")
        self.assertEqual(Test.archivo,"files1.txt")
        self.assertEqual(Test.hash,hash(Test))
 

    def test_cadena(self):
        cadenita = []
        cadenita.append (Bloque("adios@gmail","mot2","files2.txt"))
        Test = BlockManager(cadenita)
        self.assertEqual(Test.cadena[0].hash, Bloque("adios@gmail","mot2","files2.txt").hash)



if __name__ == "__main__":
    unittest.main()