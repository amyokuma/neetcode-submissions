class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #if s and t are not the same length return false
        if len(s) != len(t):
            return False

        #brute force: nested for loop and compare letter by letter

        #dictionary --> map letter to count and compare the 2 maps
        s_dict = {}
        t_dict = {}

        for i in range(len(s)):
            s_dict[s[i]] = 1 + s_dict.get(s[i], 0)
            t_dict[t[i]] = 1 + t_dict.get(t[i], 0)

        return s_dict == t_dict