package binaryStrings;

import java.util.ArrayList;
import java.util.Arrays;

import greedyGray.CombInst;
import greedyGray.CombType;

public class TBiStringType extends CombType {

	public int numInst(Object...args) {
		assert args.length == 1;
		return (int) Math.pow(2, (int) args[0]);
	}

	public CombInst[] allInst(Object...args) {
		assert args.length == 1;
		int x = (int) args[0];
		if (x == 0) {
			int[] a = {};
			CombInst[] l = {new IBinaryString(a, this, 0)};
			return l;
		}
		ArrayList<CombInst> ret = new ArrayList<CombInst>((int) Math.pow(2, x));
		for (CombInst i : this.allInst(x - 1)) {
			int[] p = (int[]) i.getRep();
			for (int j = 0; j < 2; j++) {
				int[] a = new int[p.length + 1];
				a[0] = j;
				for (int ii = 0; ii < p.length; ii++) a[ii + 1] = p[ii];
				ret.add(new IBinaryString(a, this, a.length));
			}
		}
		return ret.toArray(new CombInst[0]);
	}

	public Object[][] genParams(int maxInstances) {
		int maxN = (int) (Math.log(maxInstances) / Math.log(2));
		Object[][] ret = new Object[maxN][1];
		for (int i = 1; i <= maxN; i++) {
			Object[] l = {i};
			ret[i - 1] = l;
		}
		return ret;
	}

}
