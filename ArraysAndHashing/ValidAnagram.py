class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        dict1 = {}
        dict2 = {}

        for i in range(len(s)):
            if s[i] in dict1:
                dict1[s[i]] += 1
            else:
                dict1[s[i]] = 1
            if t[i] in dict2:
                dict2[t[i]] += 1
            else:
                dict2[t[i]] = 1

        for key in dict1:
            if key not in dict2 or dict1[key] != dict2[key]:
                return False

        for key in dict2:
            if key not in dict1 or dict2[key] != dict1[key]:
                return False

        return True


firstStrings = ['anagram', 'rat']
secondStrings = ['nagaram', 'car']
answers = [True, False]
solution = Solution()

for i in range(len(firstStrings)):
    if solution.isAnagram(firstStrings[i], secondStrings[i]) == answers[i]:
        print(f"Test {i + 1} passed.")
    else:
        print(f"Test {i + 1} failed")
