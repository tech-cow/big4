# Yu Zhou
# 14. Longest Common Prefix
#https://leetcode.com/problems/longest-common-prefix/


class Solution(object):
    def lcp(self, str_1, str_2):
        index = 0
        while index < len(str_1) and index < len(str_2):
            if str_1[index] == str_2[index]:
                index += 1
            else:
                break
        return str_1[:index]


    def longestCommonPrefix(self, strs):
        if not strs:
            return ''
        else:
            return reduce(self.lcp, strs)   #reduce可以让lcp这个方程不停的一个一个的运行，让array里面的array
                                            #不停的作比对
