from anttsp import AntTSP
from antcolony import AntColony
from antgraph import AntGraph
from ant import Ant

# T = 1 # number of test cases
# fout = open ("answer.out", "w")
# #for t in xrange(1, T+1):
#     #fin = open("instances/" + str(t) + ".in", "r")
# fin = open("instances/1.in", "r")
# # find an answer, and put into assign
# tsp = AntTSP(fin.read())
# assign = tsp.findSolution()
# assign = str(assign)
# fout.write(assign + "\n")
# fout.close()

T = 1 # number of test cases
fout = open ("answer3.out", "w")
for t in xrange(1, T+1):
	print t
	fin = open("instances/384.in", "r")# + str(t) + ".in", "r")
	N = int(fin.readline())
	d = [[] for i in range(N)]
	for i in xrange(N):
	    d[i] = [int(x) for x in fin.readline().split()]
	c = fin.readline()
	#print d
	tsp = AntTSP(N,d,c)
	assign = tsp.findSolution()
	assign = str(assign).split(', ')
	assign[0] = assign[0][1:]
	assign[-1] = assign[-1][0:1]
	# find an answer, and put into assign
	# assign = [0] * N
	# for i in xrange(N):
	#     assign[i] = i+1

	fout.write("%s\n" % " ".join(map(str, assign)))
fout.close()
