from __init__ import *
 
import unittest
from Login import Login
from LoginException import *



class LoginTest(unittest.TestCase):
    def test_loginBiasa(self):
        user = dummyUser[1]
        self.assertEqual(Login.login(user,dummyUser),user)
        
    def test_loginSalahPassword(self):
        akunSalahPassword = User('asep', 'salahpass')
        akun = dummyUser[0]
        with self.assertRaises(LoginWrongPasswordException):
            Login.login(akunSalahPassword,dummyUser)
        
    def test_loginIdTerdaftar(self):
        akunTidakTerdaftar = User('akuntidakterdaftar', 'password')
        with self.assertRaises(LoginIdNotExistException):
            Login.login(akunTidakTerdaftar, dummyUser)
            
if __name__ == "__main__":
    unittest.main()
        