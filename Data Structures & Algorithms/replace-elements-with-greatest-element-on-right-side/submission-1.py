class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        for i in range(len(arr)):
            tmp = 0
            for j in range(len(arr)):
                print(f"i: {i}, j: {j}")
                if tmp < arr[j] and j > i:
                    tmp = arr[j]
            arr[i] = tmp
        arr[-1] = -1
        return arr
                    
