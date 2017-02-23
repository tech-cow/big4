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
		#随便设个大一点的值，之后需要做比较
		self.distance = 5211314
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
			print (key + str(self.nodes[key].neighbor)+ "  " +  str(self.nodes[key].distance))  #打印所有的Neighbor

	def bfs(self, node):
		#确保bfs的Node存在与hash里面
		if node.name in self.nodes:
			#更改初始信息
			node.distance = 0
			node.color = 'red'              #black是未访问，red表示访问过
			q = []                          #设置一个Queue

			for neighbor in node.neighbor:
				self.nodes[neighbor].distance = node.distance + 1     #增加neighbor距离
				q.append(neighbor)                   #把访问的Node的所有邻居，放进这个Queue


			while len(q) > 0:
				key = q.pop(0)
				poped_node = self.nodes[key]    #pop出来key，然后reference到这个Node
				poped_node.color = 'red'

				for neighbor in poped_node.neighbor:
					neighbor_node = self.nodes[neighbor]
					if neighbor_node.color == 'black':
						q.append(neighbor)
						if neighbor_node.distance > poped_node.distance + 1:
							neighbor_node.distance = poped_node.distance + 1
							# print neighbor_node.distance



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

	g.bfs(a)
	g.display()
