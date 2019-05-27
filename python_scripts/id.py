
# id = indistinguishable balls, distinguishable boxes, (without num balls constraints)
import math

def test(n, k, first = []):
    print "ALGORITHM To1"
    print "n:",n,"k:",k
    perms = greedy_to1(n, k, first)
    print len(perms), expectedSize(n, k) 
#     for i in stringify(perms):
#         print i
    classify(perms, n, k)
    dif = expectedSize(n, k) - len(perms)
#     print dif
    correct = dif == 0
#     print "Correct:", correct
    if not correct:
        print dif
#     if correct:
#         print first    
#     print "----------------------------"
    return correct
    
def expectedSize(n, k):
    f = math.factorial
    return f(n + k - 1) / (f(k) * f(n - 1))
# Returns all k-ary strings of length n in array format
def greedy1(n, k): # Moves a ball in the rightmost box to the closest box
    # The representation is a list of integers with size n where the index is the box's value and its value is the number of balls it contains
    first = [0] * (n - 1) + [k] # Initialized all balls to the last box
    visited = [list(first)]
    found = True
    while found:
        found = False
        for i in range(1, n + 1):
            guess = list(visited[-1])
            for j in range(1, n):
                guess = list(visited[-1])
                if guess[-i] > 0:
                    guess[-i] -= 1 # Remove ball from rightmost box
                    if i + j <= n:
                        guess[-i - j] += 1 # Add ball to nearest box trying left before right
                        if guess in visited:
                            guess[-i - j] -= 1
                            guess[-i + j] += 1
                    elif i - j > 0:
                        guess[-i + j] += 1
                    else: 
                        continue
                    if guess not in visited:
                        visited.append(list(guess))
                        found = True
                        break
            if found:
                break
    return visited

def greedyR(n, k, first = []): # Move ball from rightmost box to next rightmost box
    # The representation is a list of integers with size n where the index is the box's value and its value is the number of balls it contains
    if first == []:
        first = [0] * (n - 1) + [k] # Initialized all balls to the last box 
    visited = [list(first)]
    found = True
    while found:
        found = False 
        for i in range(1, n + 1):
            guess = list(visited[-1])
            for j in range(1, n + 1):
                guess = list(visited[-1])
                if guess[-i] > 0:
                    guess[-i] -= 1
                    guess[-j] += 1
                if guess not in visited:
                    visited.append(list(guess))
                    found = True
                    break
            if found:
                break
    return visited

def greedy2(n, k): # Moves a ball from box with the least balls (smallest value) to the closest box
    # The representation is a list of integers with size n where the index is the box's value and its value is the number of balls it contains
    first = [0] * (n - 1) + [k] # Initialized all balls to the last box
    # Tried first = [k] + [0] * (n - 1) which resulted in lower success rate
    visited = [list(first)]
    found = True
    while found:
        found = False
        for i in range(n):
            guess = list(visited[-1])
            numBalls = sorted(guess)[i]
            indices = [n - ind for ind, val in enumerate(guess) if val == numBalls]
            for index in indices:
                for j in range(1, n):
                    guess = list(visited[-1])
                    if guess[-index] > 0:
                        guess[-index] -= 1 # Remove ball from least box
                        if index + j <= n:
                            guess[-index - j] += 1 # Add ball to nearest box trying left before right
                            if guess in visited:
                                guess[-index - j] -= 1
                                guess[-index + j] += 1
                        elif index - j > 0:
                            guess[-index + j] += 1
                        else:
                            continue
                        if guess not in visited:
                            visited.append(list(guess))
                            found = True
                            break
                if found:
                    break
            if found:
                break
    return visited

def greedy3(n, k, first=[]): # Move ball from bin with least balls to bin with most balls (CLOSE)
    # The representation is a list of integers with size n where the index is the box's value and its value is the number of balls it contains
    if len(first) != n:
        first = [0] * (n - 1) + [k] # Initialized all balls to the last box
    # Tried first = [k] + [0] * (n - 1) which resulted in lower success rate
    visited = [list(first)]
    found = True
    while found:
        found = False
        for i in range(n):
            guess = list(visited[-1])
            numBalls = sorted(guess)[i]
            minIndices = [ind for ind, val in enumerate(guess) if val == numBalls]
            for minIndex in minIndices:
                guess = list(visited[-1])
                for j in range(1, n + 1):
                    guess = list(visited[-1])
                    numBalls = sorted(guess)[-j]
                    maxIndices = [ind for ind, val in enumerate(guess) if val == numBalls]
                    for maxIndex in maxIndices:
                        guess = list(visited[-1])
                        if guess[minIndex] > 0:
                            guess[minIndex] -= 1
                            guess[maxIndex] += 1
                        if guess not in visited:
                            visited.append(list(guess))
                            found = True
                            break
                    if found:
                        break
                if found:
                    break
            if found:
                break
    return visited

