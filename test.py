from Graph import GraphC
from Vertex import Vertex

ingles = Vertex("ingles")
automatas = Vertex("automatas")
algoritmos = Vertex("algoritmos")
grafos = Vertex("grafos")
senales = Vertex("senales")
software = Vertex("software")
probabilidad = Vertex("probabilidad")

ingles.setEdge(algoritmos)
ingles.setEdge(grafos)
ingles.setEdge(senales)
ingles.setEdge(probabilidad)
ingles.setEdge(software)
ingles.setEdge(automatas)

automatas.setEdge(algoritmos)
automatas.setEdge(grafos)
automatas.setEdge(software)

algoritmos.setEdge(grafos)
algoritmos.setEdge(senales)
algoritmos.setEdge(probabilidad)
algoritmos.setEdge(software)

grafos.setEdge(software)

senales.setEdge(software)
senales.setEdge(probabilidad)

software.setEdge(probabilidad)


g = GraphC([ingles, automatas, algoritmos, grafos, senales, software, probabilidad])

g.coloring()

print(g.print())

g.generateImage()