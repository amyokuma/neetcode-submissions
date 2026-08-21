class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #bruteforce: double for loop --> traverse and multiply

        #two pass
        #first pass take the product of everything to the left of i
        #second pass take the product of everything to the right of i

        #create empty list
        #create integer var
        # for i less than length of nums
            #calculate everything from index 0 to i-1
            #calculate everything from index i to length of nums
            #multiply the two
            #append to list

        #return list

        output = []
        preffix = 1
        suffix = 1

        for i in range(len(nums)):
            output.append(preffix)
            preffix *= nums[i]

# [1,2,4,6]
# [1,1,2,8]
# []
        for i in range(len(nums)-1, -1, -1):
            output[i] = output[i]*suffix
            suffix *= nums[i]

        return output