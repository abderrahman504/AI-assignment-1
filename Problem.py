import copy


class Problem:
	#2D list that stores the current state of the problem. Default value is a sovled problem.
	_state: list = [
	[0,1,2],
	[3,4,5],
	[6,7,8]
	];

	#Constructor for a Problem object. It is called with a 2D list representing the initial state of the problem.
	def __init__(self, initial_state: list) -> None:

		if not initial_state is list or len(initial_state) != 3:
			print("invalid problem")
			return
		else:
			for item in initial_state:
				if not item is list or len(item) != 3:
					print("invalid problem")
					return
		_state = initial_state


	#Returns a copy of the current state of the problem.
	def get_state(self):
		return self.copy.deapcopy(self._state)

	#Returns a copy of the current position of the zero block 
	def get_zero_pos(self):
		zero_pos = []
		for i in len(self._state):
			for j in len(self._state[i]):
				if self._state[i][j] == 0: 
					zero_pos = [i, j]
		return zero_pos.copy()

	#Tries to move the 0 block to the north. Return True if successfull and False if not.
	def move_north(self):
		if self._zero_pos[0] == 0:
			return False
		
		

	#Tries to move the 0 block to the east. Return True if successfull and False if not.
	def move_east(self):
		if self._zero_pos[1] == 2:
			return False

	#Tries to move the 0 block to the east. Return True if successfull and False if not.
	def move_south(self):
		if self._zero_pos[0] == 2:
			return False

	#Tries to move the 0 block to the east. Return True if successfull and False if not.
	def move_west(self):
		if self._zero_pos[1] == 0:
			return False




myProblem: Problem = Problem(5)
