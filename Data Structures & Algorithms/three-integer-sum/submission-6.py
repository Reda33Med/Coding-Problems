class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        ansr = []
        l = 0

        for i in range(0,len(nums)):
            for j in range(i+1,len(nums)):
                for k in range(j+1,len(nums)):

                    test = sorted([nums[i] , nums[j] , nums[k]])

                    if (sum(test) == 0) and (test not in ansr):

                        ansr.append([])
                        ansr[l] = test
                        l += 1
        
        return ansr