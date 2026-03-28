import time
import random
from problems import is_valid, get_neighbors, manhattan_distance, GRID_SIZE

# Random Agent

class RandomAgent:
    """
    In this a random agent act as a robot just picks a random neighboring cells at each step using random.choice().
    """
 
    def __init__(self, max_steps=200):
        self.max_steps = max_steps
 
    def solve(self, start, goal):
        start_time = time.time()
 
        current = start
        path    = [current]
        steps   = 0
 
        while current != goal and steps < self.max_steps:
            neighbors = get_neighbors(current)
            choices = [(r, c) for (r, c, move) in neighbors if move != "WAIT"]
            if not choices:
                break
            current = random.choice(choices)
            path.append(current)
            steps += 1
 
        time_taken = time.time() - start_time
        solved     = (current == goal)
 
        return path, steps, round(time_taken, 6), solved

# Min-Conflicts Local Search
 
class MinConflictsAgent:
    """
    In this we use Min-Conflicts heuristic to find a path from start to goal.
    """
 
    def __init__(self, max_iterations=500):
        self.max_iterations = max_iterations
 
    def solve(self, start, goal):
        start_time = time.time()
 
        best_path   = None
        best_steps  = float("inf")
 
        # In case if it get's struck the it will try multiple times.
        for attempt in range(self.max_iterations):
            path   = [start]
            visited = {start}
            current = start
            stuck   = False
 
            while current != goal and len(path) <= GRID_SIZE * GRID_SIZE:
                # unvisited valid neighbors
                neighbors = []
                for (r, c, move) in get_neighbors(current):
                    if (r, c) not in visited:
                        dist = manhattan_distance((r, c), goal)
                        neighbors.append(((r, c), dist))
 
                if not neighbors:
                    stuck = True
                    break

                neighbors.sort(key=lambda x: x[1] + random.uniform(0, 0.5))
                next_cell = neighbors[0][0]
                current = next_cell
                path.append(current)
                visited.add(current)
 
            # Checking if this attempt succeeded :)
            if not stuck and current == goal:
                if len(path) - 1 < best_steps:
                    best_steps = len(path) - 1
                    best_path  = path
                break
 
        time_taken = time.time() - start_time
 
        if best_path is None:
            best_path  = [start]
            best_steps = 0
            solved     = False
        else:
            solved = True
 
        return best_path, best_steps, round(time_taken, 6), solved
