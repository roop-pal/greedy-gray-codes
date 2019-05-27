package perms;

import greedyGray.Operation;
import greedyGray.Sort;

public class SCorbett extends Sort{

	public Operation[] execute(Object... args) {
		int n = (int) args[0];
		Operation[] ops;
		ops = new Operation[n - 1];
		for (int i = 0; i < (n - 1) / 2; i++) {
			ops[2 * i] = new OPrefixRotation(n - i);
			ops[2 * i + 1] = new OPrefixRotation(i + 2);
		}
		if (n % 2 == 0) ops[n - 2] = new OPrefixRotation(n / 2 + 1);
		return ops;
	}

	public String toString() {
		return this.getClass().getSimpleName() + ": " +
				"Try biggest rotation first";
	}
	
}
