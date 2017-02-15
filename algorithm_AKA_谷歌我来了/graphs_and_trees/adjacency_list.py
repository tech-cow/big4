#!/usr/bin/python
#coding:utf-8
#=======================================================================
#  Author: Yu Zhou
#  Title: Adjacency List
#=======================================================================

class Node:  #Vertex
	def __init__(self, n):
		self.name = n
		self.neighbors = []

	def add_neighbor(self, node_name):
		if node_name not in self.neighbors:
			self.neighbors.append(node_name)
			self.neighbors.sort()	#sort以后工整点

class Graph:
	#Graph的整体structure是一个Hash table
	#这样写的好处是可以给Key起名字，key是node.name，然后value就是Node
	def __init__(self):
		self.nodes = {}

	def add_node(self, node):
		if isinstance(node, Node) and node.name not in self.nodes:
			self.nodes[node.name] = node	 #key就是node.name，然后指向Node
			return True
		else:
			return False

	def add_edge(self,start,end):  #start node.key & end node.key
		if start in self.nodes and end in self.nodes:
			#start是node.key,然后nodes[start]就reference到这个Node本身了，这时候可以用子方程，add_neighbor
			#然后把end.key传进去，建立从start到end的关系，这个步骤需要双向，因为两个node的自带的list是独立的
			self.nodes[start].add_neighbor(end)
			self.nodes[end].add_neighbor(start)
			return True
		else:
			return False

	def print_graph(self):
		for key in sorted(list(self.nodes.keys())): #把Key在左边竖着打印出来，也就是A-K
			print(key + str(self.nodes[key].neighbors))  #打印所有的Neighbor



if __name__ == '__main__':
	g = Graph()
	#把A和K转成数字，这样可以放进range，之后再转回来
	#在Graph的Hash表里面，生成 NODE: A,B,C,D,E,F,G,H,I,J,K
	for i in range(ord('A'),ord('K')):
		g.add_node(Node(chr(i)))

	edges = ['AB', 'AE', 'BF', 'CG', 'DE', 'DH', 'EH', 'FG', 'FI', 'FJ', 'GJ', 'HI']
	for edge in edges:
		g.add_edge(edge[:1], edge[1:])  #比如第一个'AB'，就是分别加A，B

	g.print_graph()
