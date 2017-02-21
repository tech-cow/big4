#================================================================================
# Author: Yu Zhou
# CTCI 1.1: is Unique
#   Implement an algorithm to determine if a string has all unique characters.
#
# Q: ASCII string or Unicode String?
# Q: Can we modify input string by sorting them?
# Q: Can we use additional data structure: hash table?
#================================================================================
class Solution(object):
    #arr method
    def is_unique_arr(self,s):
        new_s = sorted(s)   #check tim_sort time
        if not s:
            return False
        temp = new_s[0]
        for i in range(1, len(new_s)):  #o(n) time
            if new_s[i] == temp:
                return False
            temp = new_s[i]
        return True

    #hash table
    def is_unique_hash(self,s):
        hash = {}
        if not s:
            return False
        for i in range(len(s)):
            if s[i] in hash:
                return False
            hash[s[i]] = i
        return True

if __name__ == '__main__':
    s = Solution()
    print "**************hash**************"
    print s.is_unique_hash("")
    print s.is_unique_hash("abc")
    print s.is_unique_hash("abcc")

    print "**************arr**************"
    print s.is_unique_arr("")
    print s.is_unique_arr("abc")
    print s.is_unique_arr("abcc")
