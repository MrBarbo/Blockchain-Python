import os
import sys

import unittest

root_folder = os.path.abspath(os.path.dirname(os.path.dirname((__file__))))
sys.path.append(root_folder)

from codigo.blockchaincode  import Block

class Test(unittest.TestCase):
    def test_block(self):
        Test = Block("hola@gmail.com","mot1","file1.txt")
        self.assertEqual(email,"hola@gmail.com")
        self.assertEqual(motive,"mot1")
        self.assertEqual(archivo,"file1.txt")

if __name__ == "__main__":
    unittest.main()