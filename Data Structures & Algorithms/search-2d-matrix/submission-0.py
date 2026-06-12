class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        i = 0

        while i < len(matrix) :

            leftPointer = 0
            rightPointer = len(matrix[i]) - 1

            if matrix[i][rightPointer] < target :
                i += 1
                continue

            while leftPointer <= rightPointer :

                middlePointer = leftPointer + ((rightPointer - leftPointer) // 2)

                if matrix[i][middlePointer] == target :
                    return True
                elif matrix[i][middlePointer] < target :
                    leftPointer = middlePointer + 1
                else :
                    rightPointer = middlePointer - 1

            i += 1

        return False    