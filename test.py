from main import foo
import unittest

class TestFoo(unittest.TestCase):
	def test_foo(self):
		self.assertEqual(foo('Hello World'), 'Hello')
	def test_foo_wich_space(self):
		self.assertEqual(foo('  Hello World '), 'Hello')
	def test_foo_with_one_letter(self):
		self.assertEqual(foo('H e ll o'), 'H')


if __name__ == '__main__':
	unittest.main()