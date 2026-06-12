class Solution {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> combo = new HashMap<>();
        for (int i = 0; i < nums.length; i++){
            if (combo.containsKey(target - nums[i])){
                return new int[] {combo.get(target-nums[i]), i};
            }
            combo.put(nums[i], i);
        }
        return new int[] {};
    }
}