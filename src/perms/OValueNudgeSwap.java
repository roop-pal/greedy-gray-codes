package perms;
import greedyGray.CombInst;
import greedyGray.Operation;

public class OValueNudgeSwap extends Operation {
	private int value;
	private int direction;

	public OValueNudgeSwap(int _value, int _direction) {
		this.value = _value;
		this.direction = _direction;
		assert value > 0;
		assert direction == -1 || direction == 1;
	}

	public CombInst execute(CombInst prev) {
		int[] oldStr = (int[]) prev.getRep();
		int[] newStr = new int[oldStr.length];
		int index = -1;
		for (int i = 0; i < newStr.length; i++) {
			newStr[i] = oldStr[i];
			if (oldStr[i] == value) index = i;
		}
		assert index > -1;

		if (index == 0 && direction == -1) return null;
		else if (index == oldStr.length - 1 && direction == 1) return null;

		newStr[index] = oldStr[index + direction];
		newStr[index + direction] = oldStr[index];
		IPermutation next = new IPermutation(newStr, prev.getType(), prev.getArgs());
		if (!next.validate()) return null;
		assert this.validate(prev, next);
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
