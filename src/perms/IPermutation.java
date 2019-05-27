package perms;

import java.util.Arrays;

import greedyGray.CombInst;
import greedyGray.CombType;

public class IPermutation extends CombInst {

	public IPermutation(Object _representation, CombType _type, Object...args) {
		super(_representation, _type, args);
		assert args.length == 1;
		assert this.n() > 0;
		assert this.validate();
	}

	public int n() {
		return (int) args[0];
	}

	public boolean validate() {
		// Make sure the representation has the correct length.
		if (this.n() != ((int[]) representation).length) return false;
		// Make sure that there is exactly one copy of the symbols 1, 2, ..., n.
		for (int symbol = 1; symbol <= this.n(); symbol++) {
			boolean found = false;
			for (int position = 0; position < this.n(); position++) {
				if (((int[]) representation)[position] == symbol) {
					found = true;
					break;
				}
			}
			if (found == false) return false;
		}
		return true;
	}

	public boolean equals(CombInst c) {
		this.check(c);
		return Arrays.equals((int[]) representation, (int[]) c.getRep());
	}

	public String toString() {
		String str = "";
		for (int i : (int[]) this.representation) {
			str += i;
			str += " ";
		}
		return str;
	}
}
