import java.util.*;

class Solution {
    public void nextPermutation(int[] nums) {
        int n = nums.length, i = n - 1;
        while (i > 0 && nums[i - 1] >= nums[i]) i --;

        if (i == 0) { reverseArray(nums); return; }

        int j = n - 1;
        while (j >= i && nums[j] <= nums[i - 1]) j--;

        int aux = nums[j];
        nums[j] = nums[i - 1];
        nums[i - 1] = aux;

        int[] part = Arrays.copyOfRange(nums, i, n);   
        reverseArray(part);
        for (int k = 0; k < part.length; k++) {
            nums[k + i] = part[k];
        }
    }

    public int[] reverseArray(int[] array) {
        int startIndex = 0;
        int endIndex = array.length - 1;
        while(startIndex < endIndex) {
            int temp = array[endIndex];
            array[endIndex] = array[startIndex];
            array[startIndex] = temp;
            startIndex++;
            endIndex--;
        }
        return array;
    }
}
