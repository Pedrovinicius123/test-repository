import networkx as nx
import copy, time # for debugging
from collections import defaultdict
from rich.pretty import pprint
from sys import stdout

def check_empty(CNF:dict):
    for clause in CNF.values():
        if not any(clause):
            return True

    return False

def check_contradiction(CNF:dict):
    for clause in CNF.values():
        if len(clause) == 1 and [-clause[0]] in CNF.values():
            return True

    return False

def make_tree(CNF:list):
    d = defaultdict(list)
    index_clauses = {}

    for idx, clause in enumerate(CNF):
        index_clauses[idx] = copy.deepcopy(clause)
        d[clause[0]].append(idx)

    return d, index_clauses

def make_graph(n_vars:int):
    g = nx.DiGraph()
    for i in range(1, n_vars+1):
        g.add_edges_from([[(i-1), i], [(i-1), -i], [-(i-1), i], [-(i-1), -i]])

    return g

class Solver:
    def solve(self, CNF:dict, tree, g):
        self.traceback = 0
        result = self.dpllp(CNF, tree, g)

        return result, self.traceback

    def dpllp(self, CNF:dict, tree, g, current=0, assignments=set()):
        for neighbor in g.neighbors(current):
            if -neighbor in assignments:
                continue

            idx_to_drop = set()
            if neighbor in tree.keys():
                idx_to_drop = idx_to_drop.union(set(tree[neighbor]))

            CNF_copy = copy.deepcopy(CNF)
            
            for idx, clause in CNF_copy.items():
                if neighbor in clause:
                    idx_to_drop.add(idx)

                elif -neighbor in clause:
                    if len(clause) == 1:
                        for key, values in tree.items():
                            if idx in values and -key not in assignments:
                                idx_to_drop = idx_to_drop.union(set(values))
                                assignments.add(key)
                            
                            elif -key in assignments:
                                break

                    clause.remove(-neighbor)

            for idx in idx_to_drop:
                CNF_copy.pop(idx, -1)

            time.sleep(1)
            

            self.traceback += 1

            stdout.write("\rITERAÇÕES %d\n" % self.traceback)
            stdout.flush()

            print("ATRIBUIÇÕES: ", end=' ')
            pprint(assignments.union(set([neighbor])))
            print('\n')

            if not any(CNF_copy):
                assignments.add(neighbor)
                return assignments

            if not (check_empty(CNF_copy) or check_contradiction(CNF_copy)):
                assignments_copy = assignments.copy()
                if -neighbor not in assignments:
                    assignments_copy.add(neighbor)
                
                result = self.dpllp(CNF_copy.copy(), tree, g, current=neighbor, assignments=assignments_copy)

                if result:
                    return result

        return False
    