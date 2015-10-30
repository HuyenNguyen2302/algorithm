// Problem: https://leetcode.com/problems/word-pattern/
// File: word-pattern.java
// Created by Huyen Nguyen on 10/29/2015


// Data Structure: Hash Map
// Idea: Use each letter in pattern as key,
// and each word in str as value

import java.util.HashMap;

public class Solution {
    public boolean wordPattern(String pattern, String str) {
        int start = 0; // start of a word
        int index = 0; // index of character in pattern
        HashMap<Character, String> hashMap = new HashMap<Character, String>();
        String substring = ""; // substring of str which acts as a value in the hash map
        
        // extract pairs of keys and values, and put them in the hash map
        // also return answer (if possible) 
        for (int i = start; i < str.length(); ++i) {
            if (str.charAt(i) == 32 || i == str.length() - 1) {
                if (str.charAt(i) == 32) substring = str.substring(start, i);
                if (i == str.length() - 1) substring = str.substring(start);
                System.out.println("index = " + index);
                if (index >= pattern.length()) return false;
                if (!hash(pattern.charAt(index), substring, hashMap))
                    return false;
                start = i + 1;
                ++index;
            } 
        }
        // returns false if not ALL the characters in pattern map to a word in str 
        if (index != pattern.length()) return false; 
        else return true;
    }
    
    private boolean hash(char key, String value, HashMap<Character, String> hashMap) {
        // Case 1: value is already in the hash map
        if (hashMap.containsValue(value)) {
            for (Character k : hashMap.keySet()) { // find the key which maps to the given value
                String suggestValue = hashMap.get(k);
                if (suggestValue.equals(value) && k != key)
                    return false;
            }
            return true;
        } else { // Case 2: value is not already in the hash map
            // Case 2a: the key of the value is already existed and has been mapped to a DIFFERENT value
            if (hashMap.get(key)!= null && !hashMap.get(key).equals(value)) {
                return false;
            } else { // Case 2b: both the keys and the values haven't been added to the hash map
                hashMap.put(key, value);
                return true;
            }
        }
    }
}
