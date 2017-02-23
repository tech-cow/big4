import unittest
def one_away(s1, s2):
    #edge cases:
    #1 if length differs more than 1
    if abs(len(s1) - len(s2)) >= 2:
        return False
    #2 if s1 and s2 both exist

    #cases:
    #1 when length equal
    if s1 == s2:
        return True
    elif len(s1) == len(s2):
        return replace(s1,s2)
    # when length differs by 1, len(s1) > len(s2)
    elif len(s1) > len(s2):
        return insert(s1, s2)
    else:
        return insert(s2, s1)

def replace(s1, s2):
    edited = False
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            if edited:
                return False
            edited = True
    return True

def insert(s1, s2):
    edited = False
    i, j = 0, 0
    while i< len(s1) and j < len(s2):
        if s1[i] != s2[i]:
            if edited:
                return False
            edited = True
            i += 1
        i += 1
        j += 1

    return True


class Test(unittest.TestCase):
    def test_one_away(self):
        self.assertTrue(one_away('one','onef'))
        self.assertTrue(one_away('one','one'))
        self.assertTrue(one_away('one','onf'))
        self.assertTrue(one_away('on','onf'))
        self.assertTrue(one_away('','o'))

        self.assertFalse(one_away('one','two'))
        self.assertFalse(one_away('one','onerr'))
        self.assertFalse(one_away('blah','blabber'))

#
if __name__ == "__main__":
    unittest.main()
