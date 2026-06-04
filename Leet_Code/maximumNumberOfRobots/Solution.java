import java.util.ArrayDeque;
import java.util.Deque;

class Solution {
    public int maximumRobots(int[] chargeTimes, int[] runningCosts, long budget) {
        Deque<Integer> dq = new ArrayDeque<>();
        int n = chargeTimes.length, l = 0, maxSeq = 0;
        long runningSum = 0;
        for (int r = 0; r < n; r++) {
            runningSum += runningCosts[r];
            while (!dq.isEmpty() && chargeTimes[dq.getLast()] < chargeTimes[r]) {
                dq.removeLast();
            }
            dq.addLast(r);
            while (!dq.isEmpty() && (chargeTimes[dq.getFirst()] + runningSum * (r - l + 1L)) > budget) {
                runningSum -= runningCosts[l];
                if (l == dq.getFirst()) {
                    dq.removeFirst();
                }
                l += 1;
            }
            maxSeq = Math.max(maxSeq, r - l + 1);
        }
        return maxSeq;
    }
}
