'''
https://realpython.com/python-heapq-module/#how-to-identify-problems
'''

import heapq

'''
Our algorithm is a variant of Dijkstra’s algorithm. There are three data structures that are kept 
and updated throughout the algorithm:

(1) tentative is a map of a tentative path from the origin to a position, pos. The path is called 
tentative because it’s the shortest known path, but it might be improved upon.

(2) certain is set of points for which the path that tentative maps is certain to be the shortest possible path.

(3) candidates is a heap of positions that have a path. The sorting key of the heap is the length of the path.

At each step, you perform up to four actions:

(1) Pop a candidate from candidates.

(2) Add the candidate to the certain set. If the candidate is already a member of the certain set, then skip next two actions.

(3) Find the shortest known path to the current candidate.

(4) For each of the current candidate’s immediate neighbors, see if going through the candidate gives a 
shorter path than the current tentative path. If so, then update the tentative path and the candidates heap with this new path.

The steps are run in a loop until the destination is added to the certain set. When the destination is in the certain set, 
you’re done. The output of the algorithm is the tentative path to the destination, which is now certain to be the shortest possible path.

'''


map = """\
.......X..
.......X..
..X.XXXX..
..........
..........
"""

def parse_map(map):
    ''' The function takes a map and returns a tuple of three elements:
        A list of lines
        The origin
        The destination
    '''
    lines = map.splitlines()
    origin = 0, 0
    destination = len(lines[-1]) - 1, len(lines) - 1
    return lines, origin, destination


# Calculates whether a given (x, y) position is valid
def is_valid(lines, position):
    ''' This function takes two arguments:
        lines is the map as a list of lines.
        position is the position to check as a two-tuple of integers indicating the (x, y) coordinates.
    '''
    x, y = position
    if not (0 <= y < len(lines) and 0 <= x < len(lines[y])):
        return False
    if lines[y][x] == "X":
        return False
    return True

# finds all the neighbors of a position
def get_neighbors(lines, current):
    ''' get_neighbors() is careful to avoid identifying a position as its 
        own neighbor, but it does allow diagonal neighbors. This is why at least one 
        of dx and dy must not be zero, but it’s okay for both of them to be non-zero
    '''
    x, y = current
    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            if dx == 0 and dy == 0:
                continue
            position = x + dx, y + dy
            if is_valid(lines, position):
                yield position

# yields positions for which the path that has through as its last step is shorter than the current known path
def get_shorter_paths(tentative, positions, through):
    ''' get_shorter_paths() has three parameters:
        (1) tentative is a dictionary mapping a position to the shortest known path.
        (2) positions is an iterable of positions to which you want to shorten the path. The assumption is 
        that all elements in positions can be reached in one step from through
        (3) through is the position through which, perhaps, a shorter path to the positions can be found.
    '''
    ''' The function get_shorter_paths() checks if using through as the last step will make a 
        better path for each position. If there’s no known path to a position, then any path is shorter. 
        If there is a known path, then you only yield the new path if its length is shorter. In order to 
        make the API of get_shorter_paths() easier to use, part of the yield is also the shorter path
    '''
    path = tentative[through] + [through]
    for position in positions:
        if position in tentative and len(tentative[position]) <= len(path):
            continue
        yield position, path


def find_path(map):
    lines, origin, destination = parse_map(map)
    tentative = {origin: []}
    candidates = [(0, origin)]
    certain = set()
    while destination not in certain and len(candidates) > 0:
        _ignored, current = heapq.heappop(candidates)
        if current in certain:
            continue
        certain.add(current)
        neighbors = set(get_neighbors(lines, current)) - certain
        shorter = get_shorter_paths(tentative, neighbors, current)
        for neighbor, path in shorter:
            tentative[neighbor] = path
            heapq.heappush(candidates, (len(path), neighbor))
    if destination in tentative:
        return tentative[destination] + [destination]
    else:
        raise ValueError("no path")

# It returns a new map with the path indicated by the at symbol ("@")
def show_path(path, map):
    lines = map.splitlines()
    for x, y in path:
        lines[y] = lines[y][:x] + "@" + lines[y][x + 1 :]
    return "\n".join(lines) + "\n"


if __name__ == "__main__":
    path = find_path(map)
    print(show_path(path, map))