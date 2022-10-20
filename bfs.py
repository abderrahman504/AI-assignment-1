import Utility as u

import Node as n

import time

def bfs(intial_state):

    start_time = time.time()

    queue = []

    initial_node = n.Node(int(intial_state), [int(intial_state)], 0)

    queue.append(initial_node)

    explored = set()

    nodes_expanded = 0

    depth = 0

    while queue:

        node = queue.popleft()

        state = node.puzzleorder

        path = node.path

        depth = max(depth, len(path)-1)



        if not state in explored:

            explored.add(state)

            nodes_expanded += 1



        if u.goal_state(state):

            return True, path, depth, nodes_expanded , time.time() - start_time



        neighbors = u.moves(state)

        for neighbor in neighbors:

            if neighbor not in explored:

                neighbor_path = path.copy()

                neighbor_path.append(neighbor)

                neighbor_state = n.Node(neighbor, neighbor_path, node.cost+1)

                queue.append(neighbor_state)



    return False, [], depth, nodes_expanded, time.time() - start_time