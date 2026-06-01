class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # nums= [1,1,2,2,2,3,3,3,3,4,4,4,4,4], k = 2
        #{1:2, 2:3, 3:4, 4:5} , k=2 answers: [3,4]
        count = {}
        for num in nums:
            count[num] = 1 + count.get(num, 0)

        # count = {"1":"2",, "2:3", "3":"4", "4":"5"} -- > [(1,2),(2,3),(3,4),(4,5)

        arr = []
        for num, cn in count.items():
            arr.append([cn, num]) #[(2,1), (3,2), (4,3), (5,4)]

        arr.sort() #(2,1), (3,2), (4,3), (5,4)]

        top_k = []
        while len(top_k) < k:
            top_k.append(arr.pop()[1])

        return top_k





            
        