import numpy as np
import random
from math import log2, ceil
import matplotlib.pyplot as plt
from scipy.ndimage import gaussian_filter


def diamond_square(size, min_height, max_height, roughness, post_blur=0):
    assert 0 <= roughness, "Roughness below 0"
    assert roughness <= 1, "Roughness above 1"
    assert post_blur >= 0, "Negative post_blur"

    end_size = size

    size = [2 ** ceil(log2(size[0] - 1)) + 1, 2 ** ceil(log2(size[1] - 1)) + 1]

    # noinspection PyTypeChecker
    height_map = np.zeros((size[0], size[1]), dtype=np.float)
    height_map[0::size[0] - 1, 0::size[1] - 1] = np.random.uniform(0, 1, (2, 2))

    itts_done = 0

    if size[0] > size[1]:
        step = size[0] - 1
        while step > size[1]:
            r = roughness ** itts_done
            half_step = step // 2
            x_offset = 0
            while x_offset < size[0] - step:
                avg = (height_map[x_offset, 0] + height_map[x_offset + step, 0]) / 2
                height_map[x_offset + half_step, 0] = (r * random.uniform(0, 1) + (1.0 - r) * avg)
                avg = (height_map[x_offset, size[1] - 1] + height_map[x_offset + step, size[1] - 1]) / 2
                height_map[x_offset + half_step, size[1] - 1] = (r * random.uniform(0, 1) + (1.0 - r) * avg)
                x_offset += step
            step = half_step

    elif size[0] < size[1]:
        step = size[1] - 1
        while step > size[0]:
            r = roughness ** itts_done
            half_step = step // 2
            y_offset = 0
            while y_offset < size[1] - step:
                avg = (height_map[0, y_offset] + height_map[0, y_offset + step]) / 2
                height_map[0, y_offset + half_step] = (r * random.uniform(0, 1) + (1.0 - r) * avg)
                avg = (height_map[size[0] - 1, y_offset] + height_map[size[0] - 1, y_offset + step]) / 2
                height_map[size[0] - 1, y_offset + half_step] = (r * random.uniform(0, 1) + (1.0 - r) * avg)
                y_offset += step
            step = half_step

    else:
        step = size[0]

    for itt in range(itts_done, itts_done + int(log2(step))):
        r = roughness ** itt
        half_step = step // 2

        # Diamond
        x_offset = 0
        while x_offset < size[0] - step:
            y_offset = 0
            while y_offset < size[1] - step:
                avg = (height_map[x_offset, y_offset] + height_map[x_offset + step, y_offset] +
                       height_map[x_offset, y_offset + step] + height_map[x_offset + step, y_offset + step]) / 4
                height_map[x_offset + half_step, y_offset + half_step] = (r * random.uniform(0, 1) + (1.0 - r) * avg)
                y_offset += step
            x_offset += step

        # Square
        x_offset = half_step
        while x_offset < size[0]:
            y_offset = 0
            while y_offset < size[1]:
                cnt = avg = 0

                if x_offset - half_step >= 0:
                    cnt += 1
                    avg += height_map[x_offset - half_step, y_offset]
                if y_offset - half_step >= 0:
                    cnt += 1
                    avg += height_map[x_offset, y_offset - half_step]
                if x_offset + half_step < size[0]:
                    cnt += 1
                    avg += height_map[x_offset + half_step, y_offset]
                if y_offset + half_step < size[1]:
                    cnt += 1
                    avg += height_map[x_offset, y_offset + half_step]

                avg /= cnt
                height_map[x_offset, y_offset] = (r * random.uniform(0, 1) + (1.0 - r) * avg)
                y_offset += step
            x_offset += step

        x_offset = 0
        while x_offset < size[0]:
            y_offset = half_step
            while y_offset < size[1]:
                cnt = avg = 0

                if x_offset - half_step >= 0:
                    cnt += 1
                    avg += height_map[x_offset - half_step, y_offset]
                if y_offset - half_step >= 0:
                    cnt += 1
                    avg += height_map[x_offset, y_offset - half_step]
                if x_offset + half_step < size[0]:
                    cnt += 1
                    avg += height_map[x_offset + half_step, y_offset]
                if y_offset + half_step < size[1]:
                    cnt += 1
                    avg += height_map[x_offset, y_offset + half_step]

                avg /= cnt
                height_map[x_offset, y_offset] = (r * random.uniform(0, 1) + (1.0 - r) * avg)
                y_offset += step
            x_offset += step

        step = half_step

    height_map = height_map[0:end_size[0], 0:end_size[1]]

    if post_blur:
        height_map = gaussian_filter(height_map, post_blur)

    height_map = (max_height - min_height) * height_map + min_height

    return height_map


if __name__ == '__main__':
    a = diamond_square([16, 16], -100, 100, 0.5, 1)
    # for x in a: print(list(x))
    plt.imshow(a)
    plt.show()
