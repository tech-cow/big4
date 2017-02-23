#!/usr/bin/python
# -*- coding: utf-8 -*-
#================================================================================
# Author: Yu Zhou
# CTCI [1.9] String Rotation:
#    Assume you have a method isSubstring which checks
#    if one word is substring of another. Given two strings,
#    s1 and s2, write code to check if s2 is a rotation of s1
#    using only one call to isSubstring (e.g., "waterbottle" is
#    a rotation of "erbottlewat").
#================================================================================

import unittest


def is_rotation(s1, s2):
    return len(s1) == len(s2) and _is_substring(s1, s2+s2)

def _is_substring(s1, s2):
    return s1 in s2

class Test(unittest.TestCase):
    s1A = 'cat'
    s2A = 'hat'

    s1B = 'catch'
    s2B =  'tchca'

    s1C = 'pokemon'
    s2C =  'monapoke'

    def test_is_rotation(self):
        self.assertFalse(is_rotation(Test.s1A, Test.s2A))
        self.assertTrue(is_rotation(Test.s1B, Test.s2B))
        self.assertFalse(is_rotation(Test.s1C, Test.s2C))

if __name__ == '__main__':
    unittest.main()
