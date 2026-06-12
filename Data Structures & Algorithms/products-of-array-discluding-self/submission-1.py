class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        finale_solution = []
        for i in range(0 , len(nums)):
            output = 1
            for j in range(0, len(nums)):
                if i != j :
                    output = output * nums[j] 

            finale_solution.append(output)

        return finale_solution

        