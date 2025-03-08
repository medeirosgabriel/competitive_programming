class Solution {
    public int[][] insert(int[][] intervals, int[] newInterval) {
        List<int[]> out = new ArrayList<>();
        int i = 0, n = intervals.length;
        while (i < n && newInterval[0] > intervals[i][1]) {
            out.add(intervals[i++]);
        }
        while (i < n && intervals[i][0] <= newInterval[1]) {
            newInterval = new int[] {
                    Math.min(intervals[i][0], newInterval[0]),
                    Math.max(intervals[i][1], newInterval[1])
            };
            i++;
        }
        out.add(newInterval);
        while (i < n) {
            out.add(intervals[i++]);
        }
        return out.toArray(new int[out.size()][2]);
    }
}
