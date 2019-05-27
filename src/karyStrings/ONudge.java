package karyStrings;

import greedyGray.CombInst;
import greedyGray.Operation;

public class ONudge extends Operation {
	
	private int index;
	private int direction;
	
	public ONudge(int _index, int _direction) {
		index = _index;
		direction = _direction;
		assert index >= 0;
		assert direction == -1 || direction == 1;
	}

	public CombInst execute(CombInst _prev) {
		IKaryString prev = (IKaryString) _prev;
		assert prev.validate();
		assert index < prev.n();
		int[] oldStr = (int[]) prev.getRep();
		int[] newStr = new int[oldStr.length];
		for (int i = 0; i < newStr.length; i++) {
			newStr[i] = oldStr[i];
			if (i == index) newStr[i] = oldStr[i] + direction;
		}
		IKaryString next = new IKaryString(newStr, prev.getType(), prev.getArgs());
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
