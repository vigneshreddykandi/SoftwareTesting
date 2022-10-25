import string
import unittest
import age

class Mytest(unittest.TestCase):


    #  1. Test Case for age under 18
      def child(self):
       
        #Arrange
        age=int(17)
        expectedResult="You are a child" 
        #act
        result=age.Ageverification(age)
        # assert
        self.assertEqual(result,expectedResult)


    #  Test case for age greater than 18 and under 70
      def adult(self):
       
        #Arrange
        age=int(38)
        expectedResult="You are an adult"
        #act
        result=age.Ageverification(age)
        # assert
        self.assertEqual(result,expectedResult)

  #  Test case for age greater than 70
      def pensioner(self):
       
        #Arrange
        age=int(84) 
        expectedResult="You are a pensioner"
        #act
        result=age.Ageverification(age)
        # assert
        self.assertEqual(result,expectedResult)



if __name__ == '__main__':
    unittest.main()
