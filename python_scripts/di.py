import copy
# greedy Gray code algorithm found
# di = distinguishable balls, indistinguishable boxes, (no restriction on number of balls in boxes)
def test(x, y, z = None, orderTuple = (2, 1, 0)):
    funcTuple = (z, x, y)
    bools = []
    permList = []
    for n in range(1,7):
        for k in range(1,7):
            if n != k:
                continue
#             if n != 4 or k != 6:
#                 continue
#             if n != 6:
#                 continue
#             print "n:",n,"k:",k
            perms = generalizedGreedy(n, k, funcTuple, orderTuple)
            permList.append(perms)
#             print len(perms), expectedSize(n, k)
#             for i in stringify(perms):
#                 print i
#             classify(perms, n, k)
            bools.append(len(perms) == expectedSize(n, k))
            if not len(perms) == expectedSize(n, k):
                print False
                return False
#             print n, k, expectedSize(n, k) - len(perms), len(perms)
#     print bools
#     print all(bools)
    return permList
#     print "-----------------------------------------------------------------------------------------------------------------------------------------------------------"
 
# Stirling numbers of the second kind
def stirling(n,k):
    if n == 0 or k < 0 or k > n:
        return 0
    if k == n or k == 1:
        return 1
    else:
        return k * stirling(n - 1, k) + stirling(n - 1,k - 1)

# Returns bell number of n = k unless n < k, in which case n is restrained by k
def expectedSize(n, k):
    ret = 0
    for i in range(1, n + 1):
        ret += stirling(k, i)
    return ret

def move(n, k, passedPartition, fromIndex, toIndex, val):
    partition = copy.deepcopy(passedPartition)
    partition[fromIndex] -= frozenset([val])
    partition[toIndex] |= frozenset([val])
    ret = []
    for i in range(k):
        for j in partition:
            if i in list(j) and j not in ret:
                ret.append(j)
    for i in range(len(ret), n):
        ret.append(frozenset([]))
    return ret
    
def generalizedGreedy(n, k, funcTuple, orderTuple):
    first = [frozenset([i for i in range(k)])] + [frozenset([])] * (n - 1)
#     first = [frozenset([i]) for i in range(k)]
    visited = [list(first)]
    possibleMovesTuples = validDeltas(n, k, visited)
    while len(possibleMovesTuples) > 0:
        moveTuple = metaSortDeltas(possibleMovesTuples, funcTuple, orderTuple, n, k, visited[-1])
        visited.append(move(n, k, visited[-1], moveTuple[0], moveTuple[1], moveTuple[2]))
        possibleMovesTuples = validDeltas(n, k, visited)
    return visited
        
def metaSortDeltas(deltas, funcTuple, orderTuple, n, k, guess):
    deltas = leastBalls(list(deltas), 1, n, k, guess)
    for i in orderTuple: # i refers to the index of the function being used in this iteration of the loop
        sort = funcTuple[i]
        if sort is not None:
            deltas = sort(list(deltas), i, n, k, guess)
        for j in enumerate(deltas[:-1]):
            if deltas[j[0]][i] != deltas[j[0] + 1][i]:
                deltas = deltas[:j[0] + 1]
                break
            if len(deltas) == 1:
                break
    return deltas[0]

def validDeltas(n, k, visited): # Gray code set partitions from a given set partition
    partition = visited[-1]
    ret = []
    for fromIndex, fromBox in enumerate(partition):
        for toIndex in range(len(partition)):
            for ball in list(fromBox):
                if fromIndex != toIndex and ball in partition[fromIndex]:
                    guess = move(n, k, partition, fromIndex, toIndex, ball)
                    if guess not in visited + ret:
                        ret.append((fromIndex, toIndex, ball))
    return ret

def smallestBall(deltas, funcIndex, n, k, guess): # EQUIVALENT TO NO SORTING | Selects box with smallest ball or smallest ball itself
    return sorted(deltas, key = lambda element: element[funcIndex])
        
def biggestBall(deltas, funcIndex, n, k, guess): # Selects box with biggest ball or biggest ball itself
    return sorted(deltas, key = lambda element: element[funcIndex], reverse = True) # Rightmost box, not biggest ball box
    
def leastBalls(deltas, funcIndex, n, k, guess): # Selects box with least balls
    sortedGuess = sorted(enumerate(guess), key = lambda box: len(box[1]))
    ret = []
    for i in sortedGuess:
        for j in deltas:
            if j[funcIndex] == i[0]:
                ret.append(j)
    return ret
    
def mostBalls(deltas, funcIndex, n, k, guess): # Selects box with most balls
    sortedGuess = sorted(enumerate(guess), key = lambda box: len(box[1]), reverse = True)
    ret = []
    for i in sortedGuess:
        for j in deltas:
            if j[funcIndex] == i[0]:
                ret.append(j)
    return ret

