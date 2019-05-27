package greedyGray;

// TODO - make each of the subtypes a singleton pattern?
public abstract class CombType {

	public abstract int numInst(Object... args);

	// TODO - this should not be an array that is returned.
	public abstract CombInst[] allInst(Object... args);

	public abstract Object[][] genParams(int maxInstances);

}
