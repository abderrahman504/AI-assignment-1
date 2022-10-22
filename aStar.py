from cmath import sqrt
from queue import PriorityQueue
from Utility import State
import time

heuristic_mode: int = 1
MANHATTEN_MODE = 1
EUCLIDEAN_MODE = 2


class PQWrapper:
	_priority: int
	_value = None

	def __init__(self, priority: int, value) -> None:
		self._priority = priority
		self._value = value
	
	def __eq__(self, __o: object) -> bool:
		return self._priority == __o.priority

	def __lt__(self, __o) -> bool:
		return self._priority < __o._priority
	
	def get_value(self):
		return self._value


#Solves the given problem with the given heuristic. Returns info about the solution, or None if no solution exists.
def solve(problem: int, mode: int) -> tuple:
	timeStart: float = time.time()
	heuristic_mode = mode
	searchDepth = 0
	expandedNodes: int = 0
	openList: PriorityQueue = PriorityQueue()
	closedList: dict = {}
	goal_found: bool = False
	goal: State
	root: State = State(problem)
	goalCost: int
	
	#Add the initial state (root) to openList.
	openList.put(PQWrapper(0 + find_heuristic(root), root))
	#Explores the open list until the goal is found or openList is empty
	while not openList.empty():
		checking: State = openList.get().get_value()
		searchDepth = checking.get_cost() if checking.get_cost() > searchDepth else searchDepth
		if checking.is_goal(): 
			goal_found = True
			goal = checking
			break;
		#Expanding checking and adding it's children to openList
		for i in checking.get_child_states():
			childCost = checking.get_cost() + 1
			if i in closedList: 
				continue
			newState: State = State(i, childCost, checking)
			h = find_heuristic(newState)
			openList.put(PQWrapper(childCost + h, newState))
		closedList[int(checking.get_state())] = checking
		expandedNodes += 1

	if not goal_found:
		print("Couldn't solve problem")
		return False, 
	
	timeEnd: float = time.time()
	#Return Whatever The GUI wants (path, search depth, number of expanded nodes)
	return True, goal.get_path(), goal.get_cost(), searchDepth, expandedNodes, timeEnd - timeStart
	

#Finds the heuristic based on the type of A* search
def find_heuristic(state: State) -> float:
	h: int = 0
	string: str = state.get_state()
	for digitPos in range(len(string)):
		digit: int = int(string[digitPos])
		xy1: tuple = digitPos % 3, digitPos // 3 
		xy2: tuple = digit % 3, digit // 3
		if heuristic_mode == MANHATTEN_MODE:
			h += get_manhatten_dis(xy1, xy2)
		
		else:
			h += get_euclidean_dis(xy1, xy2)
	
	return h


def get_manhatten_dis(loc1: tuple, loc2: tuple) -> int:
	return abs(loc1[0] - loc2[0]) + abs(loc1[1] - loc2[1])


def get_euclidean_dis(loc1: tuple, loc2: tuple) -> float:
	return sqrt((loc1[0] - loc2[0])^2 + (loc1[1] - loc2[1])^2)


