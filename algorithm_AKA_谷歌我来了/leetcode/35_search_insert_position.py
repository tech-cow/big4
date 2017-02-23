
class Solution(object):
def searchInsert(self, nums, target):
    if target > nums[len(nums) - 1]:
        return len(nums)

    if target < nums[0]:
        return 0

    min, max = 0, len(nums) - 1
    while min <= max:
        mid = (min + max)/2
        if nums[mid] > target:
            max = mid - 1
            if max >= 0:
                if nums[max] < target:
                    return max + 1
            else:
                return 0

        elif nums[mid] < target:
            min = mid + 1
            if min < len(nums):
                if nums[min] > target:
                    return min
            else:
                return len(nums)
        else:
            return mid
