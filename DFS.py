import Utility as u
import time
from collections import deque

def dfs(intial_state):
    start_time = time.time()
    frontier = deque()
    frontier_map = set()
    frontier.append(u.State(intial_state, 0))
    explored = set()
    max_depth = 0
    while frontier:
        state = frontier.pop()
        puzzle_order = int(state.get_state())
        depth = state.get_cost()
        explored.add(puzzle_order)

        if state.is_goal():
            return True, state.get_path(), max_depth, len(explored), time.time() - start_time

        neighbors = state.get_child_states()

        for neighbor in neighbors:
            if neighbor not in explored and neighbor not in frontier_map:
                neighbor_state = u.State(neighbor, depth + 1, state)
                frontier.append(neighbor_state)
                max_depth = max(depth + 1, max_depth)
                frontier_map.add(neighbor)
    return False, [], max_depth, len(explored), time.time() - start_time

