# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def insertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:
        pair_len = len(pairs)
        pair_list = []
        for i in range(pair_len):
            print(i)
            j = i -1
            while j >=0 and pairs[j].key > pairs[j+1].key:
                pairs[j], pairs[j + 1] = pairs[j + 1], pairs[j]
                j = j - 1
                print(j)
            pair_list.append(pairs[:])
        
        return pair_list


        