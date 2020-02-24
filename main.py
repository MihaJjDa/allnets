import networkx as nx
import matplotlib.pyplot as plt
import itertools
from networkx.algorithms import isomorphism

def ariphsum(n):
  return n*(n+1)/2

def noback(l):
  for (i, j) in l:
    if (j, i) in l:
      return False
  return True

def onefirst(l):
  n = 0
  r = []
  for (i, j) in l:
    k = True
    for (p, q) in l:
      if ((i!=p) or (j!=q)) and (i==q):
        k = False
    if k and (r.count(i) == 0):
      r.append(i)
      n = n+1
  return n == 1

def onelast(l):
  n = 0
  r = []
  for (i, j) in l:
    k = True
    for (p, q) in l:
      if ((i!=p) or (j!=q)) and (j==p):
        k = False
    if k and (r.count(j) == 0):
      r.append(j)
      n = n+1
  return n == 1

def isok(l):
  return not(noback(l) and onefirst(l) and onelast(l))

def isomorph(g, l):
  res = False
  if l != []:
    for i in l:
      gm = isomorphism.DiGraphMatcher(g, i)
      res = res or gm.is_isomorphic()
  return res

'''
for numnodes in [2,3]:
"""
 """
 for numedges in [1,2,3,4,5,6,7,8,9,10,11]:
 """'''
if True:
  if True:
    numnodes = 5
    numedges = 7
    numnodes = numnodes + 1
    listnodes = [i for i in range(1, numnodes)]
    listedges = []
    for i in listnodes:
      for j in listnodes:
        if i != j:
          listedges.append((i, j))

    listgraphes = [j for j in itertools.ifilterfalse(isok,
                                                     [list(i) for i in itertools.combinations(listedges, numedges)])]
    h = []
    j = 0
    for i in listgraphes:
      g = nx.DiGraph()
      g.add_nodes_from(listnodes)
      g.add_edges_from(i)
      if not (isomorph(g, h)) and nx.is_connected(nx.Graph(g)):
        j += 1
        h.append(g)
        nx.draw_shell(g)
        plt.show()
