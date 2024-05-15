class Solution {
  
    public String countAndSay(int n) {
        return countAndSay(n, "1");
    }

    public String countAndSay(int n, String text) {
        if (n == 1) {
            return text;
        } else {
            String newText = "";
            int count = 0;
            char c = text.charAt(0);
            for (int i = 0; i < text.length(); i++) {
                char cc = text.charAt(i);
                if (cc == c) {
                    count += 1;
                } else {
                    newText += String.valueOf(count) + String.valueOf(c);
                    count = 1;
                    c = cc;
                }
                if (i == text.length() - 1) {
                    newText += String.valueOf(count) + String.valueOf(c);
                    count = 1;
                    c = cc;
                }
            }
            return countAndSay(n - 1, newText);
        }
    }
}
