# Class for queue entry used in BFS
class QueueEntry:
    def __init__(self, v=0, dist=0):
        self.v = v      # vertex number
        self.dist = dist  # distance from source

def getMinDiceThrows(moves, N):
    # Visited array
    visited = [False] * N

    # BFS queue
    queue = []

    # Start from vertex 0
    visited[0] = True
    queue.append(QueueEntry(0, 0))

    while queue:
        qe = queue.pop(0)
        v = qe.v

        # If reached the last cell
        if v == N - 1:
            return qe.dist

        # Try all next positions from current cell (v)
        for j in range(v + 1, min(v + 7, N)):
            if not visited[j]:
                visited[j] = True
                # Check for snake or ladder
                next_v = moves[j] if moves[j] != -1 else j
                queue.append(QueueEntry(next_v, qe.dist + 1))

    return -1  # if unreachable

# Driver code
if __name__ == "__main__":
    N = 30
    moves = [-1] * N

    # Ladders
    moves[2] = 21
    moves[4] = 7
    moves[10] = 25
    moves[19] = 28

    # Snakes
    moves[26] = 0
    moves[20] = 8
    moves[16] = 3
    moves[18] = 6

    result = getMinDiceThrows(moves, N)
    print("Min Dice throws required is", result)
