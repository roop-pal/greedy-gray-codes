package greedyGray;
public abstract class Operation {
	
	public abstract CombInst execute(CombInst prev);
	
	public boolean validate(CombInst prev, CombInst next) {
		return true;
	}
}
