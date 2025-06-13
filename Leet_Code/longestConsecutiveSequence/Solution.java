class Solution {
    public int longestConsecutive(int[] nums) {
        if (nums.length == 0) return 0;
        Set<Integer> numSet = new HashSet<>();

        for (int num : nums) {
            numSet.add(num);
        }

        int maxSize = 0;

        for (int n : numSet) {
            if (!numSet.contains(n - 1)) {
                int size = 1;
                while (numSet.contains(n + size)) {
                    size += 1;
                }
                maxSize = Math.max(maxSize, size);
            }
        }
        return maxSize;
    }
}
