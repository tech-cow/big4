#================================================================================
# Author: Yu Zhou
# CTCI 1.5 One Away:
#     Implement a method to perform basic string compression using the counts of
#     repeated characters. For example, the string aabcccccaaa would become a2blc5a3.
#     If the "compressed" string would not become smaller than the original string,
#     your method should return the original string.
#
#================================================================================
class ClassName(object):
    def string_compression(self, s):
        counter = 0
        arr = []
        # arr.append(s[0])
        for i in range(len(s)) :
            if i != 0 and s[i] != s[i - 1]:
                arr.append(s[i - 1] + str(counter))
                counter = 0
            counter += 1

        #last repeated char
        arr.append(s[-1] + str(counter))

        return min(s, ''.join(arr), key=len)  #return the min len


if __name__ == '__main__':
    s = ClassName()
    print s.string_compression('aabcccccaaa')
    print s.string_compression('abcdef')
