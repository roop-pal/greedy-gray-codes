package perms;

import java.util.Arrays;

import greedyGray.CombInst;
import greedyGray.Operation;

public class OPrefixRotation extends Operation {
	public int prefixLength;

	public OPrefixRotation(int prefixLength) {
		this.prefixLength = prefixLength;
		assert prefixLength > 1; // prefix 1 is not operation
	}

	public CombInst execute(CombInst prev) {
		int[] newStr = Arrays.copyOf((int[]) prev.getRep(), ((int[]) prev.getRep()).length);
		
		assert newStr.length >= prefixLength;
		int first = newStr[0];
		
		for (int i = 0; i < prefixLength - 1; i++)
			newStr[i] = newStr[i + 1];
		
		newStr[prefixLength - 1] = first;
		IPermutation next = new IPermutation(newStr, prev.getType(), prev.getArgs());
		if (!next.validate()) return null;
		assert this.validate(prev, next);
		return next;
	}

}
