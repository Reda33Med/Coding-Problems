class Solution:
    def trap(self, height: List[int]) -> int:

        solution = 0
        left_max = [0] * len(height)
        right_max = [0] * len(height)

        left_max[0] = height[0]
        for i in range(1 , len(height)):
            left_max[i] = max( left_max[i - 1] , height[i])
        
        right_max[-1] = height[-1]

        for i in range(len(height) - 2 ,0 , -1) :
            right_max[i] = max( right_max[i + 1] , height[i])


        print(left_max)
        print(right_max)

        for i in range(0 , len(height)):

            if (min(left_max[i] , right_max[i]) - height[i] > 0) :
                solution = solution + (min(left_max[i] , right_max[i]) - height[i])

        if len(left_max) == len(height) and len(right_max) == len(height):
            print("YES")

        return solution