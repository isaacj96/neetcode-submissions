class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i, _ in enumerate(numbers):
            for j, val in enumerate(numbers):
                if i < j and numbers[i] + numbers[j] == target:
                    return [i + 1, j + 1]
        return []