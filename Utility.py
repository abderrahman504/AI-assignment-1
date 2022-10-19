
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



