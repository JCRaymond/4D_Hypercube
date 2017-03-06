from Graphics import *
from Wireframe import *

pv = ProjectionViewer(750, 500)

C = gen_n_cube(4)
Ci = get_n_cube_indexes(C)
colors = []
colors.extend((255, 0, 0) for i in range(8))
colors.extend((0, 0, 255) for i in range(8))

cube = Wireframe(C, Ci, colors)

pv.translate_all(gen_translation_mat(0, 4, pv.width/2))
pv.translate_all(gen_translation_mat(1, 4, pv.height/2))
pv.scale_all(gen_scale_mat(4, 100))

pv.add_wireframe("cube", cube)
pv.run()

#For Controls look at Graphics.py at top of file