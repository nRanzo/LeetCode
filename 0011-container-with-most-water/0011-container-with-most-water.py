class Solution:
    """ 
    Two-pointer algorithm with pruning
    Optimization of algoengine algorithm that stops the search if even the maximum theoretical area
    (current width * maximum height in the array) is <= the best area found so far.
    This avoids unnecessary iterations, like in the example in the image (github),
    where we already know no remaining combination can beat the current record.
    """
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1

        largest_number = max(height)
        largest = 0

        # Continue as long as the theoretical maximum area is greater than the best found
        while (right - left) * largest_number > largest:
            area = min(height[left], height[right]) * (right - left)
            if area > largest:
                largest = area
            
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        
        return largest