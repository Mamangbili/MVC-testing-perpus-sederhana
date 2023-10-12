from __init__ import *

from Register import Register
from RegisterException import *
import unittest

class RegisterTest(unittest.TestCase):
    
    def test_registerSesuaiKriteria(self):
        Id = "Ujang"
        password1 = "Ujang1234"
        password2 = "Ujang1234"
        
        register = Register(dummyUser)
        self.assertEqual(register.create(Id,password1,password2), User(Id,password1))
    
    def test_registerSalahPassword(self):
        Id = "Ujang"
        password1 = "Ujang1234"
        password2 = "Ujang12345"
        
        register = Register(dummyUser)
        with self.assertRaises(RegisterPasswordNotMatchException) :
            register.create(Id,password1,password2)
            
    def test_registerIdSudahTerdaftar(self):
        Id = "mamat"
        password1 = "uwaw1234"
        password2 = "uwaw1234"
        
        register = Register(dummyUser)
        with self.assertRaises(RegisterIdAlreadyExistException) :
            register.create(Id,password1,password2)

if __name__ == "__main__":
    unittest.main()