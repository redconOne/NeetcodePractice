from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dict = {}

        for num in nums:
            if num in dict:
                return True
            dict[num] = True

        return False


arrs = [
    [1, 2, 3, 1],
    [1, 2, 3, 4],
    [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
]
ans = [
    True,
    False,
    True
]

solution = Solution()

for i in range(len(arrs)):
    if solution.containsDuplicate(arrs[i]) == ans[i]:
        print(f"Test {i + 1} passed.")
    else:
        print(f"Test {i + 1} failed.")
