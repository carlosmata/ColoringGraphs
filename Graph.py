'''
	Bipartite Graph
	Carlos Antonio Mata Valdez
	05/11/2018
'''
from Vertex import Vertex

class Graph(object):

	def __init__(self, vs = []):
		self.vertexs = vs			#list of vertexs

	#Add a vertex to a graph
	def addVertex(self, vertex):
		self.vertexs.append(vertex)

	#Get the vertex list to the graph
	def getVertexs(self):
		return self.vertexs

	#Add an edge in vertex1 and vertex2
	def addEdge(self, vertex1, vertex2):
		vertex1.setEdge(vertex2)

	#Color the vertexs of the node
	def coloring(self):
		for vertex in self.vertexs:
			if(not vertex.isColored()):
				vertex.coloring()

	#Clear the color of the enges
	def clearColor(self):
		for vertex in self.vertexs:
			vertex.clearColor()

	#Print the bigraph X and Y sets
	def print(self):
		cad = "nodes = [ \n";
		for x in self.vertexs:
			cad = cad + "\t" + x.id + "[" + str(x.getColor()) + "]" + "( "
			for edge in x.getEdges():
				cad = cad + edge.id + "[" + str(edge.getColor()) + "]" + ", "
			cad = cad + "), \n"
		cad = cad + "]";

		return cad

