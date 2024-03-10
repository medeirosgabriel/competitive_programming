class Solution {
    public List<Integer> findSubstring(String s, String[] words) {
        List<Integer> result = new ArrayList<>();
        HashMap<String, Integer> map = new HashMap<>();
        for (String word : words) {
            map.put(word, map.getOrDefault(word, 0) + 1);
        }
        int wordSize =  words[0].length(), sizeSubstr = words.length * wordSize;
        int start = 0, end = sizeSubstr;
        while (end <= s.length()) {
            String sub = s.substring(start, end);
            boolean isOk = true; int i = 0;
            HashMap<String, Integer> aux = (HashMap<String, Integer>) map.clone();
            while (i + wordSize <= sizeSubstr) {
                String ss = sub.substring(i, i + wordSize);
                if (!aux.containsKey(ss) || aux.get(ss) <= 0) {
                    isOk = false; break;
                } else {
                    aux.put(ss, aux.get(ss) - 1);
                }
                i += wordSize;
            }
            if (isOk) { result.add(start);}
            start++; end++;
        }
        return result;
    }
}
