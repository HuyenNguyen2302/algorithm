# Problem: https://leetcode.com/problems/reverse-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def insertionSortList(self, head):
    	# If the head is not a ListNode, return it
    	if not head:
    		return head

    	# Create the start for the linked list
    	start = ListNode(-1)
    	start.next = head
    	lastSorted = head 
    	

    	while lastSorted.next:
    		if lastSorted.next.val < lastSorted.val:
    			runner = start # runner variable runs through each element in the sorted list

    			# Compare the next value to be inserted with each element
    			# in the sorted list
    			while runner.next.val < lastSorted.next.val:
    				runner = runner.next


    			sortingElement = lastSorted.next
    			lastSorted.next = sortingElement.next # Skip the key which is sorted

    			# Insert the key to the linked list
    			sortingElement.next = runner.next 
    			runner.next = sortingElement

    		else:
    			lastSorted = lastSorted.next # Skip to the next element if this element is 
    										 # bigger or equal to the last element in the sorted list					 

    	return start.next # return the first element





