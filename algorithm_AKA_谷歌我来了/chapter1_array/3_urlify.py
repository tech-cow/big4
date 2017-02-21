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

            
if __name__ == '__main__':
    s = ClassName()
    print s.urlify('Mr John Smith    ')
