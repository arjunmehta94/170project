from anttsp import AntTSP
from antcolony import AntColony
from antgraph import AntGraph
from ant import Ant

T = 1 # number of test cases
fout = open ("answer.out", "w")
for t in xrange(1, T+1):
    fin = open(str(t) + ".in", "r")

    # find an answer, and put into assign
    tsp = AntTSP(fin.read())
    assign = tsp.findSolution()
    assign = str(assign)
    fout.write(assign)
fout.close()