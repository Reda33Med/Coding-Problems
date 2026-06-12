class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        if not nums:
            return 0

        nums_set = set(nums)

        longest = 0


        for number in nums_set :
            if (number - 1) not in nums_set:

                length = 1

                while (number + length) in nums_set:
                    length += 1

                longest = max(longest, length)
                   
        return longest