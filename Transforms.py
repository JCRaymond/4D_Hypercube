from Matrix import *
from math import sin, cos, pi

def gen_rot_mat(axis1, axis2, n, theta):
    m = Matrix.identity(n)
    m[axis1][axis1] = cos(theta)
    m[axis1][axis2] = -sin(theta)
    m[axis2][axis1] = sin(theta)
    m[axis2][axis2] = cos(theta)
    return m

def gen_translation_mat(axis, n, amnt):
    m = Matrix.identity(n)
    m[axis][n-1] = amnt
    return m

def gen_scale_mat(n, amnt):
    m = Matrix.identity(n)
    for i in range(n-1):
        m[i][i] = amnt
    return m