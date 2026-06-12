class Solution:
    def maxArea(self, heights: List[int]) -> int:
        right_pointer = len(heights) -1
        left_pointer = 0
        max_area = 0

        while right_pointer != left_pointer:

            min_height = min(heights[right_pointer],heights[left_pointer])
            length = right_pointer - left_pointer

            max_area = max(max_area,(min_height*length))

            if heights[left_pointer] >= heights[right_pointer] :
                right_pointer -= 1
            else:
                left_pointer += 1


        return max_area


        