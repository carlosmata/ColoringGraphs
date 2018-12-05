import copy

'''
	Vertex
	Carlos Antonio Mata Valdez
	05/11/2018
'''
class Vertex(object):

	def __init__(self, id = ""):
		self.id = id
		self.edges = []
		self.color = None
		self.drawing = False

	#Add an edge in the vertex 
	def setEdge(self, vertex):
		vertex.getEdges().append(self)
		self.edges.append(vertex) 

	#Add a set of edges in the vertex
	def setEdges(self, vertexs):
		self.edges = list(set(self.edges + vertexs))

	#Determines if the vertex has a transition with the vertex sent
	def hasEdgeWith(self, vertex):
		for v in self.edges:
			if(v.id == vertex.id):
				return True
		return False

	#Get the edges of the vertex
	def getEdges(self):
		return self.edges

	#Delete an edge with the vertex sent
	def deleteEdgeWith(self, vertex):
		self.edges.remove(x)

	#Define if a vertex have color
	def isColored(self):
		return (self.color != None)

	#Set a color at vertex
	def setColor(self, color):
		self.color =  color

	#Get the color of the node
	def getColor(self):
		return self.color

	#Clear the color of the enges
	def clearColor(self):
		self.color = None

	#Calculate the color of the vertex
	def coloring(self):
		notAvailable = []
		colorPossible = 0

		for v in self.edges:
			if(v.isColored()):
				notAvailable.append(v.color)

		self.color = self.calculateColor(colorPossible, notAvailable)

		for v in self.edges:
			if(not v.isColored()):
				v.coloring()

	#Calculate the new value to colorPossible that is not in notAvailable list
	def calculateColor(self, colorPossible, notAvailable):

		newColor = colorPossible
		for c in notAvailable:
			if(c == colorPossible):
				colorPossible = colorPossible + 1
				newColor = self.calculateColor(colorPossible, notAvailable)

		return newColor


