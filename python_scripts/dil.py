# distinguishable balls, indistinguishable boxes, (at) least one ball in each box
import copy


def test(n, k):
    perms = greedyNeighbors(n, k)
    return perms

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
    n, k = 3,3 
    test(n, k)