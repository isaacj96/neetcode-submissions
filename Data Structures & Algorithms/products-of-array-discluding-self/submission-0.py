class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        products = [0] * n
        multiply_left = [0] * n
        multiply_right = [0] * n

        multiply_left[0] = 1
        multiply_right[n - 1] = 1
        for i in range(1,n):
            multiply_left[i] = nums[i - 1] * multiply_left[i - 1]
        for i in range(n - 2, -1, -1):
            print(i)
            multiply_right[i] = nums[i+1] * multiply_right[i+1] 
            print(multiply_right)
        for i in range(n):
            products[i] = multiply_left[i] * multiply_right[i]
        
        return products