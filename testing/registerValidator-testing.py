
import __init__

import unittest
from User import *
from Register import Register
from RegisterException import *
dummyUser = [
            User("asep", "Asep1234"),
            User("rudi","Rudi1234"),
            Admin("mamat","Mamat1234"),
            User("cepi","Cepi1234")
        ]


register = Register(dummyUser)
class RegisterValidatorTest(unittest.TestCase):
    def test_samePassword(self):
        password1 = "habil123"
        password2 = "habil123"
        self.assertEqual(register.validateSamePassword(password1,password2),None)
        
    
    def test_notSamePassword(self):
        password1 = "habil123"
        password2 = "cepi123"
        
        with self.assertRaises(RegisterPasswordNotMatchException):
            register.validateSamePassword(password1,password2)
    
    def test_containNumberAndUpperCase(self):
        password1 = "Habil123"
        self.assertEqual(register.validateMustContainDigitAndUpperCase(password1),None)
    
    def test_notContainNumberAndUpperCase(self):
        password = ["habil123"
         ,"Habil", "wakw"]
                
        for passw in password:
            with self.assertRaises(RegisterPasswordRulesException) :
                register.validateMustContainDigitAndUpperCase(passw)
            
        
    def test_idNotRegistered(self):
        Id = "ujang"
        
        self.assertEqual(register.validateId(Id),None)
        
    
    def test_idRegistered(self):
        Id = "mamat"
        
        with self.assertRaises(RegisterIdAlreadyExistException):
            register.validateId(Id)
    
    def test_8digit(self):
        Id = ["abcde123", "foiadsiofuadsiofuadsoi"]
        
        
        for ID in Id:
            self.assertEqual(register.validate8Digit(ID),None)
    
    def test_not8digit(self):
        Id = ['dfs','13wefS']
        
        for ID in Id:
            with self.assertRaises(RegisterPasswordRulesException):
                register.validate8Digit(ID)
    
if __name__ == "__main__":
    unittest.main()