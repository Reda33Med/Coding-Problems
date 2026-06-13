class Solution:
    def trap(self, height: List[int]) -> int:

        solution = 0

        left_max = height[0]
        right_max = height[-1]

        left_pointer = 0 
        right_pointer = len(height) - 1

        while left_pointer < right_pointer :

            left_max = max(left_max , height[left_pointer])
            right_max = max(right_max , height[right_pointer])

            if left_max < right_max :

                if left_max - height[left_pointer] > 0 :
                    solution = solution + ( left_max - height[left_pointer] )
                left_pointer += 1

            else:

                if right_max - height[right_pointer] > 0 :
                    solution = solution + ( right_max - height[right_pointer] )

                right_pointer -= 1

        return solution







