class Solution:
    def search(self, nums: List[int], target: int) -> int:

        leftPointer = 0
        rightPointer = len(nums) - 1

        while leftPointer <= rightPointer :

            midPointer = leftPointer + ((rightPointer - leftPointer) // 2)

            midPointerValue = nums[midPointer]

            if midPointerValue == target :
                return midPointer

            elif midPointerValue > target : 
                rightPointer = midPointer - 1

            elif midPointerValue < target :
                leftPointer = midPointer + 1

        return -1  