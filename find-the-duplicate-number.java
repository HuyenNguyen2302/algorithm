// Problem: https://leetcode.com/problems/find-the-duplicate-number/
// Created by Huyen Nguyen on 10/31/2015

// Idea: Use Floyd's cycle-finding algorithm
// Slight modification: Because we're not working with 
// linked list, I'll use the idea that fast and slow have to 
// point at the same values at some point. Basically what I'm doing is
// comparing all pairs of values in nums to see if they match.
// Time Complexity: O(n)
// Space Complexity: O(1)

public class Solution {
    public int findDuplicate(int[] nums) {
        int fast = 1;
        int slow = 0;
        
        while (nums[fast] != nums[slow]) {          
            if (fast == nums.length - 1) fast = 1;
            else ++fast;
            if (slow == nums.length - 1) slow = 0;
            else ++slow;
        }
        return nums[fast];
    }
}
