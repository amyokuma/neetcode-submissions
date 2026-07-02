class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #edge case: empty string & 1 string
        #hashmap? --> look for strings with same letters
        #for each string in strs if same letters exist in hashmap then
        #group them together
        #how to know look at all the letters?
        #frequency array of all letters 0-26
        #count frequency of each letter and store in hashmap
        #compare hashmap if equal then anagrams

        groups = defaultdict(list)
        for s in strs:
            count = [0] * 26

            for char in s:
                index = ord(char) - ord('a')
                count[index] += 1
            
            key = tuple(count)
            groups[key].append(s)

        return list(groups.values())
