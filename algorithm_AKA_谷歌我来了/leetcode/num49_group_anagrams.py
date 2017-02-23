# Yu Zhou
# Number 49
# Given an array of strings, group anagrams together.
# For example, given: ["eat", "tea", "tan", "ate", "nat", "bat"],
# Return:
# [
#   ["ate", "eat","tea"],
#   ["nat","tan"],
#   ["bat"]
# ]

# Failed Attempt
# class Solution(object):
#     def sort_string(self, str):
#         ''.join(sorted(str))
#
#     def compare(self,str_1,str_2):
#         sort_string(str_1)
#         sort_string(str_2)
#         arr = []
#         if str_1 == str_2:
#             arr.append(str_1, str_2)
#
#     def groupAnagrams(self, strs):
#         """
#         :type strs: List[str]
#         :rtype: List[List[str]]
#         """
#         if strs is None:
#             return ''
#         else:
#             return reduce(self.compare,strs)
