from heapq import heappush, heappop

# Calculate Manhattan Distance
def heuristic(state, goal):
    distance = 0
    for i in range(9):
        if state[i] != 0:
            j = goal.index(state[i])
            distance += abs(i//3 - j//3) + abs(i%3 - j%3)
    return distance

# Generate possible moves
def get_moves(state):
    moves = []
    pos = state.index(0)
    r, c = pos//3, pos%3

    for dr, dc in [(-1,0), (1,0), (0,-1), (0,1)]:
        nr, nc = r+dr, c+dc
        if 0 <= nr < 3 and 0 <= nc < 3:
            new = state[:]
            new[pos], new[nr*3+nc] = new[nr*3+nc], new[pos]
            moves.append(new)

    return moves

# A* Search Algorithm
def astar(start, goal):
    pq = []
    heappush(pq, (heuristic(start, goal), 0, start))
    visited = set()

    while pq:
        f, g, state = heappop(pq)

        if state == goal:
            print("Solution found:", state)
            return

        if tuple(state) in visited:
            continue
        visited.add(tuple(state))

        print(state[:3])
        print(state[3:6])
        print(state[6:])
        print()

        for new in get_moves(state):
            if tuple(new) not in visited:
                heappush(pq, (g+1+heuristic(new, goal), g+1, new))

    print("No solution found")

# Main Program
start = [1, 2, 3,
         4, 0, 6,
         7, 5, 8]

goal = [1, 2, 3,
        4, 5, 6,
        7, 8, 0]

astar(start, goal)