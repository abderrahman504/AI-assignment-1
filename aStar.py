from cmath import sqrt
from queue import PriorityQueue
from Utility import State
import time

heuristic_mode: int = 1 #Determines which heuristic function to be used by A*.
MANHATTEN_MODE = 1	
EUCLIDEAN_MODE = 2

#A Wrapper class to be used with the priority queue
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
def solve(problem: int, heuristic: int) -> tuple:
	timeStart: float = time.time() #Start time of execution
	heuristic_mode = heuristic
	searchDepth = 0 #Maximum search depth in the search tree
	expandedNodes: int = 0 #Number of expanded nodes
	openList: PriorityQueue = PriorityQueue() #Contains all states that await checking.
	closedList: dict = {} #Contains all states that have been checked and expanded.
	goal_found: bool = False #Used to check if the A* was successful in finding a solution.
	goal: State	#The goal state
	root: State = State(problem) #The initial state
	
	#Add root to openList.
	openList.put(PQWrapper(0 + find_heuristic(root), root))
	#Explores the open list until the goal is found or openList is empty
	while not openList.empty():
		checking: State = openList.get().get_value()
		#If this depth is larger that the previous largest depth then update searchDepth
		searchDepth = checking.get_cost() if checking.get_cost() > searchDepth else searchDepth
		expandedNodes += 1
		
		if checking.is_goal(): #If the current state is the goal then exit the loop  
			goal_found = True
			goal = checking
			break;
		#Expanding the current state and adding it's children to openList
		for i in checking.get_child_states():
			childCost = checking.get_cost() + 1
			if i in closedList: #Don't add a child if it's already visited. 
				continue
			newState: State = State(i, childCost, checking)
			h = find_heuristic(newState)
			openList.put(PQWrapper(childCost + h, newState))
		#Add the current state to the closed list
		closedList[int(checking.get_state())] = checking 

	if not goal_found:
		print("Couldn't solve problem")
		return False, 
	
	timeEnd: float = time.time() #The end time of execution
	return True, goal.get_path(), goal.get_cost(), searchDepth, expandedNodes, timeEnd - timeStart
	

#Finds the heuristic based on the type of A* search
def find_heuristic(state: State) -> float:
	h: float = 0
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

#Gets the manhattan distance between to locations on the puzzle
def get_manhatten_dis(loc1: tuple, loc2: tuple) -> float:
	return abs(loc1[0] - loc2[0]) + abs(loc1[1] - loc2[1])

#Gets the euclidean distance between to locations on the puzzle
def get_euclidean_dis(loc1: tuple, loc2: tuple) -> float:
	return sqrt((loc1[0] - loc2[0])^2 + (loc1[1] - loc2[1])^2)


