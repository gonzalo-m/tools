#!/usr/bin/python

import re
import os.path, time
from os import listdir
from os.path import isfile, join
import argparse

class Graph:

	def __init__(self):
		self.adjacencyMap = {}
		self.dataMap = {}

	def add_edge(self, startVertex, endVertex):
		neighbors = self.adjacencyMap.get(startVertex, None)
		if neighbors is None:
			neighbors = {}
		neighbors[endVertex] = "" # empty for now
		self.adjacencyMap[startVertex] = neighbors

	def get_neighbors(self, startVertex):
		neighbors = self.adjacencyMap.get(startVertex, None)
		if neighbors is None:
			neighbors = {}
		return neighbors

	def get_vertices(self):
		return self.adjacencyMap

	def __str__(self):
		return str(self.adjacencyMap)

class Utils:

	@staticmethod
	def get_files(path):
		files = [f for f in listdir(path) if isfile(join(path, f))]
		return files

	@staticmethod
	def open_file(fname):
		f = open(fname, "r") #opens file with name of "test.txt"
		entries = []
		for line in f:
			entries.append(line.rstrip())
		return entries

	@staticmethod
	def populate_graph(graph, path, fname):
		entries = Utils.open_file(join(path, fname))
		for entry in entries:
			m = MAC_RE.search(entry)
			if m:
				mac_address = entry[m.start(): m.end()]
				graph.add_edge(mac_address, fname)


MAC_RE = re.compile('([a-fA-F0-9]{2}[:|\-]?){6}') # mac address regex

# -----------------------------------------------------------------------------
# List files to be analyzed
# -----------------------------------------------------------------------------
def get_files(path):
	print "Using in directory: {}".format(path)
	files = Utils.get_files(path)
	print "{0:<24} {1:>24}".format("Filename", "Date Modified")
	print "-"*49
	for fname in files:
		print "{0:24} {1:16}".format(fname, time.ctime(os.path.getmtime(join(path, fname))))
	return files

# -----------------------------------------------------------------------------
# Build Graph
# -----------------------------------------------------------------------------
def build_graph(files, path):
	print "Building graph" + "."*3
	graph = Graph()
	for fname in files:
		Utils.populate_graph(graph, path, fname)
	return graph

# -----------------------------------------------------------------------------
# Map MAC to files
# -----------------------------------------------------------------------------
def map_mac_addresses(graph):
	print "Mapping MAC addresses to files" + "."*3
	print "MAC {0:<24} {1:>20}".format("", "Appears in")
	print "="*49
	for mac in graph.get_vertices():
		neighbors = graph.get_neighbors(mac)
		print "{0:<24} {1:>19}".format(mac, "")
		if len(neighbors) == 0:
			print "{0:32} {1:>16}".format("", "None")
		else:
			for key, value in neighbors.iteritems():
				print "{0:32} {1:>16}".format("", key)
		print "-"*49

def main():
	parser = argparse.ArgumentParser()
	parser.add_argument("-p", "--path", help="directory containing the files to be analyzed")
	args = parser.parse_args()

	path = args.path
	files = get_files(path)
	graph = build_graph(files, path)
	map_mac_addresses(graph)


if __name__ == '__main__':
	main()







