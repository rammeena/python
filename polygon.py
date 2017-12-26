#class Vertex(object):
#    def __init__(self):
#        self.x = 0.0
#        self.y = 1.0

class Polygon(object):
    def __init__(self, list_of_vertices):

        self.vertices =list_of_vertices

    def get_vertex_positions(self):
        return zip( *((v.x,v.y) for v in self.vertices ) )
