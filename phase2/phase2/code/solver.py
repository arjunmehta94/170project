from anttsp import AntTSP
from antcolony import AntColony
from antgraph import AntGraph
from ant import Ant


T = 495 # number of test cases
fout = open ("answer.out", "w")
for t in xrange(1, T+1):
	#print t
	doubleDigit = False
	fin = open("instances/" + str(t) + ".in", "r")# + str(t) + ".in", "r")
	#fin = open("instances/" + str(t) + ".in", "r")
	N = int(fin.readline())
	d = [[] for i in range(N)]
	for i in xrange(N):
	    d[i] = [int(x) for x in fin.readline().split()]
	c = fin.readline()
	#print d
	tsp = AntTSP(N,d,c)

	assign = tsp.findSolution()
	if assign[-1] < 10:
		doubleDigit = True
	else:
		doubleDigit = False
	assign = str(assign).split(', ')
	assign[0] = assign[0][1:]
	if doubleDigit:
		assign[-1] = assign[-1][0:1]
	else:
		assign[-1] = assign[-1][0:2]
	# find an answer, and put into assign
	# assign = [0] * N
	# for i in xrange(N):
	#     assign[i] = i+1

	fout.write("%s\n" % " ".join(map(str, assign)))
fout.close()

