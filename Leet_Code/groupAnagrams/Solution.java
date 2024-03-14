class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        HashMap<String, List<String>> map = new HashMap<>();
        for (String s : strs) {
            ArrayList<String> hc = new ArrayList<>();
            for (int i = 0; i < s.length(); i++) {
                String c = String.valueOf(s.charAt(i));
                hc.add(c);
            }
            Collections.sort(hc);
            String key = hc
                    .stream()
                    .reduce("", (str, element) -> str + element);
            if (map.containsKey(key)) {
                map.get(key).add(s);
            } else {
                map.put(key, new ArrayList<>());
                map.get(key).add(s);
            }
        }
        return map.values().stream().toList();
    }
}
