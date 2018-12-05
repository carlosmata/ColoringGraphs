#from graphviz import Digraph
from Graph import Graph
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


g = Graph([ingles, automatas, algoritmos, grafos, senales, software, probabilidad])

g.coloring()

print(g.print())
"""
dot = Digraph(comment='The Round Table')

dot.node('A', 'King Arthur')
dot.node('B', 'Sir Bedevere the Wise')
dot.node('L', 'Sir Lancelot the Brave')

dot.edges(['AB', 'AL'])
dot.edge('B', 'L', constraint='false')

print(dot.source)  # doctest: +NORMALIZE_WHITESPACE

dot.render('test-output/round-table.gv', view=False)  # doctest: +SKIP """