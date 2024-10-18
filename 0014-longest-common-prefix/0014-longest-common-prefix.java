import java.util.Arrays;

class Solution {
    public String longestCommonPrefix(String[] v) {
        if (v == null || v.length == 0) {
            return "";
        }
        
        Arrays.sort(v);
        
        String first = v[0];
        String last = v[v.length - 1];
        StringBuilder ans = new StringBuilder();
        
        // Compare common characters between the first and last string
        for (int i = 0; i < Math.min(first.length(), last.length()); i++) {
            if (first.charAt(i) != last.charAt(i)) {
                return ans.toString();  // != characters => stop
            }
            ans.append(first.charAt(i));
        }
        
        return ans.toString();
    }
}
