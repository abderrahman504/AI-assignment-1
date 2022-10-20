


def swap(str, pos1, pos2):
    str = list(str)
    str[pos1], str[pos2] = str[pos2], str[pos1]
    return int(''.join(str))

def moves(state):
    state = str(state)
    if len(state) == 8:
        state = "0" + state
    zero_position = state.find("0")
    states = []
    if (zero_position + 1) < 9 and (zero_position + 1) % 3 != 0:
        right = swap(state[:], zero_position, zero_position + 1)
        states.append(right)

    if zero_position - 1 > -1 and zero_position % 3 != 0:
        left = swap(state[:], zero_position, zero_position - 1)
        states.append(left)


    if zero_position + 3 < 9:
        down = swap(state[:], zero_position, zero_position + 3)
        states.append(down)

    if zero_position - 3 > -1:
        up = swap(state, zero_position, zero_position - 3)
        states.append(up)
    return states

def goal_state(state):
    if state == 12345678:
        return True
    return False



class State:
	#int whose digits represent the current state of the problem.
	_state: int = 102345678

	#Constructor for a Problem object. It is called with a string representing the initial state of the problem.
	def __init__(self, initial_state: str) -> None:
		integer = int(initial_state)
		self._state = integer

	#Defined for easily printing the state of a problem
	def __str__(self) -> str:
		return self.get_state()
	#Defined so State objects can be used in dicts and sets.
	def __hash__(self) -> int:
		return self._state.__hash__()
	#Returns a copy of this State object.
	def copy(self):
		return State(self.get_state())

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

	def get_child_states(self) -> list:
		children: list = []
		move = self.move_north()
		if move != None: children.append(move)
		
		move = self.move_south()
		if move != None: children.append(move)
		
		move = self.move_east()
		if move != None: children.append(move)
		
		move = self.move_west()
		if move != None: children.append(move)
		return children


class Node:
	_value: State
	_parent: State

	def __init__(self, value, parent):
		self._value = value
		self._parent = parent
	
	def get_value(self):
		return self._value.copy()
	
	def get_parent(self):
		return self._parent.copy()

