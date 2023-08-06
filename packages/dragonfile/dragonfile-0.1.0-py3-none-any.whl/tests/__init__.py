import unittest
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from dragonfile import readFile

class TestDragonFile(unittest.TestCase):
    def test_readFile(self):
        dFile = 'test_file.csv'
        dSep = ';'
        nColumn = 0

        result, nColumn = readFile(dFile, dSep, nColumn)

        self.assertEqual(result, {'coluna0': ['valor1', 'valor2', 'valor3']})
        self.assertEqual(nColumn, 1)
        print(result, nColumn)

    def test_readFile_FileNotFoundError(self):

        dFile = 'nao_existe.csv'
        dSep = ';'

        nColumn = 0

        with self.assertRaises(FileNotFoundError):
            readFile(dFile, dSep, nColumn)

if __name__ == '__main__':
    unittest.main()