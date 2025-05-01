class Solution {
    public String simplifyPath(String path) {
        String[] direc = path.split("/");
        Stack<String> stack = new Stack<>();
        for (String d : direc) {
            if (!d.isEmpty() && !d.equals(".")) {
                if (d.equals("..")) {
                    if (!stack.isEmpty()) stack.pop();
                } else {
                    stack.add(d);
                }
            }
        }
        StringBuilder newPath = new StringBuilder();
        while(!stack.isEmpty()) {
            newPath.insert(0, String.format("/%s", stack.pop()));
        }
        return (newPath.isEmpty()) ? "/" : newPath.toString();
    }
}
