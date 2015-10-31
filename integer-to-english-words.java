// Problem: https://leetcode.com/problems/integer-to-english-words/
// Created by Huyen Nguyen on 10/30/2015

// Max num = 2^31 - 1 = 2 147 483 647
// Idea: 
// + Deal with groups of 3 numbers at a time (from right to left)
// + Before dealing with a group of numbers, always remove all zeros
// + Add appropriate post-fix (billion, million, thousand) based on the position 
// of the last number in the group


public class Solution {
    public String numberToWords(int num) {
        if (num == 0) return "Zero"; // Special case
 
        String wordRep = ""; // the result
        String strVer = Integer.toString(num); // convert given num to string
        String subStr = ""; // Substring of strVer being considered
        
        for (int i = strVer.length() - 1; i >= 0; i -= 3) { // processing 3 digits at a time from right to left
            int placeValue = strVer.length() - i; 
            if (i - 3 < 0) // i reaches the max length of strVer
                subStr = strVer.substring(0, i + 1);
            else
                subStr = strVer.substring(i - 2, i + 1);
            subStr = removeZeros(subStr); 
            if (!subStr.equals("")) // only add post-fix when there's a non-zero digit in the group of numbers
                wordRep = processNumbers(subStr) + addPostFix(placeValue) + wordRep; 
        }
        return wordRep.trim(); // get rid of trailing spaces in the final answer
    }
    
    // Return string representation of a group of numbers based of its length
    private String processNumbers(String str) {
        String result = "";
        String subStr = "";
        String[] ones = {" One", " Two", " Three", " Four", " Five", " Six", " Seven", " Eight", " Nine"};
        String[] normalTens = {" Ten", " Twenty", " Thirty", " Forty", " Fifty", " Sixty", " Seventy", " Eighty", " Ninety"};
        String[] specialTens = {" Eleven", " Twelve", " Thirteen", " Fourteen", " Fifteen", " Sixteen", " Seventeen", " Eighteen", " Nineteen"};
        
        str = removeZeros(str);
        
        if (str.length() == 3)
            result = ones[str.charAt(0) - 49] + " Hundred" + processNumbers(str.substring(1));
        if (str.length() == 2) {
            if (str.equals("10")) return " Ten"; // special case
            if (normalTens(str)) 
                return result = normalTens[str.charAt(0) - 49];  // 49 is the ascii code of '1'
            if (specialTens(str)) 
                return result = specialTens[str.charAt(1) - 49];
            result = normalTens[str.charAt(0) - 49] + ones[str.charAt(1) - 49];
        }
            
        if (str.length() == 1)
            return result = ones[str.charAt(0) - 49];
        return result;  
    }
    
    private String removeZeros(String str) {
        for (int i = 0; i < str.length(); ++i) {
            if (str.charAt(i) != 48)
                return str.substring(i);
        }
        return "";
    }
    
    // Normal tens are numbers whose second digit is 0
    // So the normal tens are 10, 20, ..., 90
    private boolean normalTens(String str) {
        return (str.charAt(1) == 48); // 48 is the ascii code for '0'
    }
    
    // Special tens are numbers whose first digit is 1, and the second digit is not 0
    // So the special tens are 11, 12, ..., 19
    private boolean specialTens(String str) {
        return (str.charAt(0) == 49 && str.charAt(1) != 48);
    }
    
    // Add appropriate post-fix based on the place value
    private String addPostFix(int placeValue) {
        
        String[] postFix = {" Thousand", " Million", " Billion"};
        if (placeValue == 10) return postFix[2];
        if (placeValue == 7) return postFix[1];
        if (placeValue == 4) return postFix[0];
        return "";
    }
}
