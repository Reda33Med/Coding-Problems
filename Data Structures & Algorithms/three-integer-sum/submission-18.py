class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        final_solution = []
        nums = sorted(nums)
        seen_i = {}
        index_i = 0

        while index_i < len(nums):

            if nums[index_i] in seen_i:
                index_i += 1
                continue
            else:

                seen_i[nums[index_i]] = 1
                index_j = index_i + 1
                index_k = len(nums) - 1

                while index_j < index_k :
                    #final_solution_set = set(final_solution)
                    if ( nums[index_j] + nums[index_k] ) == ( -nums[index_i]) and [nums[index_i] , nums[index_j] , nums[index_k]] not in final_solution :
                        final_solution.append([nums[index_i] , nums[index_j] , nums[index_k]]) 

                    elif ( nums[index_j] + nums[index_k] ) < ( -nums[index_i] ) :
                        index_j += 1
                        continue

                    else: 
                        index_k -= 1
                        continue

                    index_j += 1
                    index_k -= 1   

            index_i += 1

        print(nums)
        return final_solution