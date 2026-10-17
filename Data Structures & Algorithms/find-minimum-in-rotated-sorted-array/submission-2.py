class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        left, right = 0, n - 1
        while left < right:
            med = (left + right) // 2
            if nums[med] > nums[right]:
                left = med + 1
            else:
                right = med
        return nums[left] 



        