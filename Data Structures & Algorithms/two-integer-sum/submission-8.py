class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pairs = sorted([(num, i) for i, num in enumerate(nums)])
        n = len(pairs)
        two_sum = pairs[0][0] + pairs[n-1][0]
        l = 0
        r = n-1
        while two_sum != target and l < r:
            if two_sum < target:
                l += 1
            elif two_sum > target:
                r -= 1
            two_sum = pairs[l][0] + pairs[r][0]
        return sorted([pairs[l][1], pairs[r][1]])