import Utility as u
import time
def bfs(intial_state):
    start_time = time.time()
    queue = []
    queue.append(u.State(intial_state, 0))
    explored = set()
    max_depth = 0
    while queue:
        state = queue.pop(0)
        puzzle_order = int(state.get_state())
        depth = state.get_cost()
        max_depth = max(depth, max_depth)
        if not puzzle_order in explored:
            explored.add(puzzle_order)

        if state.is_goal():
            return True, state.get_path(), depth, len(explored), time.time() - start_time

        neighbors = state.get_child_states()
        for neighbor in neighbors:
            if neighbor not in explored:
                neighbor_state = u.State(neighbor, depth + 1, state)
                queue.append(neighbor_state)

    return False, [], depth, len(explored), time.time() - start_time

