// Problem: https://leetcode.com/problems/peeking-iterator/
// Created by Huyen Nguyen on 10/30/2015

// Idea: Save the peek value


// Java Iterator interface reference:
// https://docs.oracle.com/javase/8/docs/api/java/util/Iterator.html
class PeekingIterator implements Iterator<Integer> {
    Integer peekValue = null;
    Iterator<Integer> it;
    
	public PeekingIterator(Iterator<Integer> iterator) {
	    // initialize any member here.
	    peekValue = iterator.next();
	    this.it = iterator;
	}

    // Returns the next element in the iteration without advancing the iterator.
	public Integer peek() {
        return peekValue;
	}

	// hasNext() and next() should behave the same as in the Iterator interface.
	// Override them if needed.
	@Override
	public Integer next() {
	    int savePeekValue = peekValue; 
	    
	    // update peekValue
	    if (it.hasNext()) peekValue = it.next();
	    else peekValue = null;
	    
	    return savePeekValue;
	}

	@Override
	public boolean hasNext() {
	    return (peekValue != null);
	}
}
