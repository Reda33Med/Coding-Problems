class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}
        solution = []

        for i in range(len(nums)):
            if (target-nums[i]) in hash_map:
                solution.append(hash_map.get(target-nums[i]))
                solution.append(i)
                break
            else:
                hash_map[nums[i]] = i

        return solution