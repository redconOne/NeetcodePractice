from typing import List
from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = defaultdict(list)

        for word in strs:
            count = [0] * 26
            for char in word:
                count[ord(char) - ord("a")] += 1
            ans[tuple(count)].append(word)

        return ans.values()


arrs = [
    ['eat', 'tea', 'tan', 'ate', 'nat', 'bat'],
    [''],
    ['a'],
]
ans = [
    [
        ['bat'],
        ['nat', 'tan'],
        ['ate', 'eat', 'tea']
    ],
    [
        ['']
    ],
    [
        ['a']
    ]
]

solution = Solution()

for i in range(len(arrs)):
    current = [val for val in solution.groupAnagrams(arrs[i])]
    correct = ans[i]

    for x in current:
        x = x.sort()
    for x in correct:
        x = x.sort()

    current.sort()
    correct.sort()

    if current == correct:
        print(f"Test {i + 1} passed.")
    else:
        print(f"Test {i + 1} failed.")
