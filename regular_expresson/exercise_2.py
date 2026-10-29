position='The position of some particles on the horizontal x-axis are -12, -4, -3 and -1 in the negative direction, 0 at origin, 4 and 8 in the positive direction. Extract these numbers from this whole text and find the distance between the two furthest particles.'

import re

# point=re.findall(r"-?\d+",position)
# distance=int(point[-1])-int(point[0])

# print(distance)

point = [int(x) for x in re.findall(r"-?\d+", position)]

distance = max(point) - min(point)

print(distance)