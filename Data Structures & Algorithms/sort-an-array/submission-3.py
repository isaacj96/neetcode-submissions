import sys
sys.setrecursionlimit(2500) # Example: set limit to 2000

class Solution:
    def partition(self, arr, low, high):
        pivot = arr[high]

        i = low - 1

        for j in range(low, high):
            if arr[j] < pivot:
                i += 1
                self.swap(arr, i, j)
        
        self.swap(arr, i + 1, high)
        return i + 1
    
    def swap(self, arr, i, j):
        arr[i], arr[j] = arr[j], arr[i]
    
    def quickySort(self, arr, low, high):
        if low < high:
            pi = self.partition(arr, low, high)
        
            self.quickySort(arr, low, pi-1)
            self.quickySort(arr, pi+1,high)

    def sortArray(self, nums: List[int]) -> List[int]:
        n = len(nums)

        self.quickySort(nums, 0, n-1)

        return nums