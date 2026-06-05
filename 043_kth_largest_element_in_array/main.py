from typing import List
import heapq
import random

# https://neetcode.io/problems/kth-largest-element-in-an-array/question?list=neetcode150
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return heapq.nlargest(k, nums)[-1]

    # QuickSelect algorithm
    def findKthLargest2(self, nums: List[int], k: int) -> int:
        l = 0
        r = len(nums) - 1
        kLargest = len(nums) - k
        while True:
            if l == r:
                return nums[l]
            pivotIndex = random.randint(l, r)
            pivotIndex = self.partition(nums, l, r, pivotIndex)
            if kLargest == pivotIndex:
                return nums[pivotIndex]
            if kLargest < pivotIndex:
                r = pivotIndex - 1
            else:
                l = pivotIndex + 1

    def partition(self, nums: List[int], l: int, r: int, pivotIndex: int) -> int:
        pivotValue = nums[pivotIndex]
        nums[pivotIndex], nums[r] = nums[r], nums[pivotIndex]
        storeIndex = l
        for i in range(l, r):
            if nums[i] < pivotValue:
                nums[storeIndex], nums[i] = nums[i], nums[storeIndex]
                storeIndex += 1
        nums[storeIndex], nums[r] = nums[r], nums[storeIndex]
        return storeIndex

    def findKthLargest3(self, nums: List[int], k: int) -> int:
        k = len(nums) - k

        def quickSelect(l, r):
            pivotValue, storeIndex = nums[r], l
            for i in range(l, r):
                if nums[i] < pivotValue:
                    nums[storeIndex], nums[i] = nums[i], nums[storeIndex]
                    storeIndex += 1
            nums[storeIndex], nums[r] = nums[r], nums[storeIndex]
            
            if storeIndex > k:
                return quickSelect(l, storeIndex - 1)
            elif storeIndex < k:
                return quickSelect(storeIndex + 1, r)
            else:
                return nums[storeIndex]
                
        return quickSelect(0, len(nums) - 1)