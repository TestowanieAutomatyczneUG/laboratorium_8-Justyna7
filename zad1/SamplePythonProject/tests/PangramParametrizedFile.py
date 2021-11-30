import json
import unittest
import sys
#from sample.pangram import *
sys.path.insert(1, '../src/sample')
from pangram import *

class PangramParameterizedFile(unittest.TestCase):

    def test_from_file(self):
        with open("../data/pangram_data_test.json") as fileTest:
            tmpPangram = is_pangram
            j = json.load(fileTest)
            for key in j:
                print(key)
                if 'output' in j[key]:
                    self.assertEqual(tmpPangram(j[key]['input']), j[key]['output'])
                else:
                    self.assertRaises(Exception, tmpPangram, j[key]['input'])
        # for line in fileTest:
        #     if line.startswith("#") or line.startswith(" ") or line.startswith("\n"):
        #         continue
        #     else:
        #         data = line.split(" ")
        #         inp, result = int(data[0]), data[1].strip("\n")
        #         self.assertEqual(tmpPangram(inp), result)
        #fileTest.close()


if __name__ == '__main__':
    unittest.main()
