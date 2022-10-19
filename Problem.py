import copy



class Problem:
	#int whose digits represent the current state of the problem.
	_state: int = 102345678

	#Constructor for a Problem object. It is called with a string representing the initial state of the problem.
	def __init__(self, initial_state: str) -> None:
		integer = int(initial_state)
		_state = integer

	#Defined for easily printing the state of a problem
	def __str__(self) -> str:
		return self.get_state()

	def __hash__(self) -> int:
		return self._state.__hash__()
	def copy(self):
		return Problem(self.get_state())

	#Returns a string representing the current state of the problem.
	def get_state(self) -> str:
		ret_state = str(self._state)
		if len(ret_state) == 8:
			ret_state = "0" + ret_state
		return ret_state

	#Returns the current position of the zero block in the format (row number, column number).
	def get_zero_pos(self) -> tuple:
		state = self.get_state()
		zero_pos;
		for i in range(3):
			for j in range(3):
				if state[3*i + j] == "0": 
					zero_pos = i, j
		return zero_pos

	"""Transition functions"""

	#Tries to move the 0 block to the north. Returns new state if successfull and None if not.
	def move_north(self):
		if self.get_zero_pos()[0] == 0:
			return None
		old_loc = list(self.get_zero_pos())
		new_loc = list(old_loc)
		new_loc[0] -= 1; #change this in other trans funcs
		new_state = self.get_state()
		new_state[old_loc[0]*3 + old_loc[1]] = new_state[new_loc[0]*3 + new_loc[1]]
		new_state[new_loc[0]*3 + new_loc[1]] = "0"
		return new_state

	#Tries to move the 0 block to the east. Return True if successfull and False if not.
	def move_south(self):
		if self.get_zero_pos[0] == 2:
			return False
		old_loc = list(self.get_zero_pos())
		new_loc = list(old_loc)
		new_loc[0] += 1; #change this in other trans funcs
		new_state = self.get_state()
		new_state[old_loc[0]*3 + old_loc[1]] = new_state[new_loc[0]*3 + new_loc[1]]
		new_state[new_loc[0]*3 + new_loc[1]] = "0"
		return True

	#Tries to move the 0 block to the east. Return True if successfull and False if not.
	def move_east(self):
		if self.get_zero_pos[1] == 2:
			return False
		old_loc = list(self.get_zero_pos())
		new_loc = list(old_loc)
		new_loc[1] += 1; #change this in other trans funcs
		new_state = self.get_state()
		new_state[old_loc[0]*3 + old_loc[1]] = new_state[new_loc[0]*3 + new_loc[1]]
		new_state[new_loc[0]*3 + new_loc[1]] = "0"
		return True

	#Tries to move the 0 block to the east. Return True if successfull and False if not.
	def move_west(self):
		if self.get_zero_pos[1] == 0:
			return False
		old_loc = list(self.get_zero_pos())
		new_loc = list(old_loc)
		new_loc[1] -= 1; #change this in other trans funcs
		new_state = self.get_state()
		new_state[old_loc[0]*3 + old_loc[1]] = new_state[new_loc[0]*3 + new_loc[1]]
		new_state[new_loc[0]*3 + new_loc[1]] = "0"
		return True


