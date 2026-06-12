class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = [[] for i in range(len(nums) + 1)]
        sek = {}
        solution = []

        for i in nums:
            sek[i] = 1 + sek.get(i,0)

        for n,c in sek.items():
            freq[c].append(n)

        for i in range(len(freq)-1,0,-1):
            for n in freq[i]:
                solution.append(n)
                k -=1

                if k == 0:
                    return solution
            if k ==0 :
                return solution