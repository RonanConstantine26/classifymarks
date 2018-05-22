import unittest
import classify

class TestClassify(unittest.TestCase):
	def test_getData(self):
		f = open("TestData.txt")
		results = classify.getData(f)
		self.assertEqual(results[0][0],'1')
		self.assertEqual(results[2][1],40)
		pass

	
if __name__ == '__main__':


    unittest.main()

