class Solution:
    def remove_neg(self, lista: List[int]) -> List[int]:
        filtered = [x for x in lista if x > 0]
        return filtered if filtered else [max(filtered)]

    def maxSum(self, nums: List[int]) -> int:
        nums = self.remove_neg(nums)        # removes more items possible O(n)
        nums = list(set(nums))         # removes duplicates in O(n)
        nums.sort()                    # order less items possible in O(n log n)
        return sum(nums)