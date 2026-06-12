class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        solution = []
        checked = []

        for i in range(0,len(strs)):
            if sorted(strs[i]) not in checked :
                miniSolution = []
                miniSolution.append(strs[i])
                tempList = sorted(list(strs[i]))
                for j in range(i + 1, len(strs)):
                    newTempList = sorted(list(strs[j]))
                    if newTempList == tempList:
                        miniSolution.append(strs[j])
                        checked.append(sorted(list(strs[j])))

                solution.append(miniSolution)
                checked.append(strs[i])

        return solution

        