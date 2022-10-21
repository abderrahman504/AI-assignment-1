
class State:
	#int whose digits represent the current state of the problem.
	_state: int = 102345678
	_cost: int
	_parent = None

	#Constructor for a Problem object.
	def __init__(self, initial_state: str, cost: int = 0, parent = None) -> None:
		self._state = int(initial_state)
		self._cost = cost
		self._parent = parent

	def __init(self, initial_state: int, cost: int = 0, parent = None) -> None:
		self._state = initial_state
		self._cost = cost
		self._parent = parent


	#Defined for easily printing the state of a problem
	def __str__(self) -> str:
		return self.get_state()
	
	#Returns a copy of this State object.
	def copy(self):
		return State(self.get_state())

	#Returns the parent of this State, or None if it has no parent.
	def get_parent(self) -> _parent:
		return self._parent

	#Returns the cost of this state
	def get_cost(self) -> int:
		return self._cost


	#Returns the path taken to this state
	def get_path(self) -> list:
		stack: list = []
		current = self
		while current != None:
			stack.append(current.get_state())
			print(current.get_state())
			current = current.get_parent()
			print(current)
		return stack

	#Returns a string representing the current state of the problem.
	def get_state(self) -> str:
		ret_state = str(self._state)
		if len(ret_state) == 8:
			ret_state = "0" + ret_state
		return ret_state

	#Returns the current position of the zero block in the format (row number, column number).
	def get_zero_pos(self) -> tuple:
		state = self.get_state()
		zero_pos: tuple;
		for i in range(3):
			for j in range(3):
				if state[3*i + j] == "0": 
					zero_pos = i, j
		return zero_pos
	
	#Returns true if the current state is the goal, and false otherwise.
	def is_goal(self) -> bool:
		return self._state == 12345678

	"""Transition functions"""

	#Tries to move the 0 block to the north. Returns new state if successfull and None if not.
	def move_north(self):
		if self.get_zero_pos()[0] == 0:
			return None
		old_loc = list(self.get_zero_pos())
		new_loc = list(old_loc)
		new_loc[0] -= 1; #change this in other trans funcs
		
		return self._swap(old_loc, new_loc)
	
	#Tries to move the 0 block to the south. Returns new state if successfull and None if not.
	def move_south(self):
		if self.get_zero_pos()[0] == 2:
			return None
		old_loc = list(self.get_zero_pos())
		new_loc = list(old_loc)
		new_loc[0] += 1; #change this in other trans funcs
		
		return self._swap(old_loc, new_loc)

	#Tries to move the 0 block to the east. Returns new state if successfull and None if not.
	def move_east(self):
		if self.get_zero_pos()[1] == 2:
			return None
		old_loc = list(self.get_zero_pos())
		new_loc = list(old_loc)
		new_loc[1] += 1; #change this in other trans funcs
		
		return self._swap(old_loc, new_loc)

	#Tries to move the 0 block to the west. Returns new state if successfull and None if not.
	def move_west(self):
		if self.get_zero_pos()[1] == 0:
			return None
		old_loc = list(self.get_zero_pos())
		new_loc = list(old_loc)
		new_loc[1] -= 1; #change this in other trans funcs
		
		return self._swap(old_loc, new_loc)

	def _swap(self, pos1, pos2):
		new_state = list(self.get_state())
		temp: str = new_state[pos1[0]*3 + pos1[1]]
		new_state[pos1[0]*3 + pos1[1]] = new_state[pos2[0]*3 + pos2[1]]
		new_state[pos2[0]*3 + pos2[1]] = temp
		return State("".join(new_state))

	#Returns a list of the child states as ints.
	def get_child_states(self) -> list:
		children: list = []

		move = self.move_east()
		if move != None: children.append(int(move.get_state()))

		move = self.move_west()
		if move != None: children.append(int(move.get_state()))

		
		move = self.move_south()
		if move != None: children.append(int(move.get_state()))

		move = self.move_north()
		if move != None: children.append(int(move.get_state()))

		return children



