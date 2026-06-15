class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        longest = 0

        left_pointer = 0
        right_pointer = 0

        characters_set = set()

        while right_pointer < len(s) :

            if s[right_pointer] in characters_set:
                characters_set.remove(s[left_pointer])
                left_pointer += 1
            else:
                print("Im in ELSE, my character is  : " + s[right_pointer] + " and my index is : " + str(right_pointer))
                characters_set.add(s[right_pointer])
                print("The whole character set is : " + str(characters_set))
                longest = max( longest , ((right_pointer - left_pointer) + 1) )
                right_pointer += 1



        return longest
