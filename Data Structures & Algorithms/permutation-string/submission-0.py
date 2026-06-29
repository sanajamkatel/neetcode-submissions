class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
       #abc #lecabee
        s1_dict = {}
        for char in s1:
            s1_dict[char] = 1 + s1_dict.get(char, 0) # {'a': 1, "b": 1, "c":1}

        s2_dict = {}
        for j in range(len(s2)):
            char = s2[j]
            s2_dict[char] = 1 + s2_dict.get(char, 0)


            if j >= len(s1):
                old_char = s2[j - len(s1)]
                s2_dict[old_char] -= 1

                if s2_dict[old_char] == 0:
                    del s2_dict[old_char]

            if s2_dict == s1_dict:
                return True

        return False

