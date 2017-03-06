from Matrix import *

def avg_color(color1, color2):
    return tuple([(val1+val2)/2 for val1, val2 in zip(color1, color2)])

def dim_color(color):
    return tuple([val-30 if val >= 30 else 0 for val in color])

class Wireframe:

    def_node_color = (255,255,255)

    def __init__(self, nodes, edge_pairs, node_colors = ()):
        self.nodes = nodes
        self.edge_pairs = edge_pairs
        self.node_colors = node_colors
        if len(node_colors) != self.nodes.cols:
            print "Def colors"
            self.node_colors = [Wireframe.def_node_color for col in range(self.nodes.cols)]

    def get_nodes(self):
        return [coord for coord in self.nodes.transpose().vals]

    def get_nodes_c(self):
        nodes = self.get_nodes()
        return zip(nodes, self.node_colors)

    def get_edges(self):
        edges = []
        coords = self.nodes.transpose().vals
        for start, stop in self.edge_pairs:
            edges.append((coords[start], coords[stop]))
        return edges

    def get_edges_c(self):
        edges = self.get_edges()
        edge_colors = []
        for start, stop in self.edge_pairs:
            edge_colors.append(dim_color(avg_color(self.node_colors[start], self.node_colors[stop])))
        return zip(edges, edge_colors)

    def transformed(self, T):
        return Wireframe(T*self.nodes, self.edge_pairs, self.node_colors)

    def homogeneous(self, n):
        P = Matrix(n, self.nodes.rows)
        for i in range(n):
            P[i][i] = 1
        new_nodes = (P * self.nodes).homogeneous()
        return Wireframe(new_nodes, self.edge_pairs, self.node_colors)