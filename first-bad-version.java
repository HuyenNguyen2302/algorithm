// Problem: https://leetcode.com/problems/first-bad-version/
// Created by Huyen Nguyen on 10/30/2015
// Idea: Use Binary Search 

/* The isBadVersion API is defined in the parent class VersionControl.
      boolean isBadVersion(int version); */
      
import static java.lang.Math.toIntExact;

public class Solution extends VersionControl {
    public int firstBadVersion(int n) {
        int start = 1;
        int end = n;
        return findBadHelper(start, end);
    }
    
    private int findBadHelper(long start, long end) { // Use long to deal with big values of n
        if (start > end) // no bad version is found
            return -1;
            
        int middle = toIntExact((start + end) / 2); 
        if (isBadVersion(middle)) // if middle is a bad version
            if (isBadVersion(middle - 1)) // if middle is not the first bad version, then "look to the left"
                return findBadHelper(start, middle - 1);
            else // if middle is the first bad version
                return toIntExact(middle);
        else // if middle is not a bad version, then "look to the right"
             return findBadHelper(middle + 1, end);
    }
}
