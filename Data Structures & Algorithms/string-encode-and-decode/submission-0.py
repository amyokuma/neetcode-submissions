class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string =""
        for s in strs:
            encoded_string = encoded_string + str(len(s)) + '#' + s
        return encoded_string

    def decode(self, s: str) -> List[str]:
        i = 0
        decoded_strs = []
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            word_start = j+1
            word_end = word_start + length
            decoded_strs.append(s[word_start:word_end])

            i = word_end
        return decoded_strs
            
