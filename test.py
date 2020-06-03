import unittest

class Test(unittest.TestCase):
  def test_one(self):
    assertEqual("asd", "asd")
  
  def test_fail(self):
    assertEqual("not equal", "equal")

if __name__ == "__main__":
  unittest.main()
  # work?
