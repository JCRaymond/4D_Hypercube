from Matrix import *

def get_n_cube_indexes(cube):
    indexes = []
    cols = cube.transpose()
    for c1, col1 in enumerate(cols):
        for c2, col2 in enumerate(cols.vals[c1+1:]):
            num_diffs = 0
            for c1elem, c2elem in zip(col1, col2):
                if c1elem != c2elem:
                    num_diffs+=1
            if num_diffs == 1:
                indexes.append((c1, c2+c1+1))
    return indexes

def gen_n_cube(n):
    rows = n
    cols = pow(2, n)
    m = Matrix(rows, cols)
    for i in range(rows):
        switch = pow(2, i)
        for j in range(cols):
            if (j/switch)%2 == 1:
                m[i][j] = -1
            else:
                m[i][j] = 1
    return m
