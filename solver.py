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
        index_clauses[idx] = copy.deepcopy(clause[1:])
        d[clause[0]].append(idx)

    return d, index_clauses

def make_graph(n_vars:int):
    g = nx.DiGraph()
    for i in range(1, n_vars+1):
        g.add_edges_from([[(i-1), i], [(i-1), -i], [-(i-1), i], [-(i-1), -i]])

    return g

def unitary_propagation(CNF:dict):
    unitaries = set()
    idx_to_drop = set()

    for idx, value in CNF.items():
        if len(value) == 1 and -value[0] not in unitaries:
            unitaries.add(value[0])
            idx_to_drop.add(idx)

        elif len(value) > 1:
            for literal in value:
                if literal in unitaries:
                    idx_to_drop.add(idx)

                elif -literal in unitaries:
                    value.remove(literal)


    return unitaries, idx_to_drop

def apply_assignments(tree, CNF_copy:dict, assignments:set):
    ext_assignments = set()
    for assignment in assignments:
        idx_to_drop = set()

        if assignment in tree.keys():
            idx_to_drop = idx_to_drop.union(set(tree[neighbor]))

        for idx, clause in CNF_copy.items():
            if neighbor in clause:
                idx_to_drop.add(idx)

            elif -neighbor in clause:
                if len(clause) == 1:
                    for key, values in tree.items():
                        if idx in values and -key not in assignments:
                            idx_to_drop = idx_to_drop.union(set(values))
                            ext_assignments.add(key)
                        
                        elif -key in assignments:
                            break

                clause.remove(-neighbor)

        for assignment in ext_assignments:
            if assignment in tree.keys():
                idx_to_drop = idx_to_drop.union(tree[assignment])

            for idx, clause in CNF_copy.items():
                if assignment in clause:
                    idx_to_drop.add(idx)

                elif -assignment in clause:
                    clause.remove(-assignment)

    for idx in idx_to_drop:
        CNF_copy.pop(idx, -1)

    return CNF_copy, ext_assignments

def test_assignments(assignments:set, CNF_copy:dict, i):
    CNF_copy = CNF.copy()
        
    assignments.add(i)
    new, CNF_copy = unitary_propagation(CNF)
    assignments = assignments.union(new)

    CNF_copy, ext_assignments = apply_assignments(tree, CNF_copy=CNF_copy, assignments=assignments)
    assignments = assignments.union(ext_assignments)
    
    if not check_empty(CNF_copy):
        return CNF_copy, assignments

    elif not any(CNF_copy):
        return True, assignments

    return False

class Solver:
    def solve(self, CNF:dict, tree, g):
        self.traceback = 0
        result = self.dpllp(CNF, tree, g)

        return result, self.traceback

    def dpllp(self, CNF:dict, tree, assignments=set(), new_assignments=set(), i=0):
        self.traceback += 1
        result = test_assignments(assignments, CNF.copy(), i+1)
        
        if isinstance(result, bool) and result:
            assignments.add(i)
            return assignments

            assignments_copy = assignments.copy()
            assignments_copy = assignments_copy.union(ext_assignments)

            if -neighbor not in assignments:
                assignments_copy.add(neighbor)
            
            result = self.dpllp(CNF_copy.copy(), tree, assignments=assignments_copy)

            if result:
                return result

            return self.dpllp(CNF_copy.copy()), tree, current

        return False
    