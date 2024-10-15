class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1
        while left < right:
            curr_total = numbers[left] + numbers[right]
            if curr_total == target:
                return [left + 1, right + 1]
            elif curr_total < target:
                left += 1
            else:
                right -= 1