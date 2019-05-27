package perms;

import greedyGray.Operation;
import greedyGray.Sort;

public class SSmallestIndices extends Sort {

	public Operation[] execute(Object... args) {
		int n = (int) args[0];
		int total, index;
		Operation[] ops;
		total = (int)((n * (n - 1)) / 2);
		ops = new Operation[total];
		index = 0;
		for (int i = 0; i < n - 1; i++) {
			for (int j = i + 1; j < n; j++) {
				ops[index] = new OIndexSwap(i, j);
				index += 1;
			}
		}
		return ops;
	}

	public String toString() {
		return this.getClass().getSimpleName() + ": " +
			"Swap elements at smallest indices";
	}
}
