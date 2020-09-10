#!/usr/bin/env python3

"""
This is to test the standard_functions.py
"""

import unittest
from  standard_functions import genpassword

# Create a class to test your module, inheriting from the unittest.TestCase class
class Test_genpassword(unittest.TestCase):
    def test_forbidden_chars(self):
        forbidden_chars=r'x'
        passwordLength=1
        self.assertNotRegex(genpassword(forbidden_chars=forbidden_chars,passwordLength=passwordLength), rf'.*[{forbidden_chars}].*' )
        

    def test_length(self):
        forbidden_chars=r'x'
        passwordLength=5
        self.assertTrue(len(genpassword(forbidden_chars=forbidden_chars,passwordLength=passwordLength))==passwordLength)

        


# Run tests
unittest.main()


