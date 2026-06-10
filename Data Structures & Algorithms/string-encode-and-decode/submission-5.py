class Solution:

    def encode(self, strs: List[str]) -> str:
        encodedString = ""
        for string in strs:
            encodedString += str(len(string)) + "#" + string

        return encodedString # 5#Hello5#Kitty

    def decode(self, s: str) -> List[str]:
        decodeString  = []
        i = 0 # starting a pointer to keep track of initial string index
        while i < len(s):
            j = i 
            while s[j] != "#":
                j += 1

            length  = int(s[i:j])

            stringInitial = j + 1 #2
            stringFinal = stringInitial + length #seven

            finalString = s[stringInitial:stringFinal] #Hello

            decodeString.append(finalString)

            i = stringFinal

        return decodeString


