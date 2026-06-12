class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        if not nums:
            return 0

        k = []
        nums_set = set(nums)

        for index in range(len(nums)):

            l = 0

            if (nums[index] - 1) not in nums_set:
                p = nums[index]
                #print(nums[index])
                while (p + 1) in nums_set:

                    l = l + 1
                    p = p + 1

                k.append(l)

                   
        return (max(k) +1)

