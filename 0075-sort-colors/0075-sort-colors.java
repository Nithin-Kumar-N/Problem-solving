public class Solution {
    public void sortColors(int[] nums) {
        int red = 0;
        int blue = nums.length - 1;
        int curr = 0;
        
        while (curr <= blue) {
            if (nums[curr] == 0) {
                swap(nums, red, curr);
                red++;
                curr++;
            } else if (nums[curr] == 2) {
                swap(nums, curr, blue);
                blue--;
            } else {
                curr++;
            }
        }
    }
    
    private void swap(int[] nums, int i, int j) {
        int temp = nums[i];
        nums[i] = nums[j];
        nums[j] = temp;
    }
}
