class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest_consequence = 0

        for n in numSet:
            if (n-1) not in  numSet:
                start_point = n
                length = 1

                while (start_point+1) in numSet:
                    start_point += 1
                    length += 1

                longest_consequence = max(longest_consequence, length)

        return longest_consequence

        