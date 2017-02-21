#================================================================================
# Author: Yu Zhou
# CTCI 1.3 URLify:
#   Write a method to replace all spaces in a string with '%20'. Assume string has
#   sufficient space at end of string to hold additional characters, and that you're
#   given a true length of a string. I used the books code, implementing the solution
#   in Java using a character array (given the fact that Java Strings are immutable):
#
# Q: Case sensitive? Space?
#================================================================================
class ClassName(object):
    def urlify(self, s):
        if not s:
            return False

        next_i = 1
        for i in range(len(s)):
            cur = s[i]
            while s[next_i] != None:  #check if n exist
                if cur == ' ' and s[next_i] == ' ':
                    s.pop(cur)
                if cur == ' ' and s[next_i] != ' ':
                    cur = '%20'
                # if s[i+1]:
                next_i = i+1
                print next_i
            return s

if __name__ == '__main__':
    s = ClassName()
    print s.urlify('Mr John Smith    ')
