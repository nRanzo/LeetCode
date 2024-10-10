class Solution {
    public int[] runningSum(int[] nums) {
        int i = 0;
        while(i < nums.length - 1){
            i++;
            nums[i] += nums[i-1];
        }
        return nums;
    }
}