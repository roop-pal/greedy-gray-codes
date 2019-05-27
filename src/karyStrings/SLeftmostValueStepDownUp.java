package karyStrings;
//package karyStrings;
//
//import java.util.ArrayList;
//import java.util.Arrays;
//import java.util.Comparator;
//
//import greedyGray.CombInst;
//import greedyGray.Operation;
//import greedyGray.Sort;
//
//public class SLeftmostValueStepDownUp extends Sort {
//	
//	private KaryString x;
//	// TODO make static
//	private class C<T extends Operation> implements Comparator<T> {
//		public int compare(T arg0, T arg1) {
//			int a_diff = Math.abs(((ChangeBit) arg0).value - 
//								((int[]) x.getRep())[((ChangeBit) arg0).index]);
//			int b_diff = Math.abs(((ChangeBit) arg1).value - 
//								((int[]) x.getRep())[((ChangeBit) arg1).index]);
//			if (a_diff > b_diff) return 1;
//			else if (a_diff < b_diff) return -1;
//			return 0;
//		}	
//	}
//
//	public Operation[] execute(CombInst last) {
//		this.x = (KaryString) last;
//		Operation[] operations = LeftBitSmall.generateOps
//								(((KaryString) last).n, ((KaryString) last).k);
//		Arrays.sort(operations, new C<Operation>());
////		 Removes all operations that change the bit by more than 1
//		ArrayList<Operation> ret = 
//							new ArrayList<Operation>(Arrays.asList(operations));
//		ArrayList<Operation> toRemove = new ArrayList<Operation>();
//		for (Operation i : ret) {
//			if (Math.abs(((ChangeBit) i).value - 
//							((int[]) x.getRep())[((ChangeBit) i).index]) != 1) {
//				toRemove.add(i);
//			}
//		}
//		for (Operation i : toRemove) ret.remove(i);
//		return ret.toArray(new Operation[0]);
//	} 
//	
//	public String toString() {
//		return "Decrement or increment (in that order) the leftmost bit";
//	}
//
//	
//}
