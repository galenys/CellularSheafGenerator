import matplotlib.pyplot as plt
import random
import itertools

class SimplicialComplex:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.vertices = {i: self.random_point() for i in range(num_vertices)}
        self.edges = self.generate_edges()
        self.faces = self.generate_faces()

    def generate_edges(self):
        all_possible_edges = list(itertools.combinations(range(self.num_vertices), 2))
        return random.sample(all_possible_edges, k=random.randint(1, len(all_possible_edges)))

    def generate_faces(self):
        potential_faces = list(itertools.combinations(range(self.num_vertices), 3))
        faces = []
        for face in potential_faces:
            edges_of_face = list(itertools.combinations(face, 2))
            if all(edge in self.edges for edge in edges_of_face):
                faces.append(face)
        return faces

    def display(self):
        fig, ax = plt.subplots()
        ax.set_aspect('equal')
        ax.set_xlim(0, 1)
        ax.set_ylim(0, 1)

        for v in self.vertices.values():
            ax.scatter(*v, color='blue')

        for edge in self.edges:
            v0, v1 = self.vertices[edge[0]], self.vertices[edge[1]]
            plt.plot([v0[0], v1[0]], [v0[1], v1[1]], color='black')

        for face in self.faces:
            polygon = [self.vertices[v] for v in face]
            polygon.append(polygon[0])  # close the polygon
            xs, ys = zip(*polygon)
            plt.fill(xs, ys, alpha=0.3, color='grey')

        plt.show()

    @staticmethod
    def random_point():
        return random.uniform(0, 1), random.uniform(0, 1)

sc = SimplicialComplex(5)
sc.display()