def greedy4(n, k): # Move ball from bin with most balls to bin with next most balls
    # The representation is a list of integers with size n where the index is the box's value and its value is the number of balls it contains
    first = [0] * (n - 1) + [k] # Initialized all balls to the last box 
    visited = [list(first)]
    found = True
    while found:
        found = False
        for i in range(1, n + 1):
            guess = list(visited[-1])
            numBalls = sorted(guess)[-i]
            maxIndices = [ind for ind, val in enumerate(guess) if val == numBalls]
            for maxIndex in maxIndices:
                guess = list(visited[-1])
                for j in range(1, n + 1):
                    guess = list(visited[-1])
                    numBalls = sorted(guess)[-j]
                    maxIndices2 = [ind for ind, val in enumerate(guess) if val == numBalls]
                    for maxIndex2 in maxIndices2:
                        guess = list(visited[-1])
                        if guess[maxIndex] > 0:
                            guess[maxIndex] -= 1
                            guess[maxIndex2] += 1
                        if guess not in visited:
                            visited.append(list(guess))
                            found = True
                            break
                    if found:
                        break
                if found:
                    break
            if found:
                break
    return visited

def greedy5(n, k): # Move ball from box with least balls to rightmost box
    # The representation is a list of integers with size n where the index is the box's value and its value is the number of balls it contains
    first = [0] * (n - 1) + [k] # Initialized all balls to the last box 
    visited = [list(first)]
    found = True
    while found:
        found = False
        for i in range(1,n+1):
            guess = list(visited[-1])
            numBalls = sorted(guess)[-i]
            maxIndices = [ind for ind, val in enumerate(guess) if val == numBalls]
            for maxIndex in maxIndices:
                for j in range(1, n + 1):
                    guess = list(visited[-1])
                    if guess[maxIndex] > 0:
                        guess[maxIndex] -= 1
                        guess[j-1] += 1
                    if guess not in visited:
                        visited.append(list(guess))
                        found = True
                        break
                if found:
                    break
            if found:
                break
    return visited

def greedy6(n, k): # Reversed tries of greedy5 (Rightmost to least)
    # The representation is a list of integers with size n where the index is the box's value and its value is the number of balls it contains
    first = [0] * (n - 1) + [k] # Initialized all balls to the last box
    #first = [k] + [0] * (n - 1) 
    visited = [list(first)]
    found = True
    while found:
        found = False
        for i in range(1, n + 1):
            guess = list(visited[-1])
            for j in range(1, n + 1):
                numBalls = sorted(guess)[j - 1]
                maxIndices = [ind for ind, val in enumerate(guess) if val == numBalls]
                for maxIndex in maxIndices:
                    guess = list(visited[-1])
                    if guess[-i] > 0:
                        guess[maxIndex] += 1
                        guess[-i] -= 1
                    if guess not in visited:
                        visited.append(list(guess))
                        found = True
                        break
                if found:
                    break
            if found:
                break
    return visited


# Select box to move TO first, rather than box to move FROM first

def greedy_to1(n, k, first = []): # Moves ball to rightmost box from ball from the closest box
    # The representation is a list of integers with size n where the index is the box's value and its value is the number of balls it contains
    if first == []:
        first = [0] * (n - 1) + [k] # Initialized all balls to the last box
    visited = [list(first)]
    found = True
    while found:
        found = False
        for i in range(1, n + 1):
            guess = list(visited[-1])
            for j in range(1, n):
                guess = list(visited[-1])
                guess[-i] += 1 # Add ball to rightmost box
                if i + j <= n and guess[-i - j] > 0:
                    guess[-i - j] -= 1 # Remove ball from left before right
                    if guess in visited and i - j > 0 and guess[-i + j] > 0:
                        guess[-i - j] += 1
                        guess[-i + j] -= 1
                elif i - j > 0 and guess[-i + j] > 0:
                    guess[-i + j] -= 1
                else:
                    continue
                if guess not in visited:
                    visited.append(list(guess))
                    found = True
                    break
            if found:
                break
    return visited

def backTracking(n, k):
    print n, k

def classify(perms, n, k):
    restrictive = True
    gray = True
    for i in range(len(perms) - 1):
        changed = False
        changed2 = False
        for j in range(len(perms[i])):
            s = abs(perms[i][j] - perms[i + 1][j])
            if s > 1:
                restrictive = False
            elif s > 0:
                if not changed:
                    changed = True
                elif not changed2:
                    changed2 = True
                else:
                    gray = False
                    break
    print "Restrictive:", restrictive
    print "Gray:", gray
    print "Correct:", len(perms) == expectedSize(n, k)
    
def stringify(perms):
    ret = []
    for i in perms:
        p = ""
        for j in i:
            p += str(j)
        ret.append(p)
    return ret

if __name__ == "__main__":
#     print expectedSize(6, 8)
#     incorrect = [(4,6),(4,7),(4,8),(5,5),(6,5),(6,6),(6,7),(6,8),(7,3),(7,7),(7,8),(8,4),(8,5),(8,6),(8,7)]
#     for j in incorrect:
#         print j
#         arr = greedy3(j[0], j[1])
#         incorrect = ()
#         print "done"
#         for i in arr:    
#             test(j[0], j[1],i)
    bools = []
    for n in range(1,9):
        for k in range(1,9):
            #first = [k] + [0] * (n - 1)
            bools.append(test(n, k))  
    print bools
    print all(bools)