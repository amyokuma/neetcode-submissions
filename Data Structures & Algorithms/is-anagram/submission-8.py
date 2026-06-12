class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #if s and t are not the same length return false
        if len(s) != len(t):
            return False

        #brute force: nested for loop and compare letter by letter

        #dictionary --> map letter to count and compare the 2 maps
        s_dict = {}
        t_dict = {}

        for char in s:
            s_dict[char] = s.count(char)

        for char in t:
            t_dict[char] = t.count(char)

        return s_dict == t_dict