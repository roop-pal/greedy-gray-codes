package binaryStrings;

import java.util.Arrays;

import greedyGray.CombInst;
import greedyGray.CombType;

public class IBinaryString extends CombInst {

	public IBinaryString(Object _representation, CombType _type, Object...args) {
		super(_representation, _type, args);
		assert args.length == 1;
		assert this.n() >= 0;
		assert this.validate();
	}

	public int n() {
		return (int) args[0];
	}

	public boolean validate() {
		if (((int[]) representation).length != this.n()) return false;
		for (int i : (int[]) this.representation)
			if (i != 0 && i != 1) return false;
		return true;
	}

	public boolean equals(CombInst c) {
		this.check(c);
		return Arrays.equals((int[]) representation, (int[]) c.getRep());
	}

	public String toString() {
		String str = "";
		for (int i : (int[]) representation) str += i;
		return str;
	}
}