def closestBox(deltas, funcIndex, n, k, guess): # Selects box closest to box already selected
    assert funcIndex in [0, 1]
    selectedIndex = deltas[0][1 - funcIndex] # Switches 0 and 1 to 1 and 0 respectively
    return sorted(deltas, key = lambda element: abs(element[funcIndex] - selectedIndex))
    
def farthestBox(deltas, funcIndex, n, k, guess):
    assert funcIndex in [0, 1]
    selectedIndex = deltas[0][1 - funcIndex] # Switches 0 and 1 to 1 and 0 respectively
    return sorted(deltas, key = lambda element: abs(element[funcIndex] - selectedIndex), reverse = True)

def adjacentLeftBox(deltas, funcIndex, n, k, guess):
    print 1

def classify(perms, n, k):
    gray = True
    for index, value in enumerate(perms[:-1]):
        value = set(value)
        a = set(perms[index + 1])
        b = set(value) 
        if len(a ^ b) > 4:
            gray = False
            break
        a_vals = set([])
        for i in (a | b) - b:
            for j in i:
                a_vals.add(j)
        b_vals = set([])
        for i in (a | b) - a:
            for j in i:
                b_vals.add(j)
        gray = a_vals == b_vals
    if not gray:
        print "NOT GRAY"
        print "||||||||||||||||||||||||||||||||||||||||"
        print "NOT GRAY"
    print "Correct:", len(perms) == expectedSize(n, k)
    
def classifyRGS(strings):
    perms = []
    for i in strings:
        perms.append([int(j) for j in list(i)])
    gray = True
    for i in range(len(perms) - 1):
        changed = False
        for j in range(len(perms[i])):
            s = abs(perms[i][j] - perms[i + 1][j]) 
            if s > 0:
                if not changed:
                    changed = True
                else:
#                     print perms[i], perms[i + 1]
                    gray = False
                    break
#     print "Gray:", gray
    return gray
    
def stringify(perms):
    ret = copy.deepcopy(perms)
    for i in ret:
        for j in enumerate(i):
            newj = frozenset([])
            for k in j[1]:
                newj |= frozenset([k + 1])
            i[j[0]] = list(newj)
#             i[j[0]] = list(j[1])
    return ret

def RGS(l):
    rgs = {}
    for i, part in enumerate(l):
        for j in part:
            rgs[j] = i
    t = tuple([rgs[i] for i in sorted([i for p in l for i in p])])
    s = ""
    for i in t:
        s += str(i)
    return s        

def recursive(n, k):
    if n > k:
        n = k
    if n == 1:
        return [[range(1, k + 1)]]
    sequence = []
    for parity, partition in enumerate(recursive(n, k - 1)):
        if parity % 2 == 0:
            for i, box in enumerate(partition):
                box.append(k)
                sequence.append(partition[:i] + [list(box)] + partition[i + 1:])
                box.remove(k)
            if len(partition) < n:
                sequence.append(partition + [[k]])
        else:
            if len(partition) < n:
                sequence.append(partition + [[k]])
            partition.reverse()
            for i, box in enumerate(partition):
                box.append(k)
                sequence.append(list(reversed(partition[i + 1:])) + [list(box)] + list(reversed(partition[:i])))
                box.remove(k)
    return sequence
    
def indexOfBall(partition, ball):
    for index, box in enumerate(partition):
        if ball in box:
            return index
    
def fix(partition):
    partition.sort()
    while [] in partition:
        partition.remove([])
    
def greedyNeighbors(n, k): # Moves biggest ball to its own box if it were to be adjacent or the currently adjacent box
    if n > k:
        n = k
    visited = [[range(1, k + 1)]]
    nextPartitionFound = True
    while nextPartitionFound:
        nextPartitionFound = False
        for i in range(k):
            bigBall = k - i
            previousPartition = copy.deepcopy(visited)[-1]
            bigBallIndex = indexOfBall(list(previousPartition), bigBall)
            previousPartition[bigBallIndex].remove(bigBall)
            if len(visited[-1]) < n:
                # try new adjacent box
                guess = previousPartition[:bigBallIndex] + [[bigBall]] + previousPartition[bigBallIndex:]
                fix(guess)
#                 print "New box", guess
                if abs(bigBallIndex - indexOfBall(list(guess), bigBall)) == 1 and guess not in visited:
                    visited.append(guess)
                    nextPartitionFound = True
                    break
            # try left adjacent box
            if bigBallIndex > 0:
                guess = list(previousPartition)
                guess[bigBallIndex - 1].append(bigBall)
                guess[bigBallIndex - 1].sort()
                fix(guess)
#                 print "Left adjacent", guess
                if guess not in visited:
                    visited.append(guess)
                    nextPartitionFound = True
                    break
                if bigBall in guess[bigBallIndex - 1]:
                    guess[bigBallIndex - 1].remove(bigBall)
                # try right adjacent box
            if bigBallIndex + 1 < len(previousPartition):
                guess = list(previousPartition)
                guess[bigBallIndex + 1].append(bigBall)
                guess[bigBallIndex + 1].sort()
                fix(guess)
