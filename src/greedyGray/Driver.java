package greedyGray;
import karyStrings.*;
import binaryStrings.*;
import perms.*;

public class Driver {

	public static void main(String[] args) {
		// binary strings
		//Sort[] biSorts = {new LeftMost(), new MakeLeftmost1()};
		//new Tester(biSorts, new BiStringType(), 512);

		// k-ary strings
		// Sort[] kSorts = {new LeftCharSmall(), new LeftNudgeDownUp()};
		// new Tester(kSorts, new KStringType(), 20);

		// permutations
		Sort[] permSorts = {new SCorbett()};
		new Tester(permSorts, new TPermType(), 720);
	}
}
