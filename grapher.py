import sys
from pylab import *
from sets import Set
import matplotlib.pyplot as plt
import networkx as nx
import collections

'''
Summoned script extension
Input file:
 
Edges from where nodes are deduced
Example:


 IP1 IP4
 IP3 IP1 
 
'''


def getNextIndex():
    global index
    index = index + 1
    return index

def getIndex(ip):
    global G, nodes
    if ip not in ipMap.keys():
        i = getNextIndex()
        ipMap[ip] = i
        labels[i]=ip
        nodes.append(i)

    return ipMap[ip]


def printEdge(edge):
    global edgesCount
    global edges
    ip1 = edge[0]
    ip2 = edge[1]
    ip1I = getIndex(ip1)
    ip2I = getIndex(ip2)
    count = edgesCount[(ip1,ip2)]
    inverse_count = edgesCount[(ip2,ip1)]
    if count > inverse_count:
        edges.append((ip1I,ip2I))
        edge_labels[(ip1I,ip2I)] = "("+str(count)+", "+str(inverse_count)+")"
  

ipMap = {}
index = -1
edges = []
edge_labels = {}
edgesCount = None
nodes = []
labels = {}
lines = [line.rstrip('\n') for line in open(sys.argv[1])]

setEd = Set([])
arrEd = []
#Parse ips
for line in lines:   
   newIps = line.split(" ",2)
   setEd.add((newIps[0],newIps[1]))
   arrEd.append((newIps[0],newIps[1]))

edgesCount = collections.Counter(arrEd)


for package in setEd:
    printEdge(package)



G = nx.MultiDiGraph()
G.add_nodes_from(nodes)
G.add_edges_from(edges)

pos = nx.circular_layout(G)



nx.draw_networkx_nodes(G,pos,node_color='w',node_size=500)
nx.draw_networkx_edges(G,pos,width=1)

nx.draw_networkx_edge_labels(G,pos,edge_labels=edge_labels)
nx.draw_networkx_labels(G,pos,labels=labels,font_color='r',font_weight='bold')

plt.show()
