from typing import List

class Solution:

    # Runtime: 31ms (Beats 28.93%)
    # Memory: 7.9 MB (Beats 21.61%)
    def singleNumber1(self, nums: List[int]) -> int:
        seen = set()
        for num in nums:
            if num not in seen:
                seen.add(num)
            else:
                seen.remove(num)
        return seen.pop()

    # Memory: 8.0 MB (Beats 19.69%)
    # Runtime: 38ms (Beats 19.21%)
    def singleNumber2(self, nums: List[int]) -> int:
        res = 0
        for num in nums:
            prev_res = res
            res = num ^ res
            print(f"current res: {res} = {prev_res} ^ {num}")
        return res