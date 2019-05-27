package karyStrings;

import java.util.ArrayList;

import greedyGray.CombInst;
import greedyGray.CombType;

public class TKStringType extends CombType {

	public int numInst(Object...args) {
		assert args.length == 2;
		return (int) Math.pow((int) args[1], (int) args[0]);
	}

	public CombInst[] allInst(Object...args) {
		assert args.length == 2;
		int n = (int) args[0];
		int k = (int) args[1];
		if (n == 0) {
			int[] asdf = {};
			CombInst[] sdaf = {new IKaryString(asdf, this, asdf.length, k)};
			return sdaf;
		}
		ArrayList<CombInst> ret = new ArrayList<CombInst>((int) Math.pow(2, n));
		for (CombInst i : this.allInst(n - 1, k)) {
			int[] p = (int[]) i.getRep();
			for (int j = 0; j < k; j++) {
				int[] a = new int[p.length + 1];
				a[0] = j;
				for (int ii = 0; ii < p.length; ii++) a[ii + 1] = p[ii];
				ret.add(new IKaryString(a, this, a.length, k));
			}
		}
		return ret.toArray(new CombInst[0]);
	}

	public Object[][] genParams(int maxInstances) {
		ArrayList<Object[]> ret = new ArrayList<Object[]>();
		int n = 2;
		while(this.numInst(n, 2) <= maxInstances) {
			int k = 2;
			while(this.numInst(n, k) <= maxInstances) {
				Object[] l = {n, k};
				ret.add(l);
				k += 1;
			}
			n += 1;
		}
		return ret.toArray(new Object[0][0]);
	}
}
