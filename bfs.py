import Utility as u
import time
from collections import deque

def bfs(intial_state):
	start_time = time.time()
	queue = deque()
	queue.append(u.State(intial_state, 0))
	queue_map = set()
	queue_map.add(int(intial_state))
	explored = set()
	max_depth = 0
	while queue:
		state = queue.popleft()
		puzzle_order = int(state.get_state())
		depth = state.get_cost()
		if not puzzle_order in explored:
			explored.add(puzzle_order)

		if state.is_goal():
			return True, state.get_path(), max_depth, len(explored), time.time() - start_time

		neighbors = state.get_child_states()
		for neighbor in neighbors:
			if neighbor not in explored and neighbor not in queue_map:
				neighbor_state = u.State(neighbor, depth + 1, state)
				max_depth = max(max_depth, depth+1)
				queue.append(neighbor_state)
				queue_map.add(neighbor)

	return False, [], max_depth, len(explored), time.time() - start_time
