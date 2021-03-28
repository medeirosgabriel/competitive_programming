package medianTwoArrays;

public class Solution {
	
	public static void main(String args[]) {
		int[] nums1 = new int[] {1};
		int[] nums2 = new int[] {2};
		double out = findMedianSortedArrays(nums1, nums2);
		System.out.println(out);
	}
	
	private static double findMedianSortedArrays(int[] nums1, int[] nums2) {
		
		int size1 = nums1.length, size2 = nums2.length;
		int sum = size1 + size2;
        int medianp = sum/2;
        
        int p1 = 0, p2 = 0, r1 = 0, r2 = 0;
        
        while ((p1 < size1 || p2 < size2) && (p1 + p2) <= medianp) {
        	r2 = r1;
        	if (p1 < size1) {
        		if (p2 < size2) {
            		r1 = (nums1[p1] <= nums2[p2]) ? nums1[p1++] : nums2[p2++];
        		} else {
            		r1 = nums1[p1++];
        		}
        	} else {
        		r1 = nums2[p2++];
        	}
        }
        
        return (sum % 2 == 0) ? (r1 + r2)/2.0 : r1;
    }
}
