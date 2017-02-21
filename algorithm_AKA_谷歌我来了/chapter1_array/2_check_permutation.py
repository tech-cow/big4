#================================================================================
# Author: Yu Zhou
# CTCI 1.2 Check Permutation:
#    Given 2 strings, write a method to decide if one is a permutation of the other
#
# Q: Case sensitive? Space?
#================================================================================

class Solution(object):
    def is_permutation(self, s1, s2):
        return sorted(s1) == sorted(s2)


if __name__ == '__main__':
    s = Solution()
    s1 = "ask"
    s2 = "kas"
    print s.is_permutation(s1,s2)
