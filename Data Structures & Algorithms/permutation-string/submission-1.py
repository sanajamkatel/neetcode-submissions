class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
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



        # so the thing is inorder for the case to be re
       #abc #lecabee
       
