from constant import Register,dummyUser,User
import unittest
from Login import Login

class RegisterLoginITest(unittest.TestCase):
        
    def test_registerUserBiasa(self):
        username = 'testing'
        password1 = 'Testing1234'
        password2 = 'Testing1234'
    
        register =  Register(dummyUser)
        testUser = register.create(username,password1,password2) 
        dummyUser.append(testUser)   

        self.assertEqual(testUser, User(username,password1))
        
        Login.login(testUser, dummyUser)
            
 
if __name__ == "__main__":
    unittest.main() 