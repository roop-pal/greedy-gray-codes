package perms;

import greedyGray.Operation;
import greedyGray.Sort;

public class SLargestLeftRight extends Sort {

	public Operation[] execute(Object...args) {
		int n = (int) args[0];
		OValueNudgeSwap[] ret = new OValueNudgeSwap[2 * n];
		for (int i = 0; i < n; i++) {
			ret[2 * i] = new OValueNudgeSwap(n - i, -1);
			ret[2 * i + 1] = new OValueNudgeSwap(n - i, 1);
		}
		return ret;
	}

	public String toString() {
		return this.getClass().getSimpleName() + ": " +
			"Move the largest number left or right";
	}

}
