#medium.com/@nicholas.w.swift/easy-a-star-pathfinding-7e6689c7f7b2

class Node():
    """A node class for A* Pathfinding"""

    def __init__(self, parent=None, position=None):
        #Stores parent to find which previous square it links too.
        self.parent = parent
        self.position = position

        self.g = 0
        self.h = 0
        self.f = 0

    #This operator runs in an if a == b for two objects.
    def __eq__(self, other):
        return self.position == other.position


def astar(maze, start, end):
    """Returns a list of tuples as a path from the given start to the given end in the given maze"""
    # Create start and end node
    start_node = Node(None, start)
    start_node.g = start_node.h = start_node.f = 0
    end_node = Node(None, end)
    end_node.g = end_node.h = end_node.f = 0

    # Initialize both open and closed list
    #open list is what we check
    open_list = []
    #closed is what we dont check because it has most efficient route to the nodes in it
    closed_list = []

    # Add the start node
    open_list.append(start_node)

    #A limiter on the nodes checked
    nodesChecked = 0

    # Loop until you find the end
    while len(open_list) > 0 and nodesChecked < 50:
        # Get the current node
        current_node = open_list[0]
        current_index = 0
        for index, item in enumerate(open_list):
            #Get the smallest costing node in the open list.
            if item.f < current_node.f:
                current_node = item
                current_index = index

        # Pop current off open list, add to closed list
        open_list.pop(current_index)
        closed_list.append(current_node)

        # Found the goal
        if current_node == end_node:
            path = []
            current = current_node
            while current is not None:
                path.append(current.position)
                current = current.parent
            return path[::-1] # Return reversed path

        # Generate children. Children are adjacent squares.
        children = []
        for new_position in [(0, -1), (0, 1), (-1, 0), (1, 0)]: # Adjacent squares

            # Get node position
            node_position = (current_node.position[0] + new_position[0], current_node.position[1] + new_position[1])

            # Make sure within map limits
            if node_position[0] > (len(maze) - 1) or node_position[0] < 0 or node_position[1] > (len(maze[len(maze)-1]) -1) or node_position[1] < 0:
                continue

            # Make sure walkable terrain
            if maze[node_position[0]][node_position[1]] != '.' and maze[node_position[0]][node_position[1]] != 'p':
                continue

            # Create new node
            new_node = Node(current_node, node_position)

            # Appends adjacent coordinates for further checking right below after this loop ends.
            children.append(new_node)

        # Loop through children
        for child in children:
            ignorechild = False

            # Child is on the closed list ignore it
            for closed_child in closed_list:
                if child == closed_child:
                    ignorechild = True

            # Create the f, g, and h values
            child.g = current_node.g + 1
            child.h = ((child.position[0] - end_node.position[0]) ** 2) + ((child.position[1] - end_node.position[1]) ** 2)
            child.f = child.g + child.h

            # Child is already in the open list then ignore it
            for open_node in open_list:
                if child == open_node and child.g > open_node.g:
                    ignorechild = True

            # Add the child to the open list. It will be looked at later on.
            if not ignorechild:
                open_list.append(child)

        #Increases nodes checked to show that we have checked another node
        nodesChecked += 1

    #----- end of while loop code ----#
    #If it can't find a path to the player it just return empty list
    return []

'''
maze = [[0, 0, 0, 0, '#', 0, 0, 0, 0, 0],
        [0, 0, 0, 0, '#', 0, 0, 0, 0, 0],
        [0, 0, 0, 0, '#', 0, 0, 0, 0, 0],
        [0, 0, 0, 0, '#', 0, 0, 0, 0, 0],
        [0, 0, 0, 0, '#', 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, '#', 0, 0, 0, 0, 0],
        [0, 0, 0, 0, '#', 0, 0, 0, 0, 0],
        [0, 0, 0, 0, '#', 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

start = (0, 0)
end = (7, 6)

path = astar(maze, start, end)
print(path)
maze[end[0]][end[1]] = 'e'
for i in maze:
    print(i)
'''
