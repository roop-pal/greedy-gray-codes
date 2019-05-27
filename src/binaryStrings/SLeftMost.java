package binaryStrings;

import greedyGray.Operation;
import greedyGray.Sort;

public class SLeftMost extends Sort {

	public Operation[] execute(Object... args) {
		assert args.length == 1;
		int n = (int) args[0];
		Operation[] ops = new Operation[n];
		for (int i = 0; i < n; i++) ops[i] = new OFlipBit(i);
		return ops;
	}

	public String toString() {
		return this.getClass().getSimpleName() + ": " +  
			"Flip the leftmost bit";
	}
}
