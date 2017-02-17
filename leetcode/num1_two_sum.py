#===============================================
# Yu Zhou
# Given an array of integers, return indices of the two numbers such that they add up to a specific target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# Example:

#Given nums = [2, 7, 11, 15], target = 9,
#Because nums[0] + nums[1] = 2 + 7 = 9,
#return [0, 1].
#===============================================
# Version 1:
# Double for loop
# Starting time: 8:26 AM
# Ending time: 8:42 AM
# runtime:582
# Time:  O(n^2)
# Space: O(1)

class Solution(object):

    def twoSum_v1(self, nums, target):
        # make sure list not empty
        if nums is not None:
        #go over the array
            for i in range(len(nums)):
                for j in range(i+1, len(nums)):
                        if nums[i] + nums[j] == target:
                            print nums[i]
                            print nums[j]
                            return [i,j]
    #直接用双重For Loop太慢，如何进行优化？


#Version 2:
# HashKey Mapping
# runtime: 482
# Time:  O(n)
# Space: O(1)
class Solution(object):
    def twoSum(self, nums, target):
        # make sure list not empty
        hash = {}
        for i in range(len(nums)):
            if target - nums[i] in hash:
                return [hash[target - nums[i]], i]
            hash[nums[i]] = i
        return (-1,-1)
