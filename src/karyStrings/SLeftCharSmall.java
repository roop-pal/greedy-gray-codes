package karyStrings;

import greedyGray.Operation;
import greedyGray.Sort;

public class SLeftCharSmall extends Sort{

	public Operation[] execute(Object... args) {
		assert args.length == 2;
		int n = (int) args[0];
		int k = (int) args[1];
		OChangeChar[] ret = new OChangeChar[n * k];
		for (int i = 0; i < n; i++)
			for (int j = 0; j < k; j++) ret[i * k + j] = new OChangeChar(i, j);
		return ret;
	}

	public String toString() {
		return this.getClass().getSimpleName() + ": " +
			"Make the leftmost bit the smallest value";
	}
}
