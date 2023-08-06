import unittest
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from dragonfile import readFile

class TestDragonFile(unittest.TestCase):
    def test_readFile(self):
        dFile = 'test_file.csv'
        dSep = ';'
        nameColumn = 'coluna'
        nColumn = 0

        result, nColumn = readFile(dFile, dSep, nameColumn, nColumn)

        self.assertEqual(result, {'coluna': ['valor1', 'valor2', 'valor3']})
        self.assertEqual(nColumn, 1)

    def test_readFile_FileNotFoundError(self):

        dFile = 'nao_existe.csv'
        dSep = ';'
        nameColumn = 'coluna'
        nColumn = 0

        with self.assertRaises(FileNotFoundError):
            readFile(dFile, dSep, nameColumn, nColumn)

if __name__ == '__main__':
    unittest.main()