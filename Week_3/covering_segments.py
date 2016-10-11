# Uses python3
import sys
from collections import namedtuple

Segment = namedtuple('Segment', 'start end')

def optimal_points(segments):
    points = []
    #Sort by end point to get minimum one
    sorted_set = sorted(segments, key = lambda x: x.end)
    
    #Repeat the following until all segments have been removed from the sorted_set
    while sorted_set:
        #Get rid of segment with smallest end point first
        smallest_segment = sorted_set.pop(0)
        #This is the coordinate for the intersecting segment
        points.append(smallest_segment.end)

        #Remove segments whose start point is less than this smallest end point
        for segment in sorted_set[:]:
            if segment.start <= smallest_segment.end: sorted_set.remove(segment)

    return points

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *data = map(int, input.split())
    segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    points = optimal_points(segments)
    print(len(points))
    for p in points:
        print(p, end=' ')
