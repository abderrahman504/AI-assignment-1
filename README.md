# AI-assignment-1


### State class
This is a class intended to be used to store the states of the problem when using any search algorithms.

#### Methods

###### copy()
Create a copy of State.

###### get_state()
Return a string representing the state of the problem.

###### get_zero_pos()
Return index of the zero character in the state string.

###### is_gloal()
Returns True if state is the goal, and False otherwise.

###### get_child_states()
Return a list of all the possible next states as ints.

###### get_path()
Returns a list of State objects that were taken to reach this state.