#                 print "Right adjacent", guess
                if guess not in visited:
                    visited.append(guess)
                    nextPartitionFound = True
                    break
    return visited

if __name__ == "__main__":
    bools = []
#     sizebools = []
    for n in range(1, 8):
        for k in range(1, 8):
#             if expectedSize(n, k) > 500:
#                 continue
            if n != k:
                continue
            perms = recursive(n, k)
#             perms2 = greedyNeighbors(n, k)
#             bools.append(perms == perms2)
            print perms[-1]
#             print n, k, bools[-1]
#             sizebools.append(len(perms) == expectedSize(n, k))
#     print all(bools)
#     print all(sizebools)
#     for i in recursive(3, 5):
#         print i
#     for i in enumerate(greedyNeighbors(3, 5)):
#         print i[1], recursive(3, 5)[i[0]]
#     print len(greedyNeighbors(3, 5)), len(recursive(3, 5)), expectedSize(3, 5)
#     brek = False
#     names = []
#     perms = []
#     fromNames = ["box with smallest ball (leftmost box)", "box with biggest ball (rightmost box)", "box with least balls", "box with most balls", "closest box to the box moved to", "farthest box to the box moved to"]
#     toNames = ["box with smallest ball (leftmost box).", "box with biggest ball (rightmost box).", "box with least balls.", "box with most balls.", "closest box to the box moved from.", "farthest box to the box moved from."]
#     ballNames = ["smallest ball", "biggest ball"]
#     fromFunctions = [smallestBall, biggestBall, leastBalls, mostBalls, closestBox, farthestBox]
#     toFunctions = [smallestBall, biggestBall, leastBalls, mostBalls, closestBox, farthestBox]
#     ballFunctions = [smallestBall, biggestBall]
#     for i in stringify(test(closestBox, biggestBall)[3]):
#         print i
#     for i in recursive(4, 4):
#         print i
#     print "--"
#     for i in stringify(test(smallestBall, biggestBall)[3]):
#         print i
#     print "--"
#     print recursive(4, 4) == test(smallestBall, biggestBall)[3]
#     for i in stringify(test(smallestBall, biggestBall)[3]):
#         print i
#     print "--"
#     for i in recursive(4):
#         print i
#     for i in range(3,6):
#         print stringify(test(smallestBall, biggestBall)[i]) == recursive(i + 1)
#     for i in range(len(fromFunctions)):
#         for j in range(len(toFunctions)):
#             for k in range(len(ballFunctions)):
# #                 print "From the",fromNames[i],"move the",ballNames[k],"to the",toNames[j]
#                 p = test((fromFunctions[i], toFunctions[j], ballFunctions[k]),(2,1,0))
#                 if p not in perms:
#                     perms.append(p)
#                     names.append((toNames[j],ballNames[k]))
#                 print len(perms)
#     for i in range(len(ballFunctions)):
#         test((None))
#     
#     for x, allNK in enumerate(perms):
# #         print x, names[x]
#         bools = []
#         for nk in allNK:
#             strings = []
#             for l in stringify(nk):
# #                 print RGS(l)
#                 strings.append(RGS(l))
#             bools.append(classifyRGS(strings))
#         print bools
#         print all(bools)
#     bigBallLeftBox = perms[7]
#     for i in bigBallLeftBox:
#         strings = []
#         for j in stringify(i):
#             print RGS(j)
#             strings.append(RGS(j))
#         print classifyRGS(strings)
#     funcTuple = (smallestBall, smallestBall, smallestBall)
#     for i in stringify(test(funcTuple,(2,1,0))[0]):
#         print RGS(i)
#     funcTuple = (smallestBall, smallestBall, biggestBall)
#     for i in stringify(test(funcTuple,(2,1,0))[0]):
#         print RGS(i)
#                     print [perms[-1][ind] == perms[-2][ind] for ind, val in enumerate(perms[-1])]
#                 for orderTuple in [(0,1,2),(0,2,1),(1,0,2),(2,1,0)]:
#                     if orderTuple[0] == 0 and (i == closestBox or i == farthestBox):
#                         print "Skip"
#                         continue
#                     if orderTuple[0] == 1 and (j == closestBox or j == farthestBox):
#                         print "Skip"
#                         continue
#                     print "Selecting in order",orderTuple
#                     if test((fromFunctions[i], toFunctions[j], ballFunctions[k]), orderTuple):
#                         workingNames.append(((fromNames[i], toNames[j], ballNames[k]), orderTuple))
#                 print "-----------------------------------------------------------------------------------------------------------------------------------------------------------"
#     test((biggestBall, smallestBall, biggestBall),(2,0,1))