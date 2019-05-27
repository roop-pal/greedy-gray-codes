package trees;

import greedyGray.CombInst;
import greedyGray.CombType;

public class TTreeType extends CombType {

	public int numInst(Object...args) {
		int n = (int) args[0];
		// Taken from http://www.geeksforgeeks.org/program-nth-catalan-number/

		// A recursive function to find nth catalan number
		
        int res = 0;
	         
        // Base case
        if (n <= 1) {
            return 1;
        }
        for (int i = 0; i < n; i++) {
            res += this.numInst(i) * this.numInst(n - i - 1);
        }
        return res;
	}

	@Override
	public CombInst[] allInst(Object... args) {
		// TODO Auto-generated method stub
		return null;
	}

	@Override
	public Object[][] genParams(int maxInstances) {
		// TODO Auto-generated method stub
		return null;
	}

}
