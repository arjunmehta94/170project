from anttsp import AntTSP
from antcolony import AntColony
from antgraph import AntGraph
from ant import Ant

T = 1 # number of test cases
fout = open ("answer.out", "w")
for t in xrange(1, T+1):
    fin = open("instances/6.in", "r") #+ str(t) + ".in", "r")

    # find an answer, and put into assign
    tsp = AntTSP(fin.read())
    assign = tsp.findSolution()
    assign = str(assign)
    fout.write(assign)
fout.close()

# 1B
# 2B
# 3B
# 4B
# 5B
# 6B
# 7B
# 8B
# 9R
# 10R
# 11R
# 12R
# 13R
# 14R
# 15R
# 16R