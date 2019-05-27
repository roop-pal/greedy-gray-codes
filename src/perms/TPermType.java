package perms;

import java.util.ArrayList;

import greedyGray.CombInst;
import greedyGray.CombType;

public class TPermType extends CombType{

	public int numInst(Object...args) {
		int total = 1;
		for (int i = 2; i <= (int) args[0]; i++) {
			total *= i;
		}
		return total;
	}

	public CombInst[] allInst(Object...args) {
		assert args.length == 1;
		int n = (int) args[0];
		if (n == 1) {
			int[] i = {1};
			CombInst[] ret = {new IPermutation(i, this, i.length)};
			return ret;
		}
		int total = 1;
		for (int i = 2; i <= n; i++) total *= i;
		CombInst[] ret = new CombInst[total];
		int index = 0;
		for (CombInst i : this.allInst(n - 1)) {
			ArrayList<Integer> rep = new ArrayList<Integer>();
			for (int ii : (int[]) i.getRep()) rep.add(ii);
			for (int j = 0; j <= rep.size(); j++) {
				ArrayList<Integer> toAdd = new ArrayList<Integer>();
				toAdd.addAll(rep.subList(0, j));
				toAdd.add(n);
				toAdd.addAll(rep.subList(j, rep.size()));
				int[] retArr = new int[toAdd.size()];
				int iindex = 0;
				for (Integer jj : toAdd) retArr[iindex++] = jj.intValue();
				ret[index++] = new IPermutation(retArr, this, retArr.length);
			}
		}
		return ret;
	}

	public Object[][] genParams(int maxInstances) {
		ArrayList<Object[]> ret = new ArrayList<Object[]>();
		int n = 2;
		while(this.numInst(n) <= maxInstances) {
			Object[] l = {n};
			ret.add(l);
			n += 1;
		}
		return ret.toArray(new Object[0][0]);
	}
}
