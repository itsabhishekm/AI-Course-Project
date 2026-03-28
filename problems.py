GRID_SIZE = 8
 
START    = (0, 0)   # Starting point
DROPOFF  = (7, 7)   # Ending point
 
# Pickup point for robot to pick up the items and deliver it back to dropoff point mentioned
PICKUP   = (3, 5)

# Possible moves for robot
MOVES = {
    "UP":    (-1,  0),
    "DOWN":  ( 1,  0),
    "LEFT":  ( 0, -1),
    "RIGHT": ( 0,  1),
    "WAIT":  ( 0,  0),
}

"""
In the below mentioned function we are going check 
 1) Cell is inside the grid boundaries
 2) Understanding the neighbours from the current position
 3) Using heuristic to guide the search ( Manhattan distance between two grid cells)
"""
 
def is_valid(row, col):
    return 0 <= row < GRID_SIZE and 0 <= col < GRID_SIZE
 
 
def get_neighbors(position):
    
    row, col = position
    neighbors = []
 
    for move_name, (dr, dc) in MOVES.items():
        new_row = row + dr
        new_col = col + dc
        if is_valid(new_row, new_col):
            neighbors.append((new_row, new_col, move_name))
 
    return neighbors
 
 
def manhattan_distance(pos1, pos2):
    
    return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])

# Grid
def print_grid(path, pickup=PICKUP, title=""):

    grid = [['.' for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]
    for (r, c) in path:
        grid[r][c] = '*'

    #locations
    sr, sc = START
    pr, pc = pickup
    dr, dc = DROPOFF
    grid[sr][sc] = 'S'
    grid[pr][pc] = 'P'
    grid[dr][dc] = 'D'
 
    # current position
    if path:
        rr, rc = path[-1]
        grid[rr][rc] = 'R'
 
    # grid printing
    if title:
        print(f"\n{'='*30}")
        print(f"  {title}")
        print(f"{'='*30}")
 
    print("    " + "  ".join(str(c) for c in range(GRID_SIZE)))
    print("   " + "---" * GRID_SIZE)
    for r in range(GRID_SIZE):
        row_display = "  ".join(grid[r])
        print(f" {r} | {row_display}")
 
    print()
    print(f"  S = Start location of robot {START}")
    print(f"  P = Pickup location of robot {pickup}")
    print(f"  D = Dropoff location of robot {DROPOFF}")
    print(f"  R = Current position of robot")
    print(f"  * = Path taken to reach the destination")
 

if __name__ == "__main__":
    print("Grid size:", GRID_SIZE, "x", GRID_SIZE)
    print("Start location:", START)
    print("Pickup location:", PICKUP)
    print("Dropoff location:", DROPOFF)
    print("\nNeighbors of (0,0):", get_neighbors((0, 0)))
    print("Manhattan distance from START to PICKUP:", manhattan_distance(START, PICKUP))
    print_grid([START], title="Initial State")