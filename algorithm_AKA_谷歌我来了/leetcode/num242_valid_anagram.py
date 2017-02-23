#My solution
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        str_1 = sorted(s)
        str_2 = sorted(t)

        if len(str_1) != len(str_2):
            return False
        else:
            return self._comepare(str_1, str_2)

    def _comepare(self, s , t):
        for i in range(len(s)):
            if s[i] != t[i]:
                return False
        return True

#Smart Solution
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        str_1 = sorted(s)
        str_2 = sorted(t)
        
        if len(str_1) != len(str_2):
            return False
        else:
            return self._comepare(str_1, str_2)

    def _comepare(self, s , t):
        for i in range(len(s)):
            if s[i] != t[i]:
                return False
        return True
