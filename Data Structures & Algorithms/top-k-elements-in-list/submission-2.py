class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        dictt = {}
        finaleSolution = []

        for number in nums:
            if number not in dictt:
                dictt[number] = 1

            else:
                dictt[number] = dictt[number] + 1

        reversedDictt = sorted( dictt.items() ,reverse = True , key= lambda x: x[1])

        i = 0
        while i < k :
            finaleSolution.append(reversedDictt[i][0])

            i+=1

        return finaleSolution