
import unittest
import ageEngine

class ageTesting(unittest.TestCase):
    def test_IsChild_True(self):
        #Arrange
        value = int(10)
        #Act
        result = ageEngine.IsChild(value)
        #Assert
        self.assertEqual(result, True)

    def test_IsAdult_True(self):
        #Arrange
        value = int(25)
        #Act
        result = ageEngine.IsAdult(value)
        #Assert
        self.assertEqual(result, True)

    def test_IsPensioner_True(self):
        #Arrange
        value = int(80)
        #Act
        result = ageEngine.IsPensioner(value)
        #Assert
        self.assertEqual(result, True)


    
    

    

