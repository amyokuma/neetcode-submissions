class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #given array find the k most frequent values that appear in the array
        #return as a list of those values

        #first thought: loop through the array and count each val store each 
        #val as a key and its count as its value pair in a hashmap
        #take the k highest and return as a list

        count = {}

        for num in nums:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1

        output = []

        for i in range(k):
            output.append(max(count, key=count.get))
            del count[max(count, key=count.get)]

        return output