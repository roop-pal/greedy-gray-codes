package binaryStrings;

import greedyGray.CombInst;
import greedyGray.Operation;

public class OFlipBit extends Operation {
	private int index;

	public OFlipBit(int _index) {
		index = _index;
		assert index >= 0;
	}

	public CombInst execute(CombInst _prev) {
		IBinaryString prev = (IBinaryString) _prev;
		assert prev.validate();
		assert this.index < prev.n();
		int[] oldStr = (int[]) prev.getRep();
		int[] newStr = new int[oldStr.length];
		for (int i = 0; i < newStr.length; i++) {
			newStr[i] = oldStr[i];
			if (i == index) newStr[i] = 1 - newStr[i];
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
