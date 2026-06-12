class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        solution = []

        for i in range(len(numbers)):
            for j in range(i+1,len(numbers)):
                if numbers[i] + numbers[j] == target :
                    solution.append(i+1)
                    solution.append(j+1)

        return solution