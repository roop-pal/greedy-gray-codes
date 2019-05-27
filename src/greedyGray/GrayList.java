package greedyGray;
import java.util.ArrayList;
import java.util.Arrays;

// I = I element

// Encapsulate greedy algorithm into here
// Also store the prioritized operation list and use it to apply greedy a
public class GrayList<I extends CombInst> {

	private ArrayList<I> list;
	private I current;

	private Operation[] ops;
	private ArrayList<Integer> indices;
	private CombType type;
	private Object[] args;

	public GrayList(I first, Operation[] ops, CombType _type) {
		this.ops = Arrays.copyOf(ops, ops.length);
		this.list = new ArrayList<I>();
		this.indices = new ArrayList<Integer>();
		this.list.add(first);
		this.current = first;
		this.args = first.getArgs();
		this.type = _type;
	}

	public I getCurrent() {
		assert current == list.get(list.size() - 1);
		return current;
	}

	public ArrayList<I> getList() {
		return new ArrayList<I>(list);
	}

	// Apply the indexth operation to the current instance.
	// If the result is valid and not in the list, then add it and return true.
	// Otherwise, do not add the result to the list and return false.
	public boolean applyOperation(int index) {
		// Make sure that the index is value.
		assert index >= 0 && index < ops.length;

		// Apply the operation to get the proposed next instance.
		Operation op = this.ops[index];
		@SuppressWarnings("unchecked")
		I next = (I) op.execute(current);
		// Assert the types point to the same single variable
		assert next.getType() == this.type;

		// Assert the args are the same;
		assert Arrays.equals(next.getArgs(), this.args);

		// Operations should return null or a valid instance.
		assert next == null || next.validate();

		// Check if the next instance can be added to the list.
		if (next == null)
			return false;
		if (contains(next))
			return false;


		// Sanity check: Make sure that the list is not already complete.
		assert !isComplete();

		// Add the instance to the list and update current.
		this.list.add(next);
		this.indices.add(index);
		this.current = next;
		return true;
	}

	public void runGreedy() {
		int index = -1;
		while (++index < ops.length)
			if (applyOperation(index)) index = -1;
	}

	// Returns true/false depending on whether instance is in the list.
	public boolean contains(I testInstance) {
		for (I inInstance : this.list) {
			if (inInstance.equals(testInstance))
				return true;
		}
		return false;
	}


	public boolean isComplete() {
		assert list.size() > 0;
		return list.size() == this.type.numInst(this.args);
	}

	public void status() {
		System.out.println("Current Len: " + this.list.size());
		System.out.println("Maximum Len: " + this.type.numInst(this.args));
		System.out.println("Completed? " + this.isComplete());
	}

	public void print() {
		for (I e : list) System.out.println(e.toString());
	}
}
