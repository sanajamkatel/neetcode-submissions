class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # for example index 0 = 1 banana, 1= 4 banana, 2= 3 and 3= 2 banana
        # h = hour to eat banana, k = banana / hour 
        left =  1
        right = max(piles)
        res = right 

        while left <= right:
            k = (left + right)// 2
            totalTime = 0
            for p in piles:
                totalTime += math.ceil(p/k)
            if totalTime <= h:
                res = k
                right = k - 1
            else:
                left = k + 1

        return res

        