import sys
import os
current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)
 
from User import *

dummyUser = [
            User("asep", "asep123"),
            User("rudi","rudi123"),
            Admin("mamat","mamat123"),
            User("cepi","cepi123")
        ]