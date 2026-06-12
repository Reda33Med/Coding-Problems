class Solution:
    def maxArea(self, heights: List[int]) -> int:

        big_solution = []

        for i in range(len(heights)-1):
            for j in range(i+1,len(heights)):
                lowest = min(heights[i],heights[j]);
                big_solution.append(lowest*(j-i))

        return max(big_solution)

        