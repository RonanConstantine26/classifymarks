#!/usr/bin/env python3
import unittest
import classify

class TestClassify(unittest.TestCase):
	def setUp(self):
		self.data = open("TestData.txt")
		self.results = classify.getData(self.data)

	def test_getData(self):
		self.assertEqual(self.results[0][0],'1')
		self.assertEqual(self.results[2][1],40)
	
	def test_thoseInRange(self):
		students = classify.thoseInRange(self.results, 0, 25)
		self.assertEqual(len(students),3)
		self.assertEqual(students[0],'1')
		self.assertEqual(students[1],'9')
		self.assertEqual(students[2],'10')

	

	
if __name__ == '__main__':


    unittest.main()

