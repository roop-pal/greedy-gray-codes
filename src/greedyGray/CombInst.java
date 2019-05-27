package greedyGray;

import java.util.Arrays;

public abstract class CombInst {

	protected CombType type;
	protected Object[] args;
	protected Object representation;

	public CombInst(Object _representation, CombType _type, Object... args) {
		this.type = _type;
		this.args = args; // test to ensure that args is passed by value
		this.representation = _representation;
	}

	public CombType getType() {
		return type;
	}
	public Object[] getArgs() {
		return Arrays.copyOf(args, args.length);
	}
	public Object getRep() {
		return representation;
	}

	public abstract boolean validate();

	public void check(CombInst c) {
		assert c.validate();
		assert Arrays.equals(c.getArgs(), this.getArgs());
		assert this.type == c.getType(); //Check if the types are same in memory
	}
	
	public abstract boolean equals(CombInst c);

	public String toString() {
		return representation.toString();
	}
}
