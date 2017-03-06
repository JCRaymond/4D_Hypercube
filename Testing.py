from Matrix import *
from Wireframe import *
from NCube import *

c = gen_n_cube(4)
ci = get_n_cube_indexes(c)
w = Wireframe(c, ci)

t = Matrix.identity(4) * 2

print c
print w.mat
print w.nodes[0].coords
print c