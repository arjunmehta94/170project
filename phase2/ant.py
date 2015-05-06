import math
import random
import sys
from threading import *

class Ant(Thread):
    def __init__(self, ID, start_node, colony):
        Thread.__init__(self)
        self.ID = ID
        self.start_node = start_node
        self.colony = colony

        self.curr_node = self.start_node
        self.graph = self.colony.graph
        self.path_vec = []
        self.path_vec.append(self.start_node)
        self.path_cost = 0
        self.last1 = None
        self.last2 = None
        self.last3 = None
        # same meaning as in standard equations
        self.Beta = 1
        #self.Q0 = 1  # Q0 = 1 works just fine for 10 city case (no explore)
        self.Q0 = 0.5
        self.Rho = 0.99

        # store the nodes remaining to be explored here
        self.nodes_to_visit = {}

        for i in range(0, self.graph.num_nodes):
            if i != self.start_node:
                self.nodes_to_visit[i] = i

        # create n X n matrix 0'd out to start
        self.path_mat = []

        for i in range(0, self.graph.num_nodes):
            self.path_mat.append([0]*self.graph.num_nodes)

    # overide Thread's run()
    def run(self):
        graph = self.colony.graph
        while not self.end():
            # we need exclusive access to the graph
            graph.lock.acquire()
            new_node = self.state_transition_rule(self.curr_node)
            self.path_cost += graph.delta(self.curr_node, new_node)

            self.path_vec.append(new_node)
            self.path_mat[self.curr_node][new_node] = 1  #adjacency matrix representing path

            self.local_updating_rule(self.curr_node, new_node)
            graph.lock.release()

            self.curr_node = new_node


        # don't forget to close the tour
        self.path_cost += graph.delta(self.path_vec[-1], self.path_vec[0])

        # send our results to the colony
        self.colony.update(self)

        # allows thread to be restarted (calls Thread.__init__)
        self.__init__(self.ID, self.start_node, self.colony)

    def end(self):
        return not self.nodes_to_visit 

    # described in report -- determines next node to visit after curr_node
    def state_transition_rule(self, curr_node):
        graph = self.colony.graph
        q = random.random()
        max_node = -1

        if q < self.Q0:
            print "Ant", self.ID, "continues on its journey!"
            max_val = -1
            val = None

            for node in self.nodes_to_visit.values():
                if graph.tau(curr_node, node) == 0:
                    raise Exception("tau = 0")

                val = graph.tau(curr_node, node) * math.pow(graph.etha(curr_node, node), self.Beta)
                if val > max_val:
                    max_val = val
                    max_node = node
        else:
            losers = []
            while 1:
                sum = 0
                node = -1

                for node in self.nodes_to_visit.values():
                    if node in losers:
                        continue
                    if graph.tau(curr_node, node) == 0:
                        raise Exception("tau = 0")
                    sum += graph.tau(curr_node, node) * math.pow(graph.etha(curr_node, node), self.Beta)
                if sum == 0:
                    raise Exception("sum = 0")

                avg = sum / len(self.nodes_to_visit)

                

                for node in self.nodes_to_visit.values():
                    if node in losers:
                        continue
                    p = graph.tau(curr_node, node) * math.pow(graph.etha(curr_node, node), self.Beta) 
                    if p > avg:
                        
                        max_node = node

                
                if max_node == -1:
                    max_node = node
                if self.last1 == None or self.last2 == None or self.last3 == None:    
                    break
                if graph.color(self.last1) == graph.color(self.last2) == graph.color(self.last3) == graph.color(max_node) :
                    losers.append(max_node)
                else:
                    break

        self.last1 = self.last2
        self.last2 = self.last3
        self.last3 = max_node

        if max_node < 0:
            raise Exception("max_node < 0")

        del self.nodes_to_visit[max_node]
        


        return max_node

    # phermone update rule for indiv ants
    def local_updating_rule(self, curr_node, next_node):
        graph = self.colony.graph
        val = (1 - self.Rho) * graph.tau(curr_node, next_node) + (self.Rho * graph.tau0)
        graph.update_tau(curr_node, next_node, val)

