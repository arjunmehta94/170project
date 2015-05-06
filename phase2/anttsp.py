from antcolony import AntColony
from antgraph import AntGraph

import pickle
import sys
import traceback
import re

class AntTSP:
    
    def __init__(self, input_str):
        self.num_nodes = 0
        self.num_ants = 0
        self.num_iterations = 0
        self.num_repetitions = 0
        self.color_mat = []
        self.cost_mat = [] 
        matchObj = re.match("^(\d*)\n([\d\s]+)\n([a-zA-Z]+)$", input_str)        
        if(matchObj):
            self.num_nodes = eval(matchObj.group(1))
            cost_mat_prep = matchObj.group(2)
            #self.cost_mat = [[0 for x in range(self.num_nodes)] for x in range(self.num_nodes)]
            self.cost_mat = cost_mat_prep.split("\n", self.num_nodes)
            for i in range(0,self.num_nodes):
                self.cost_mat[i] = self.cost_mat[i].split(" ")
            
            for x in range(0,self.num_nodes):
                for y in range(0,self.num_nodes):
                    self.cost_mat[x][y] = int(self.cost_mat[x][y])

           
            self.color_mat = matchObj.group(3)
        else:
            print "Exception: Invalid String"
            return

        if self.num_nodes <= 10:
            self.num_ants = 20
            self.num_iterations = 12
            self.num_repetitions = 1
        else:
            self.num_ants = 28
            self.num_iterations = 20
            self.num_repetitions = 1

        if self.num_nodes < len(self.cost_mat):
            self.cost_mat = self.cost_mat[0:self.num_nodes]
            self.color_mat = self.color_mat[0:self.num_nodes]
            for i in range(0, self.num_nodes):
                self.cost_mat[i] = self.cost_mat[i][0:self.num_nodes]

    def findSolution(self):
        try:
            graph = AntGraph(self.num_nodes, self.cost_mat, self.color_mat)
            best_path_vec = None
            best_path_cost = sys.maxint
            for i in range(0, self.num_repetitions):
                graph.reset_tau()
                ant_colony = AntColony(graph, self.num_ants, self.num_iterations)
                ant_colony.start()
                if ant_colony.best_path_cost < best_path_cost:
                    best_path_vec = ant_colony.best_path_vec
                    best_path_cost = ant_colony.best_path_cost
            return best_path_vec

        except Exception, e:
            print "exception: " + str(e)
            traceback.print_exc()