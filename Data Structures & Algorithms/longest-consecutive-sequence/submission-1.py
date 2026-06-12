class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        solution = []

        for i in nums:
            number = i
            long_cons = 1
            for j in range(len(nums)):
                if (number + 1) in nums:
                    number = number + 1
                    long_cons +=1
                else:
                    break
            solution.append(long_cons)

        if len(nums) == 0:
            return 0
        else: 
            return(max(solution))