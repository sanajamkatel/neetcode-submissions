class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # "xyzxyz"
        theset= set()
        left = 0
        res = 0
        for i in range(len(s)):
            while s[i] in theset:
                theset.remove(s[left])
                left += 1

            theset.add(s[i])
            res = max(res, i - left + 1)

        return res
