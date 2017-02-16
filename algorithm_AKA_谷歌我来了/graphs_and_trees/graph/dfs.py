#!/usr/bin/python
#coding:utf-8
#=======================================================================
#  Author: Yu Zhou
#  Title: OOP Adjacency List
#=======================================================================

class Node(object):
	def __init__(self, n):
		self.name = n
		self.neighbor = []
		#设置一个discovery time，然后当node的path没有分支以后，设置一个finish time
		self.discovery = 0
		self.finish = 0

		self.color = 'black'

	def add_neighbor(self, key):
		#check if key exists:
		if key not in self.neighbor:
			self.neighbor.append(key)
			#排个序
			self.neighbor.sort()


class Graph():
	def __init__(self):
		self.nodes = {} #这个hash用来存node的key，然后reference到node，然后再通过
						# node.neighbor去access，node里面自带的neighbor array

	def add_node(self, node):
		#check if node's key is  already exist in the nodes hashtable
		if isinstance(node, Node) and node.name not in self.nodes:
			self.nodes[node.name] = node #key就是node.name，然后指向Node
			return True
		else:
			return False

	def add_edges(self, start_key, end_key):
		if start_key in self.nodes and end_key in self.nodes:
			#start是node.key,然后nodes[start]就reference到这个Node本身了，这时候可以用子方程，add_neighbor
			#然后把end.key传进去，建立从start到end的关系，这个步骤需要双向，因为两个node的自带的list是独立的
			self.nodes[start_key].add_neighbor(end_key)
			self.nodes[end_key].add_neighbor(start_key)
			return True
		else:
			return False

	def display(self):
		for key in sorted(list(self.nodes.keys())):  #把Key在左边竖着打印出来，也就是A-K
			print (key + str(self.nodes[key].neighbor)+ "  " +  str(self.nodes[key].discovery)+ "/" + str(self.nodes[key].finish))  #打印所有的Neighbor

	def dfs(self, node):
		global time
		time = 1
		self._dfs(node)

	def _dfs(self, node):
		global time
		node.color = 'red'
		node.discovery = time
		time += 1
		for neighbor in node.neighbor:
			if self.nodes[neighbor].color == 'black':
				self._dfs(self.nodes[neighbor])
		node.color = 'blue'
		node.finish = time
		time += 1



if __name__ == '__main__':
	g = Graph()
	#把A和K转成数字，这样可以放进range，之后再转回来
	#在Graph的Hash表里面，生成 NODE: A,B,C,D,E,F,G,H,I,J,K
	a = Node('A')
	g.add_node(a)
	for i in range(ord('A'),ord('K')):
		g.add_node(Node(chr(i)))

	edges = ['AB','AC', 'AD', 'AF', 'BA','BC','BD','CG', 'DE', 'DH', 'EH', 'FG', 'FI', 'FJ', 'GJ', 'HI']
	for edge in edges:
		g.add_edges(edge[:1], edge[1:])  #比如第一个'AB'，就是分别加A，B

	g.dfs(a)
	g.display()
