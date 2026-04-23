class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        match = [0] * 2
        for i, _ in enumerate(numbers):
            for j, val in enumerate(numbers):
                if i < j and numbers[i] + numbers[j] == target:
                    match[0] = i + 1
                    match[1] = j + 1
        return match