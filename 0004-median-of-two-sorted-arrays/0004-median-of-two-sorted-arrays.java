class Solution {
    public double findMedianSortedArrays(int[] nums1, int[] nums2) {
        int n1 = nums1.length, n2 = nums2.length;

        // ensure nums1 is the smaller array, if not make it the smallest:
        if (n1 > n2)
            return findMedianSortedArrays(nums2, nums1);
        
        int n = n1 + n2;
        int left = (n1 + n2 + 1) / 2;       // left partition
        int low = 0, high = n1;

        while (low <= high) {
            int mid1 = (low + high) >> 1;   // mid index for nums1
            int mid2 = left - mid1;          // mid index for nums2

            int l1 = Integer.MIN_VALUE, l2 = Integer.MIN_VALUE;
            int r1 = Integer.MAX_VALUE, r2 = Integer.MAX_VALUE;

            if (mid1 < n1)
                r1 = nums1[mid1];
            if (mid2 < n2)
                r2 = nums2[mid2];
            if (mid1 - 1 >= 0)
                l1 = nums1[mid1 - 1];
            if (mid2 - 1 >= 0)
                l2 = nums2[mid2 - 1];
            
            if (l1 <= r2 && l2 <= r1) {
                // partition correct, median found
                if (n %2 == 1)
                    return Math.max(l1, l2);
                else
                    return ((double)(Math.max(l1, l2) + Math.min(r1, r2))) / 2.0;
            }
            else if (l1 > r2) {
                // partition must be moved toward nums1's left side
                high = mid1 - 1;
            }
            else {
                // partition must be moved toward nums1's left side
                low = mid1 + 1;
            }
        }
        // input arrays were not sorted at this pointed
        return 0;
    }
}