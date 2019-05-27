package karyStrings;

import java.util.Arrays;

import greedyGray.CombInst;
import greedyGray.CombType;

public class IKaryString extends CombInst {
	
	public IKaryString(Object _representation, CombType _type, Object...args) {
		super(_representation, _type, args);
		assert args.length == 2;
		assert this.n() > 0;
		assert this.k() > 0;
		assert this.validate();
	}

	public int n() {
		return (int) args[0];
	}
	
	public int k() {
		return (int) args[1];
	}

	public boolean validate() {
		if (((int[]) representation).length != this.n()) return false;
		for (int i : (int[]) this.representation)
			if (i < 0 || i >= this.k()) return false;
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
