package karyStrings;

import greedyGray.Operation;
import greedyGray.Sort;

public class SLeftNudgeDownUp extends Sort {

	public Operation[] execute(Object... args) {
		assert args.length == 2;
		return SLeftNudgeDownUp.generateOps((int) args[0]);
	}

	public static Operation[] generateOps(int n) {
//		n = 6, then 0 12 34
		ONudge[] ret = new ONudge[n * 2];
		for (int i = 0; i < n; i++) {
			ret[2 * i] = new ONudge(i, -1);
			ret[2 * i + 1] = new ONudge(i, 1);
		}
		return ret;
	}

	public String toString() {
		return this.getClass().getSimpleName() + ": " +
			"Decrement or increment (in that order) the leftmost bit";
	}
}
