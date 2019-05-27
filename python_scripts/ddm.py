# ddm = distinguishable balls, distinguishable boxes, (at) most one ball
import math, Queue

# def test(funcTuple, orderTuple):
#     bools = []
#     permList = []
#     for n in range(3,8):
#         for k in range(3,8):
#             if expectedSize(n, k) > 200:
#                 continue
# #             if n != 6 or k != 6:
# #                 continue
# #             print "n:",n,"k:",k
#             perms = generalizedGreedy(n, k, funcTuple, orderTuple)
#             permList.append(perms)
# #             print len(perms), expectedSize(n, k)
# #             for i in stringify(perms):
# #                 print i
# #             classify(perms, n, k)
#             bools.append(len(perms) == expectedSize(n, k))
#             if not len(perms) == expectedSize(n, k):
#                 print False
#                 return False
# #             print n, k, expectedSize(n, k) - len(perms), len(perms)
# #     print bools
#     print all(bools)
#     return permList
#     print "-----------------------------------------------------------------------------------------------------------------------------------------------------------"

def expectedSize(n,k):
    f = math.factorial
    return f(n) / f(n - k)  


# Try biggest ball and put it into the rightmost bin


# Take the rightmost ball and try to move it to the adjacent right (moving the ball in n - 1 right moves it to 0)
# Does not generate all permutations
def greedy1(n, k):
    if n <= k:
        # Throw error
        return
    if k == 1:
        return [[i] for i in range(n)]
    # The representation is a list of integers with size k where the index is the ball's value and its value is the box the ball belongs to
    first = [i for i in range(k)]
    visited = [list(first)] # Initialized all balls to leftmost positions
    found = True
    while found:
        found = False
        for i in range(1, k + 1):
            guess = list(visited[-1])
            guess[-i] += 1 # Try right
            guess[-i] %= n # If value was n - 1, move to 0
            if guess not in visited and sorted(guess) == list(set(guess)):
                visited.append(list(guess))
                found = True
                break
    return visited  

# Move rightmost balls into leftmost spot
def greedy2(n, k):
    assert (n >= k)
    if k == 1:
        return [[i] for i in range(n)]
    # The representation is a list of integers with size k where the index is the ball's value and its value is the box the ball belongs to
    first = [(k - i) for i in range(1,k + 1)]
    visited = [list(first)] # Initialized all balls to leftmost positions
    found = True
    while found:
        found = False
        for i in range(1, k + 1):
            guess = list(visited[-1])
            orderedBoxes = sorted(list(guess))
            empty = [j for j in range(n) if j not in guess]
            for m in empty:
                index = guess.index(orderedBoxes[-i])
                prev = guess[index]
                guess[index] = m
                if guess not in visited and sorted(guess) == list(set(guess)):
                    visited.append(list(guess))
                    found = True
                    break
                guess[index] = prev
            if found:
                break
    return visited  

# Move maximal ball to leftmost position
def greedy3(n, k):
    assert (n >= k)
    if k == 1:
        return [[i] for i in range(n)]
    # The representation is a list of integers with size k where the index is the ball's value and its value is the box the ball belongs to
    first = [i for i in range(k)]
    visited = [list(first)] # Initialized all balls to leftmost positions
    found = True
    while found:
        found = False
        for i in range(1, k + 1):
            guess = list(visited[-1])
            empty = [j for j in range(n) if j not in guess]
            for m in range(0,len(empty)):
                guess = list(visited[-1])
                guess[-i] = empty[m]
                if guess not in visited and sorted(guess) == list(set(guess)):
                    visited.append(list(guess))
                    found = True
                    break
            if found:
                break
    return visited  

# Move maximal ball to rightmost position
def greedy4(n, k):
    assert (n >= k)
    if k == 1:
        return [[i] for i in range(n)]
    # The representation is a list of integers with size k where the index is the ball's value and its value is the box the ball belongs to
    first = [i for i in range(k)]
    visited = [list(first)] # Initialized all balls to leftmost positions
    found = True
    while found:
        found = False
        for i in range(1, k + 1):
            guess = list(visited[-1])
            empty = [j for j in range(n) if j not in guess]
            for m in range(1,len(empty) + 1):
                guess = list(visited[-1])
                guess[-i] = empty[-m]
                if guess not in visited and sorted(guess) == list(set(guess)):
                    visited.append(list(guess))
                    found = True
                    break
            if found:
                break
    return visited

# Recursive formula to check <A greedy formula>. TO BE WRITTEN AND THOUGHT OF         

# Swap balls the farthest apart going left to right 
def maxGap(n,k):
    assert(n == k)
    first = [i for i in range(n)]
    visited = [list(first)] # Initialized all balls in order
    found = True
    while found:
        found = False
        q = Queue.PriorityQueue()
        for i in range(n):
            for j in range(i + 1, n):
                guess = list(visited[-1])
                temp = guess[i]
                guess[i] = guess[j]
                guess[j] = temp
                q.put((-min(i + n - j,j - i),guess))
        while not q.empty():
            guess = list(q.get()[1])
            if guess not in visited and sorted(guess) == list(set(guess)):
                visited.append(list(guess))
                found = True
                break
    return visited  

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
    return greedy1(n, k) == recursive(n, k)
    
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

# if __name__ == "__main__":
    #for n in range(2,8):
        #for k in range(2,8):
            #if k < n:
                #test(n,k)
#     test(4,4)
    #test(5,2, start)
    #bools = []
    #for n in range(1,8):
    #    for k in range(1,6):
    #        x = check(n, k)
    #        bools.append(x)
    #print all(bools)