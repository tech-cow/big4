#===============================================
# Yu Zhou
# Given a string, find the length of the longest substring without repeating characters.
#
# Examples:
# Given "abcabcbb", the answer is "abc", which the length is 3.
# Given "bbbbb", the answer is "b", with the length of 1.
# Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
#===============================================
# Version 1:
# Double for loop
# Starting time: 12:57 AM
# Ending time: 8:42 AM
# runtime:82
# Time:  O(n)
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        prev_index = -1 #设置一个最低数
        max_len = 0
        hash = {}

        for i in range(len(s)):
            if s[i] in hash and prev_index < hash[s[i]]: #当key在hash里，且pre_index小于hash里的index的时候
                prev_index = hash[s[i]]             # 更改prev的值
            if i - prev_index > max_len:            # 当i循环到某个数，此时的prev_index也是在没有重复数的基础为0开始算
                max_len = i - prev_index            # 这样 i - prev_index就意味着在没有重复的情况下的最长， 将这个值赋值给max
            hash[s[i]] = i                          # 进行hash
        return max_len
