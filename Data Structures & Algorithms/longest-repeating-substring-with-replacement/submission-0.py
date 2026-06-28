class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # "XYYX"
        count = {}
        left = 0
        longest_length = 0
        res = 0
        for i in range(len(s)):
                count[s[i]] = 1 + count.get(s[i], 0)
                longest_length = max(longest_length, count[s[i]])

                while (i - left + 1) - longest_length > k:
                    count[s[left]] -= 1
                    left += 1

                res = max(res, i - left + 1)

        return res


        