from typing import List

class Solution:

    # My solution
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix = [1] * n
        suffix = [1] * n
        
        i = 0
        res = 1
        while i < n - 1:
            res = res * nums[i]
            prefix[i+1] = res
            i += 1
        
        j = n - 1
        res = 1
        while j > 0:
            res = res * nums[j]
            suffix[j-1] = res
            j -= 1

        return [x * y for x, y in zip(prefix, suffix)]

    def productExceptSelf2(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0] * n
        pref = [0] * n
        suff = [0] * n

        pref[0] = suff[n - 1] = 1
        for i in range(1, n):
            pref[i] = nums[i - 1] * pref[i - 1]
        for i in range(n - 2, -1, -1):
            suff[i] = nums[i + 1] * suff[i + 1]
        for i in range(n):
            res[i] = pref[i] * suff[i]
        return res