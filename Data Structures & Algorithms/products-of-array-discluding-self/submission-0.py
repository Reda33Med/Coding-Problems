class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        output = []

        for i in range(len(nums)):
            amount = 1
            for j in range(len(nums)):
                if i == j :
                    continue
                
                amount = amount * nums[j]

            output.append(amount)
        return output
        