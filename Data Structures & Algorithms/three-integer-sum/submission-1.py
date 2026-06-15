class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # result = []
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         for k in range(j+1, len(nums)):
        #             total = nums[i] + nums[j] + nums[k]
        #             if total == 0:
        #                 triplet = sorted([nums[i], nums[j], nums[k]])
                        
        #                 if triplet not in result:
        #                     result.append(triplet)
        # return result


        result = []
        nums.sort()
        
        for num in range(len(nums)):
            if num > 0 and nums[num] == nums[num-1]:
                continue

            left = num + 1
            right = len(nums) - 1

            while left < right:
                total = nums[left] + nums[right] + nums[num]

                if total == 0 :
                    result.append([nums[num], nums[left], nums[right]])
                    left += 1
                    right -= 1

                    while left < right and nums[left] == nums[left - 1]:
                        left += 1

                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1

                elif total < 0:
                    left += 1

                else:
                    right -= 1

        return result



        