#================================================================================
# Author: Yu Zhou
# CTCI 1.4: Palindrom Permutation:
#    Given a string, write a function to check
#    if it is a permutation of a palindrome. A palindrome is a word or
#    phrase that is the same forwards and backwards. A permutation is a
#    rearrangement of letters. The palindrome does not need to be limited
#   to just dictionary words.

# Input: Tact Coa
# Output: True
#================================================================================
# Hash Table Solution
# Time complexity: O(n) count characters and then loop through smaller
# subset
# Space complexity: O(c) where c is each char / Also can be thought
# of as O(1) because set of characters is limited
import unittest

def palindrome_permutation(s):
    hash_count = hash_counter(s)
    flag = False

    for key in hash_count:
        if hash_count[key] % 2 == 1:
            if flag:
                return False
            flag = True
    return True



def hash_counter(s):
    #for a given string, counter repeated characters
    hash_count = {}
    for i in range(len(s)):
        if s[i] in hash_count:
            hash_count[s[i]] += 1
        else:
            hash_count[s[i]] = 1
    return hash_count

class Test(unittest.TestCase):
    def test_palindrome_permutation(self):
        # hash table solution
        self.assertTrue(palindrome_permutation('abcdeabcde'))
        self.assertTrue(palindrome_permutation('ddddeeeej'))
        self.assertTrue(palindrome_permutation('xyxyxyxyttu'))
        self.assertFalse(palindrome_permutation('abcdeabcdeae'))
        self.assertFalse(palindrome_permutation('aabbcdez'))
        self.assertFalse(palindrome_permutation('xyz'))

if __name__ == "__main__":
    unittest.main()
    # print hash_counter('abcdeabcde')
