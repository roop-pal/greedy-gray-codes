from collections import Counter
# greedy Gray code algorithm found

# dd = distinguishable balls, distinguishable boxes, (without num balls constraints)

# Informal unit tests
def test(n, k):
    ''' print "ALGORITHM 1"
    print "n:",n,"k:",k
    perms = greedy1(n, k)
    print len(perms)
    #for i in stringify(perms):
    #    print i
    classify(perms, n)
    print "|||||||||||||||||||||||||||"
    print "ALGORITHM 2"
    print "n:",n,"k:",k
    perms = greedy2(n, k)
    print len(perms)
    #for i in stringify(perms):
    #    print i
    classify(perms, n)
    print "|||||||||||||||||||||||||||"
    '''
    print "ALGORITHM 3"
    print "n:",n,"k:",k
    perms = greedy3(n, k)
    print len(perms)
    for i in stringify(perms):
        print i
    classify(perms, n)
    print "|||||||||||||||||||||||||||"
    print "ALGORITHM 4"
    print "n:",n,"k:",k
    perms = recursive(n, k)
    print len(perms)
    for i in stringify(perms):
        print i
    classify(perms, n)
    print "----------------------------"

# Move algorithm (Theorem 10 from GGA paper)
# Returns all n-ary strings of length k in array format
def greedy1(n, k):
    # The representation is a list of integers with size k where the index is the ball's value and its value is the box the ball belongs to
    first = [0] * k
    visited = [list(first)] # Initialized all balls to zeroth box
    # Using min ball yields reversed output to max ball, still reflected gray code.
    # For all n < 3, gray code is restrictive with +-1 changes which are modular
    found = True
    while found:
        found = False
        for i in range(k):
            guess = list(visited[-1])
            for j in range(n):
                guess = list(visited[-1])
                guess[k - i - 1] = j
                if guess not in visited:
                    visited.append(list(guess))
                    found = True
                    break
            if found:
                break
    return visited

# For greedy2    
def fix(mode_tuples, n):
    l = range(n)
    for i in range(len(mode_tuples)):
        l.remove(mode_tuples[i][0])
    for i in l:
        mode_tuples.append((i,0))

# Equilibrium algorithm. UNFINISHED
def greedy2(n, k):
    # The representation is a list of integers with size k where the index is the ball's value and its value is the box the ball belongs to 
    first = [0] * k # Initialized all balls to zeroth box
    visited = [list(first)]
    # Using min ball yields reversed output to max ball, still reflected gray code.
    found = True
    while found:
        found = False
        guess = list(visited[-1])
        mode_tuples = list(Counter(list(guess)).most_common()) # Prioritized list of modes and their abundances
        fix(mode_tuples, n)
        for i in range(len(mode_tuples)):
            guess = list(visited[-1])
            if mode_tuples[i][1] > 0:
                for j in range(k):
                    guess = list(visited[-1])
                    for m in range(n):
                        if j != m and guess[j] == mode_tuples[i][0]:
                            guess[j] = mode_tuples[m][0] 
                            if guess not in visited:
                                visited.append(list(guess))
                                found = True
                                break
                            guess = list(visited[-1])
                    if found:
                        break
                if found:
                    break
    return visited   
    
# Neighbors algorithm
def greedy3(n, k):
    # The representation is a list of integers with size k where the index is the ball's value and its value is the box the ball belongs to
    first = [0] * k
    visited = [list(first)] # Initialized all balls to zeroth box
    if n == 1:
        return visited
    found = True
    while found:
        found = False
        for i in range(1, k + 1):
            guess = list(visited[-1])
            guess[-i] += 1 # Try right
            if guess[-i] > 1 and (guess[-i] == n or guess in visited):
                guess[-i] -= 2 #Try left
            if guess not in visited:
                visited.append(list(guess))
                found = True
                break
    return visited  
         
# Recursive formula to check greedy3            
def recursive(n,k):
    if k == 1:
        return [[i] for i in range(n)]
    ret = []
    for i in range(0, n):
        suffixes = recursive(n, k - 1)
        if i % 2 == 1:
            suffixes.reverse()
        for j in suffixes:
            ret.append([i] + j)
    return ret

def check(n,k):
    return greedy3(n, k) == recursive(n, k)
    
# Assumes rolling
def classify(perms, n):
    n -= 1 # Adjust for mod operation
    restrictive = True
    gray = True
    for i in range(len(perms) - 1):
        changed = False
        for j in range(len(perms[i])):
            s = abs(perms[i][j] - perms[i + 1][j]) % n
            if s > 1:
                restrictive = False
            elif s > 0:
                if not changed:
                    changed = True
                else:
                    gray = False
                    break
    print "Restrictive:", restrictive
    print "Gray:", gray
    
def stringify(perms):
    ret = []
    for i in perms:
        p = ""
        for j in i:
            p += str(j)
        ret.append(p)
    return ret

if __name__ == "__main__":
    #test(4,3)
    #test(2,3)
    #test(5,2)
    bools = []
    for n in range(1,8):
        for k in range(1,6):
            x = check(n, k)
            bools.append(x)
    print all(bools)