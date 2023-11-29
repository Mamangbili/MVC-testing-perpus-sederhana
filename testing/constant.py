import sys
import os
current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)
from Register import Register 
from User import Authorize,User, Admin

dummyUser = [
            User("asep", "asep124"),
            User("rudi","rudi123"),
            Admin("mamat","mamat123"),
            User("cepi","cepi123")
        ]