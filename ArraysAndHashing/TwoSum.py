from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict = {}

        for idx in range(len(nums)):
            current = nums[idx]
            complement = target - current
            if complement in dict:
                return [dict[complement], idx]
            dict[current] = idx

        return [-1]


arr1 = [2, 7, 11, 15, 7]
target1 = 9
ans1 = [0, 1]

arr2 = [3, 2, 4]
target2 = 6
ans2 = [1, 2]

arr3 = [3, 3]
target3 = 6
ans3 = [0, 1]

solution = Solution()

print("Test 1 passed." if solution.twoSum(
    arr1, target1) == ans1 else 'Test 1 failed.')
print("Test 2 passed." if solution.twoSum(
    arr2, target2) == ans2 else 'Test 2 failed.')
print("Test 3 passed." if solution.twoSum(
    arr3, target3) == ans3 else 'Test 3 failed.')
