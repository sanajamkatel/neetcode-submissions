class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # #abc #lupapabc
        # if len(s1) > len(s2):
        #     return False

        # s1count = [0] * 26
        # s2count = [0] * 26

        # for i in range(len(s1)):
        #     s1count[ord(s[i]) - ord('a')] += 1
        #     s2count[ord(s[i]) - ord('a')] += 1

        # matches = 0
        # for i in range(26):
        #     matches += (1 if s1count[i] == s2count[i] else 0)

        # l = 0
        # for r in range(len(s1), len(s2)): #3 , #8
        #     if matches == 26:
        #         return True

        #     index = ord(s2[r]) - ord('a')
        #     s2count[index] += 1


        if len(s1) > len(s2):
            return False

        dic_s1 = {}

        for char in s1:
            dic_s1[char] = 1 + dic_s1.get(char, 0)
       
        dic_s2 = {}
        for i in range(len(s2)):
            char1 = s2[i]
            dic_s2[char1] = 1 + dic_s2.get(char1, 0)

            if i >= len(s1):
                old_char = s2[i - len(s1)]
                dic_s2[old_char] -= 1
                if dic_s2[old_char] == 0:
                    del dic_s2[old_char]

            if dic_s1 == dic_s2:
                return True

        return False



    #     # so the thing is inorder for the case to be re
    #    #abc #lecabee
       
