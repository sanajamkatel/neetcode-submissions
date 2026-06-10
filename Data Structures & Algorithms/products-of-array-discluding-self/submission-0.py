class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left_array = [1] * len(nums)
        for i in range(1, len(nums)):
            left_array[0] = 1
            left_array[i] = left_array[i - 1] * nums[i-1]
            # it means it will get the product of everything to the right side except the number itself
            # when i = 1, 1 * 1 = 1
            # when i = 2, left_array[2] = left_array[1] * nums[1] = 1 * 2 = 2
            # when i = 3, 2 * 4 = 8
            # [1,1,2,8]

        right_array = [1] * len(nums)
        for i in range(len(nums) - 2, -1, -1): # the second last index , stop at 0 , reverse
            right_array[-1] = 1
            right_array[i] = right_array[i+1] * nums[i+1]
            # when i = 2 = 1 * 6 = 6
            # when i = 1 = 6 * 4 = 24
            # when i = 0 = 24 * 2 = 48
            # [48,24,6,1]


        result = []
        for i in range(len(nums)):
            result.append(left_array[i]* right_array[i])


        return result





        
        