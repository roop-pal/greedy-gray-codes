package greedyGray;

import java.util.ArrayList;

public final class Tester {

	public Tester(Sort[] sorts, CombType type, int maxInstances) {
		for (Sort s : sorts) {
			// System.out.println("Sort: " + s);
			for (Object[] params : type.genParams(maxInstances)) {
				ArrayList<GrayList<CombInst>> lists = new ArrayList<GrayList<CombInst>>();
				ArrayList<String> firsts = new ArrayList<String>();
				String prt = "Parameters: ";
				for (Object o : params) prt += o + ", ";
				System.out.println(prt.substring(0, prt.length() - 2));
				for (CombInst f : type.allInst(params)) {
					lists.add(new GrayList<CombInst>(f, s.execute(params), type));
					firsts.add(f.toString());
				}
				for (int i = 0; i < lists.size(); i++) {
					System.out.println("Start String: " + firsts.get(i));
					GrayList<CombInst> current = lists.get(i);
					current.runGreedy();
//					current.print();
//					 current.status();
					if (current.isComplete()) {
//						System.out.println("Sort: " + s);
//						System.out.println("Start String: " + firsts.get(i));
						// current.print();
						current.status();
					}
				}
			}
		}
	}
}
