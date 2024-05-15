class Solution {
    public String countAndSay(int n) {
        return countAndSay(n, "1");
    }

    public String countAndSay(int n, String text) {
        if (n == 1) {
            return text;
        } else {
            StringBuilder sb = new StringBuilder();
            int count = 0;
            char c = text.charAt(0);
            for (int i = 0; i < text.length(); i++) {
                char cc = text.charAt(i);
                if (cc == c) {
                    count += 1;
                } else {
                    sb.append(String.valueOf(count));
                    sb.append(String.valueOf(c));
                    count = 1; c = cc;
                }
                if (i == text.length() - 1) {
                    sb.append(String.valueOf(count));
                    sb.append(String.valueOf(c));
                    count = 1; c = cc;
                }
            }
            return countAndSay(n - 1, sb.toString());
        }
    }
}
