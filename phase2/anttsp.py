from antcolony import AntColony
from antgraph import AntGraph

import pickle
import sys
import traceback
import re

class AntTSP:
    def __init__(self, input_str):

        matchObj = re.match("^(\d*)\n([\d\s]+)\n([a-zA-Z]+)$", input_str)        
        if(matchObj):
            num_nodes = matchObj.group(1)
            cost_mat = matchObj.group(2)
            color_mat = matchObj.group(3)
        
        if num_nodes <= 10:
            num_ants = 20
            num_iterations = 12
            num_repetitions = 1
        else:
            num_ants = 28
            num_iterations = 20
            num_repetitions = 1

        if num_nodes < len(cost_mat):
            cost_mat = cost_mat[0:num_nodes]
            for i in range(0, num_nodes):
                cost_mat[i] = cost_mat[i][0:num_nodes]

        try:
            graph = AntGraph(num_nodes, cost_mat, color_mat)
            best_path_vec = None
            best_path_cost = sys.maxint
            for i in range(0, num_repetitions):
                graph.reset_tau()
                ant_colony = AntColony(graph, num_ants, num_iterations)
                ant_colony.start()
                if ant_colony.best_path_cost < best_path_cost:
                    best_path_vec = ant_colony.best_path_vec
                    best_path_cost = ant_colony.best_path_cost

        except Exception, e:
            print "exception: " + str(e)
            traceback.print_exc()
