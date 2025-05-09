import networkx as nx
import copy, time # for debugging

from collections import defaultdict

def check_empty(CNF:list):
    for clause in CNF:
        if not any(clause):
            return True

    return False

def check_contradiction(CNF:list):
    for clause in CNF:
        if len(clause) == 1 and [-clause[0]] in CNF:
            return True

    return False

def get_most_recurrent(CNF:list):
    counter = defaultdict(int)
    for clause in CNF:
        for literal in clause:
            counter[abs(literal)] += 1

    return max(counter, key=counter.get)            

class NodeGen:
    def __init__(self, max_var):
        self.max_var = max_var
        self.i = 0
        self.G = nx.DiGraph()

    def solve(self, CNF:list, initial:int, relational=defaultdict(list)):
        CNF_copy = []
        for clause in CNF:
            if initial in clause:
                clause.remove(initial)
                relational[-initial].append(clause)

            elif -initial in clause:
                clause.remove(-initial)
                relational[initial].append(clause)

            else:
                CNF_copy.append(clause)

        if not (check_contradiction(relational[initial]) or check_empty(relational[initial])):
            relational[initial] = self.solve(relational[initial] + CNF_copy, get_most_recurrent(relational[initial] + CNF_copy))
        
        elif not (check_contradiction(relational[-initial]) or check_empty(relational[-initial])):
            relational[-initial] = self.solve(relational[-initial] + CNF_copy, get_most_recurrent(relational[-initial] + CNF_copy))

        return relational       