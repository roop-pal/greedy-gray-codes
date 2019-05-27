package binaryStrings;

import greedyGray.Operation;
import greedyGray.Sort;

public class SMakeLeftmost1 extends Sort{

	public Operation[] execute(Object... args) {
		assert args.length == 1;
		int n = (int) args[0];
		OChangeBit[] ret = new OChangeBit[n * 2];
		for (int i = 0; i < n; i++) {
			ret[i] = new OChangeBit(i, 1);
			ret[n + i] = new OChangeBit(i, 0);
		}
		return ret;
	}

	public String toString() {
		return this.getClass().getSimpleName() + ": " + 
			"Make the leftmost bit 1. If no bits can be flipped to 1, make the leftmost bit 0.";
	}

}
