class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len (nums)
        output = [1] * n
        lp = 1
        for i in range(n):
            output[i] = lp
            lp = lp * nums[i]
        rp = 1
        for i in range(n - 1, -1, -1):
            output[i] *= rp
            rp = rp * nums[i]
        return output