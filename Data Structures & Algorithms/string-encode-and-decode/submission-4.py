class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_str = ""
        for string in strs:
            encoded_str += str(len(string)) + "#" + string

        return encoded_str

    def decode(self, s: str) -> List[str]:
        decoded_str = []
        i =0
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1

            length = int(s[i:j])


            string_initial = j + 1 
            string_final = string_initial + length

            final_string = s[string_initial : string_final]

            decoded_str.append(final_string)

            i = string_final


        return decoded_str

