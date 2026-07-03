class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {} #create hasmap of name count
        freq = [[] for i in range(len(nums) + 1)] #create a list of lists of size len(nums) + 1

        for num in nums: #for each number in list num
            count[num] = 1 + count.get(num, 0) #in hashmap of key num add 1 to value, if none default 0
        for num, cnt in count.items(): #for each key value pair in the hashmap
            freq[cnt].append(num) #index = count add num to freq

        res = [] #output array
        for i in range(len(freq) - 1, 0, -1): # loop through freq backward, start = len(freq), stop = index 0, step = backward 1
            for num in freq[i]: # for val in freq indexed 
                res.append(num)
                if len(res) == k:
                    return res