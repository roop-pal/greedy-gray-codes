//package perms;
//
//import java.util.ArrayList;
//
//import greedyGray.CombInst;
//import greedyGray.Sort;
//import greedyGray.Tester;
//
//
//// Eventual goal of generic "greedyGrayCode.java" which takes arguments sorts to
//// try, operation used, and initial CombInst
//public class Driver {
//
//	// TODO - this process should be a little more automated.
//	public static void main(String[] args) {
//		Sort[] sorts = {new SmallestIndices()}; // TODO - add LargestNeighbor
//		int maxLen = 5;
//		for (int n = 5; n < maxLen + 1; n++) {
//			// Create list of starting Permutations
//			ArrayList<Permutation> firsts = new ArrayList<Permutation>();
//			int[] init1 = new int[n];
//			int[] init2 = new int[n];
//			for (int j = 0; j < n; j++){
//				init1[j] = j+1;
//				init2[j] = n-j;
//			}
//			firsts.add(new Permutation(init1));
////			firsts.add(new Permutation(init2));
////			new Tester(sorts, firsts.toArray(new Permutation[0]));
//			for (CombInst i : new Permutation(init1).allInst()) System.out.println(((Permutation) i).toString());
//			System.out.println(new Permutation(init1).allInst().length + " " + new Permutation(init1).numInst());
//		}
//	}
//
//}
