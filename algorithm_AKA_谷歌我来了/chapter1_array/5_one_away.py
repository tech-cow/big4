#================================================================================
# Author: Yu Zhou
# CTCI 1.5 One Away:
#    There are three types of edits that can be performed on strings: insert a character,
#    remove a character, or replace a character. Given 2 strings, write a function to Check
#    if they are one edit(or zero) away
#
# Q: Case sensitive? Space?
#================================================================================

class ClassName(object):
    def one_away(self, s1, s2):
        if len(s1) == len(s2):
            return self._edit_by_replace(s1,s2)
        elif len(s1)-len(s2) == 1:
            return self._edit_by_insert(s1,s2)
        elif len(s2)-len(s1) == 1:
            return self._edit_by_insert(s2,s1)
        return False

    def _edit_by_replace(self, s1,s2):
        edited = False
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                if edited:
                    return False
                edit = True
        return True

    def _edit_by_insert(self,s1,s2):
        edited = False
        i, j = 0, 0
        while i < len(s1) and j < len(s2):
            if s1[i] != s2[j]:
                if edited:
                    return False
                edited = True
                i += 1
            else:
                i += 1
                j += 1
        return True

if __name__ == "__main__":
    s = ClassName()
    print s.one_away('pale', 'ple')
    print s.one_away('pald', 'pale')
    print s.one_away('pale', 'ble')
