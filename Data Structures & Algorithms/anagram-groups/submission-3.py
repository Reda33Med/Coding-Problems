class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        solution = []
        anagrams = {}
        for word in strs:
            semiAnagram = []
            tempWord = ''.join(sorted(list(word)))

            if tempWord in anagrams.keys():
                semiAnagram.append(word)

            else:
                anagrams[tempWord] = [word]

            anagrams[tempWord] = anagrams[tempWord] + semiAnagram

        for s in anagrams.values():
            solution.append(s)

        return solution