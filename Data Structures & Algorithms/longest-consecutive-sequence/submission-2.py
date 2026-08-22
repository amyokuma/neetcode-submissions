class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        best_count = 0
        for num in nums_set:
            if (num-1) not in nums_set:
                val = num
                count = 1
                while (val+1) in nums_set:
                    val+=1
                    count+=1
                best_count = max(best_count, count)
                    

        return best_count

        