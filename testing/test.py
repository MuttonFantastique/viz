import unittest
import sys



sys.path.append('/home/blackpanther/Desktop/sdlHacking/working/')
#print sys.path
from client  import *
from vizD import Child_Fork
import gui 

class Calculator(object):
 
    def add(self, x, y):
      number_types = (int, long, float, complex)

      if isinstance(x,number_types) and isinstance(y,number_types):
        return x+y
      else:
        raise ValueError




 
class TDDInPythonExample(unittest.TestCase):

    calc = Calculator()
    


    def test_calculator_add_method_returns_correct_result(self):
   
      result = self.calc.add(2,2)
      self.assertEqual(4, result)

    def test_calculator_returns_error_message_if_both_args_not_numbers(self):
      self.assertRaises(ValueError, self.calc.add, 'two', 'three')



    def test_calculator_returns_error_message_if_y_arg_not_number(self):
      self.assertRaises(ValueError, self.calc.add, 'two', 3)
 
    def test_calculator_returns_error_message_if_x_arg_not_number(self):
      self.assertRaises(ValueError, self.calc.add, 2, 'three')



class TDD_Server(unittest.TestCase):
    #child = Child_Fork()

    def test_just_experimenting(self):
      self.assertEqual(child.MSG_LENGTH, 50)





if __name__ == '__main__':
  unittest.main()