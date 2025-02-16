class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []
        nums.sort()
        n = len(nums)
        res = []

        for i in range(n-2):
            if nums[i] > 0:
                break  

            if i > 0 and nums[i] == nums[i-1]:
                continue            # skip duplicates
            
            left, right = i+1, n-1  # two pointers

            while left < right:
                total = nums[i] + nums[left] + nums[right]

                if total == 0:
                    res.append([nums[i], nums[left], nums[right]])

                    # skipping duplicates        
                    while left < right and nums[left] == nums[left+1]:
                        left +=1
                    while left < right and nums[right] == nums[right-1]:
                        right -=1

                    # moving both pointers after finding valid tuplet
                    left += 1
                    right -= 1

                elif total < 0:
                    left += 1
                
                else:
                    right -= 1
        return res