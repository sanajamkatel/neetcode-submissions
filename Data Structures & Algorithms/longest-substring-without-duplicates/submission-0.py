class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # "xyzxyz"
        newSet = set()
        left = 0
        max_length_substring = 0
        for i in range(len(s)):
            while s[i] in newSet:
                newSet.remove(s[left])
                left += 1

            newSet.add(s[i])
            max_length_substring = max(max_length_substring, i - left + 1)

        return max_length_substring
