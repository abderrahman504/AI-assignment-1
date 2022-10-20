# AI-assignment-1


### State class
This is a class intended to be used to store the states of the problem when using any search algorithms.

#### Methods

###### copy()
Create a copy of State.

###### get_state()
Return a string representing the state of the problem.

###### get_zero_pos()
Return a tuple of the position of the zero block in the format (row number, column number)

###### is_gloal()
Returns True if state is the goal, and False otherwise.

###### get_child_states()
Return a list of all the possible next states.

###### move_north()
Return a State object with a new state after moving north, or None if moving north isn't possible. 

###### move_south()
Return a State object with a new state after moving south, or None if moving south isn't possible.

###### move_east()
Return a State object with a new state after moving east, or None if moving east isn't possible.

###### move_west()
Return a State object with a new state after moving west, or None if moving west isn't possible.

### Node class
Should be used to form the search tree.
Should be constructed with a value and a parent. Both value and parent must be State objects.

#### Methods

###### get_parent()
Returns the parent of the node.

###### get_value()
Returns the value of the node.
