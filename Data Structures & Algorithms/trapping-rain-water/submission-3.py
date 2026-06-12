class Solution:
    def trap(self, height: List[int]) -> int:

        solution = 0
        left_max = [0]
        right_max = [0]

        for i in range(0 , len(height)-1):
            left_max.append(max(height[i] , left_max[i] ))
            right_max.append(max(height[len(height) -i-1] , right_max[i] ))

        right_max.reverse()

        print(left_max)
        print(right_max)

        for i in range(0 , len(height)):

            if (min(left_max[i] , right_max[i]) - height[i] > 0) :
                solution = solution + (min(left_max[i] , right_max[i]) - height[i])

        if len(left_max) == len(height) and len(right_max) == len(height):
            print("YES")

        return solution