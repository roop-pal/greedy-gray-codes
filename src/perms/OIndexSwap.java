// Index-based swaps where the indices are zero-based.
// TODO - consider adding swaps based on values and/or directions.

package perms;

import greedyGray.CombInst;
import greedyGray.Operation;

public class OIndexSwap extends Operation {
	private int index1;  // TODO - consider using unsigned integers.
	private int index2;

	public OIndexSwap(int _index1, int _index2) {
		assert index1 >= 0;
		assert index2 >= 0;
		this.index1 = _index1;
		this.index2 = _index2;
	}

	public CombInst execute(CombInst prev) {
		int[] oldStr = (int[]) prev.getRep();
		int[] newStr = new int[oldStr.length];
		for (int i = 0; i < newStr.length; i++) {
			newStr[i] = oldStr[i];
			if (i == index1) newStr[i] = oldStr[index2];
			else if (i == index2) newStr[i] = oldStr[index1];
		}
		IPermutation next = new IPermutation(newStr, prev.getType(), prev.getArgs());
		if (!next.validate()) return null;
		assert this.validate(prev, next); // maintaining grayness
		return next;
	}


	public boolean validate(CombInst prev, CombInst next) {
		int s = 0;
		int[] a = (int[]) prev.getRep();
		int[] b = (int[]) next.getRep();
		for (int i = 0; i < a.length; i++) if (a[i] != b[i]) s++;
		return s == 2 || s == 0;
	}
}
