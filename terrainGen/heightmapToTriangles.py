import numpy as np


def heightmap_to_triangles(heightmap: np.array, min, max):
    shape = heightmap.shape
    triangles = []
    for x in range(shape[0] - 1):
        for y in range(shape[1] - 1):
            avg = [((x + 0.5) / shape[0]) * (max[0] - min[0]) + min[0],
                   ((y + 0.5) / shape[1]) * (max[1] - min[1]) + min[1],
                   sum(sum(heightmap[x:x + 2, y:y + 2])) / 4]

            # x,y x+1,y avg
            triangles.append([(x / shape[0]) * (max[0] - min[0]) + min[0], (y / shape[1]) * (max[1] - min[1]) + min[1],
                              heightmap[x, y]])
            triangles.append(
                [((x + 1) / shape[0]) * (max[0] - min[0]) + min[0], (y / shape[1]) * (max[1] - min[1]) + min[1],
                 heightmap[x + 1, y]])
            triangles.append(avg)

            # x+1,y x+1,y+1 avg
            triangles.append(
                [((x + 1) / shape[0]) * (max[0] - min[0]) + min[0], (y / shape[1]) * (max[1] - min[1]) + min[1],
                 heightmap[x+1, y]])
            triangles.append(
                [((x + 1) / shape[0]) * (max[0] - min[0]) + min[0], ((y + 1) / shape[1]) * (max[1] - min[1]) + min[1],
                 heightmap[x + 1, y+1]])
            triangles.append(avg)

            # x+1,y+1 x,y+1 avg
            triangles.append(
                [((x + 1) / shape[0]) * (max[0] - min[0]) + min[0], ((y + 1) / shape[1]) * (max[1] - min[1]) + min[1],
                 heightmap[x+1, y+1]])
            triangles.append(
                [(x / shape[0]) * (max[0] - min[0]) + min[0], ((y + 1) / shape[1]) * (max[1] - min[1]) + min[1],
                 heightmap[x, y+1]])
            triangles.append(avg)

            # x,y+1 x,y avg
            triangles.append(
                [(x / shape[0]) * (max[0] - min[0]) + min[0], ((y + 1) / shape[1]) * (max[1] - min[1]) + min[1],
                 heightmap[x, y + 1]])
            triangles.append(
                [(x / shape[0]) * (max[0] - min[0]) + min[0], (y / shape[1]) * (max[1] - min[1]) + min[1],
                 heightmap[x, y]])
            triangles.append(avg)

    return triangles


if __name__ == '__main__':
    from diamondSquare import *

    m = diamond_square([3, 3], 0, 1, 0, 5)
    print(heightmap_to_triangles(m))
