'''
	Bipartite Graph
	Carlos Antonio Mata Valdez
	05/11/2018
'''
from Vertex import Vertex
from graphviz import Graph
from random import random
import subprocess

class GraphC(object):

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

	#Execute the command to generate the image using graphviz
	def executeCommand(self, fileName, format):
		try:
			subprocess.call("./bin/dot.exe" + " -T" + format + " " + 
							 fileName  + ".txt -o " + fileName + "." + format)
		except:
			print("An exception occurred")

	#Get the maximun color of the vertexs
	def getMaximumColor(self):
		max = 0
		for vertex in self.vertexs:
			if(vertex.getColor() > max):
				max =  vertex.getColor()

		return max + 1;

	#Execute the image of the graph
	def generateImage(self):

		filesource = "output/sourceGraph"
		colors = self.generateColors()
		
		self.generateFileTxt(filesource, colors)
		self.executeCommand(filesource, "png")

	#Generate the file TXT to the image graph
	def generateFileTxt(self, filesource, colors):
		dot = Graph('G', filename='coloring.gv', engine='sfdp')

		for node in self.vertexs:
			dot.attr('node', shape='ellipse', style='filled', color=colors[node.getColor()], fontcolor='white')
			dot.node(node.id)

		for node in self.vertexs:
			node.drawing = True
			for edge in node.getEdges():
				if(not edge.drawing):
					dot.edge(node.id, edge.id)

		dot.attr(label='(Las materias con diferente color no pueden compartir horario)')
		file = open(filesource + ".txt","w") 
		file.write(dot.source) 
		file.close()

	#generate the colors to the graph
	def generateColors(self):
		colors =[]

		#generates the colors
		for c in range(self.getMaximumColor()):
			colors.append(str(random()) + ' ' + 
							str(random()) + ' ' + 
							str(random()))

		return colors

