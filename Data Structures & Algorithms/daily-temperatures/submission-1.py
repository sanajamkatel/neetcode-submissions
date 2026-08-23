class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # res = [0] * len(temperatures)
        # for i in range(len(temperatures)):
        #     for j in range(i+1 , len(temperatures)):
        #         if temperatures[i] < temperatures[j]:
        #             res[i] = j - i
        #             break

        # return res

        res = [0] * len(temperatures)
        stack = []

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                stackT, stackIndex = stack.pop()
                res[stackIndex] = i - stackIndex
            stack.append((t, i))

        return res


        