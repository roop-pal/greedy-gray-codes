package binaryStrings;

import greedyGray.CombInst;
import greedyGray.Operation;

public class OChangeBit extends Operation {

	private int index;
	private int value;

	public OChangeBit(int _index, int _value) {
		index = (int) _index;
		value = (int) _value;
		assert index >= 0;
		assert value == 0 || value == 1;
	}

	// Initialize operation with Object...args
	// Execute only takes in CombInst prev
	public CombInst execute(CombInst _prev) {
		IBinaryString prev = (IBinaryString) _prev;
		assert prev.validate();
		assert this.index < prev.n();
		int[] oldStr = (int[]) prev.getRep();
		int[] newStr = new int[oldStr.length];
		for (int i = 0; i < newStr.length; i++) {
			newStr[i] = oldStr[i];
			if (i == index) newStr[i] = this.value;
		}
		IBinaryString next = new IBinaryString(newStr, prev.getType(), prev.getArgs());
		if (!next.validate()) return null;
		assert this.validate(prev, next); // maintaining grayness
		return next;
	}

	public boolean validate(CombInst prev, CombInst next) {
		int s = 0;
		int[] a = (int[]) prev.getRep();
		int[] b = (int[]) next.getRep();
		for (int i = 0; i < a.length; i++) if (a[i] != b[i]) s++;
		return s <= 1;
	}

}
