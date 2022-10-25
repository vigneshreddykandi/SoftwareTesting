#vignesh reddy kandi
import unittest
import triangle

class tgltest(unittest.TestCase):
     # 1. Test case for Equilateral Triangle
     def test_send_side1_and_side2_and_side3_To_triangle_Returns_EquilateralTriangle(self):
         #Arrange
        side1=3  
        side2=3
        side3=3
        
        expectedResult="Equilateral Triangle"
        #act
        result=triangle.triangle(side1,side2,side3)
          # assert
        self.assertEqual(result,expectedResult)

# 2. Test case for Isoceles Triangle
     def test_send_3_and_4_and_3_To_triangle_Returns_IsocelesTriangle(self):
         #Arrange
        side1=3
        side2=4
        side3=3
    
        expectedResult="Isoceles Triangle"
        #act
        result=triangle.triangle(side1,side2,side3)
         # assert
        self.assertEqual(result,expectedResult)


         # 3.Test case for Scalene Triangle
     def test_send_3_and_4_and_5_To_triangle_Returns_ScaleneTriangle(self):
         #Arrange
        side1=3
        side2=4
        side3=5
    
        expectedResult="Scalene Triangle"
        #act
         
        result=triangle.triangle(side1,side2,side3)
         # assert
        self.assertEqual(result,expectedResult)



if __name__ == '__main__':
    unittest.main()