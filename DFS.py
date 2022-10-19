import Utility as u
import Node as n

def dfs(intial_state):
    frontier = []
    initial_node = n.Node(int(intial_state), [int(intial_state)], 0)
    frontier.append(initial_node)
    explored = set()
    nodes_expanded = 0
    depth = 0
    while frontier:
        node = frontier.pop()
        state = node.puzzleorder
        path = node.path
        depth = max(depth, len(path)-1)

        if not state in explored:
            explored.add(state)
            nodes_expanded += 1

        if u.goal_state(state):
            return True, path, depth, nodes_expanded

        neighbors = u.moves(state)
        for neighbor in neighbors:
            if neighbor not in explored:
                neighbor_path = path.copy()
                neighbor_path.append(neighbor)
                neighbor_state = n.Node(neighbor, neighbor_path, node.cost+1)
                frontier.append(neighbor_state)

    return False

print(dfs("125340678"))