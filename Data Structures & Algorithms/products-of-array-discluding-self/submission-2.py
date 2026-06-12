class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        finale_solution = []

        pre_fix = []
        left_k = 1
        post_fix = []
        right_k = 1

        for index in range(0 , len(nums)):

            left_k = left_k * nums[index]
            pre_fix.append(left_k)
            right_k = right_k * nums[len(nums) - index -1]
            post_fix.append(right_k)

        post_fix.reverse()

        print(pre_fix)
        print(post_fix)

        for index in range(0 , len(nums)):

            if index == 0 :
                finale_solution.append(post_fix[1])

            elif index == len(nums) - 1:
                finale_solution.append(pre_fix[index - 1])
            else:
                finale_solution.append(pre_fix[index-1] * post_fix[index + 1])

        return finale_solution

        