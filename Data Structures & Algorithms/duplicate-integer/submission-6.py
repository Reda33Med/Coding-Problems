class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        seeBefore = set()
        for number in nums:
            if number in seeBefore:
                return True
            else:
                seeBefore.add(number)

        return False