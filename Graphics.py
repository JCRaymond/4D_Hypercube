import pygame
from NCube import *
from Transforms import *

class pv:
    shift_amnt = 10
    scale_u_amnt = 1.25
    scale_d_amnt = 1/scale_u_amnt
    r = pi/32

    shift_l = gen_translation_mat(0, 4, -shift_amnt)
    shift_r = gen_translation_mat(0, 4, shift_amnt)
    shift_d = gen_translation_mat(1, 4, -shift_amnt)
    shift_u = gen_translation_mat(1, 4, shift_amnt)

    scale_u = gen_scale_mat(4, scale_u_amnt)
    scale_d = gen_scale_mat(4, scale_d_amnt)

    X = gen_rot_mat(1, 2, 4, r)
    Xi = gen_rot_mat(1, 2, 4, -r)
    Y = gen_rot_mat(0, 2, 4, r)
    Yi = gen_rot_mat(0, 2, 4, -r)
    Z = gen_rot_mat(0, 1, 4, r)
    Zi = gen_rot_mat(0, 1, 4, -r)

    R1 = gen_rot_mat(0, 3, 4, r)
    R1i = gen_rot_mat(0, 3, 4, -r)
    R2 = gen_rot_mat(1, 3, 4, r)
    R2i = gen_rot_mat(1, 3, 4, -r)
    R3 = gen_rot_mat(2, 3, 4, r)
    R3i = gen_rot_mat(2, 3, 4, -r)


def rotate_pv_4D(pv, R):
    for key, wireframe in pv.wireframes.items():
        pv.wireframes[key] = wireframe.transformed(R)


class ProjectionViewer:

    key_functions = {
        pygame.K_LEFT: (lambda x: x.translate_all(pv.shift_l)),
        pygame.K_RIGHT: (lambda x: x.translate_all(pv.shift_r)),
        pygame.K_DOWN: (lambda x: x.translate_all(pv.shift_d)),
        pygame.K_UP: (lambda x: x.translate_all(pv.shift_u)),

        pygame.K_EQUALS: (lambda x: x.scale_all(pv.scale_u)),
        pygame.K_MINUS: (lambda x: x.scale_all(pv.scale_d)),

        pygame.K_q: (lambda x: x.rotate_all(pv.X)),
        pygame.K_w: (lambda x: x.rotate_all(pv.Xi)),
        pygame.K_a: (lambda x: x.rotate_all(pv.Y)),
        pygame.K_s: (lambda x: x.rotate_all(pv.Yi)),
        pygame.K_z: (lambda x: x.rotate_all(pv.Z)),
        pygame.K_x: (lambda x: x.rotate_all(pv.Zi)),

        pygame.K_y: (lambda x: rotate_pv_4D(x,pv.R1)),
        pygame.K_u: (lambda x: rotate_pv_4D(x,pv.R1i)),
        pygame.K_h: (lambda x: rotate_pv_4D(x,pv.R2)),
        pygame.K_j: (lambda x: rotate_pv_4D(x,pv.R2i)),
        pygame.K_n: (lambda x: rotate_pv_4D(x,pv.R3)),
        pygame.K_m: (lambda x: rotate_pv_4D(x,pv.R3i)),
    }

    def __init__(self, width, height, background = (10, 10, 50), node_radius = 4):
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption("Wireframe Display")
        self.background = background

        self.wireframes = {}
        self.node_radius = 4
        self.display_nodes = True
        self.display_edges = True

        self.translate = Matrix.identity(4)
        self.rotate = Matrix.identity(4)
        self.scale = Matrix.identity(4)

    def add_wireframe(self, name, wireframe):
        self.wireframes[name] = wireframe

    def run(self):

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key in ProjectionViewer.key_functions:
                        ProjectionViewer.key_functions[event.key](self)

            self.display()
            pygame.display.flip()

    def display(self):

        self.screen.fill(self.background)

        for wireframe in self.wireframes.values():
            twf = wireframe.transformed(self.rotate)
            twf = twf.transformed(self.scale)
            twf = twf.homogeneous(3)
            twf = twf.transformed(self.translate)

            if self.display_edges:
                for ((e_start, e_stop), color) in twf.get_edges_c():
                    pygame.draw.aaline(self.screen, color, (e_start[0], e_start[1]),
                                       (e_stop[0], e_stop[1]), 1)

            if self.display_nodes:
                for node, color in twf.get_nodes_c():
                    pygame.draw.circle(self.screen, color, (int(node[0]), int(node[1])), self.node_radius, 0)

    def translate_all(self, T):
        self.translate = T*self.translate

    def rotate_all(self, R):
        self.rotate = R*self.rotate

    def scale_all(self, S):
        self.scale = S*self.scale