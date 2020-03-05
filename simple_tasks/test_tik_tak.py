import unittest
import tik_tak_toe

class TestGame(unittest.TestCase):

  def test_space_check(self):
    my_list = ['', '', '']
    self.assertTrue(tik_tak_toe.space_check(my_list, 2))

if __name__ == '__main__':
  unittest.main()
