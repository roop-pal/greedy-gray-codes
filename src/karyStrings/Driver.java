//package karyStrings;
//
//import java.util.ArrayList;
//
//import binaryStrings.BinaryString;
//import binaryStrings.LeftMost;
//import binaryStrings.MakeLeftmost1;
//import greedyGray.CombInst;
//import greedyGray.Sort;
//import greedyGray.Tester;
//
//
//// Eventual goal of generic "greedyGrayCode.java" which takes arguments sorts to
//// try, operation used, and initial CombInst
//public class Driver {
//
//	public static void main(String[] args) {
//		Sort[] sorts = {new LeftMost(), new MakeLeftmost1()};
//		int maxLen = 5;
//		for (int n = 1; n <= maxLen; n++) {
//			// Create list of starting BinaryStrings
//			ArrayList<BinaryString> firsts = new ArrayList<BinaryString>();
//			int[] init1 = new int[n];
//			int[] init2 = new int[n];
//			for (int j = 0; j < n; j++){
//				init1[j] = 0;
//				init2[j] = 1;
//			}
////			firsts.add(new BinaryString(init1));
//			for (CombInst i : new BinaryString(init1).allInst()) firsts.add((BinaryString) i);
//			new Tester(sorts, firsts.toArray(new BinaryString[0]));
//		}
//		
//		System.out.println("------------------------");
//		
////		int n = 5;
////		int k = 3;
////		for (int i = 0; i < n; i++) for (int j = 0; j < k; j++) 
////			System.out.println(k * i + j + " " + i + " " + j);
//		Sort[] sorts1 = {new LeftmostValueStepDownUp(), new LeftBitSmall()};
//		int maxLen1 = 3;
//		int maxK1 = 5;
//		for (int n1 = 1; n1 <= maxLen1; n1++) {
//			for (int k1 = 1; k1 <= maxK1; k1++) {
//				ArrayList<KaryString> firsts1 = new ArrayList<KaryString>();
//				int[] init11 = new int[n1];
//				int[] init21 = new int[n1];
//				for (int i1 = 0; i1 < n1; i1++) {
//					init11[i1] = 0;
//					init21[i1] = k1 - 1;
//				}
//				
////				System.out.println(Arrays.toString(init11));
////				System.out.println(Arrays.toString(init21));
//				firsts1.add(new KaryString(init11, k1));
//				firsts1.add(new KaryString(init21, k1));
//				
//				new Tester(sorts1, firsts1.toArray(new KaryString[0]));
//				/*
//				for (Sort i : sorts1) {
//					for (KaryString first1 : firsts1) {
//						System.out.println(k1 + " gray list starting with " +
//								first1.toString());
//						runSort1(first1, i);
//					}
//				}*/
//				
//			}
//		}
//	}
//	
////	public static void runSort(BinaryString first, Sort sort) {
////		GrayList<BinaryString> g = new GrayList<BinaryString>(first);
////		Operation[] ops = LeftMost.generateOps(first.n);
////		boolean found = true;
////		while (found) {
////			found = false;
////			BinaryString current = (BinaryString) g.last();
////			ops = sort.execute(current, ops);
////			for (Operation o : ops) {
////				if (g.add(o.execute(current))) {
////					found = true;
////					break;
////				}
////			}
////		}
////		g.results();
////		g.print();
////	}
////	
////	public static void runSort1(KaryString first, Sort sort) {
////		GrayList<KaryString> g = new GrayList<KaryString>(first);
////		Operation[] ops = (Operation[]) LeftBitSmall.generateOps(first.n
////																	, first.k);
////		boolean found = true;
////		while (found) {
////			found = false;
////			KaryString current = (KaryString) g.last();
////			ops = (Operation[]) sort.execute(current, ops);
////			for (Operation o : ops) {
////				if (g.add(o.execute(current))) {
////					found = true;
////					break;
////				}
////			}
////		}
////		g.results();
////		g.print();
////	}
//}