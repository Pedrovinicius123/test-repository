import time, copy, random # for debugging
from collections import defaultdict
from itertools import combinations
from sys import stdout

def check_empty(CNF:dict):
    for clause in CNF.values():
        if len(clause) == 0:
            return True

    return False

def check_contradiction(CNF:dict):
    for clause in CNF.values():
        if len(clause) == 1 and set([-list(clause)[0]]) in CNF.values():
            return True

    return False

def unitary_propagation(CNF:dict, assignments=set()):
    while True:
        idx_to_drop = set()

        for idx, clause in CNF.items():
            if len(clause) == 1 and -list(clause)[0] not in assignments:
                assignments.add(list(clause)[0])
                idx_to_drop.add(idx)

            elif any(literal in assignments for literal in clause):
                idx_to_drop.add(idx)
                
            elif len(clause) == 1 and -list(clause)[0] in assignments:
                return False, CNF

        for i in idx_to_drop:
            CNF.pop(i)

        if not any(CNF) or not any(idx_to_drop):
            return assignments, CNF            

def test_assignments(CNF:dict, assignments:set):
    idx_to_drop = set()
    for literal in assignments:
        for idx, clause in CNF.items():
            if literal in clause:
                idx_to_drop.add(idx)

            elif -literal in clause:
                clause.remove(-literal)

    for idx in idx_to_drop:
        CNF.pop(idx)

    return CNF

def complement(clause1, clause2):
    copy1 = clause1.copy()
    copy2 = clause2.copy()

    inter = set(copy1).intersection(set(copy2))

    for literal in inter:
        copy1.remove(literal)
        copy2.remove(literal)

    return inter, [copy1] + [copy2]

def dict_cnf(CNF:list):
    CNF_new = {}
    for idx, clause in enumerate(CNF):
        CNF_new[idx] = clause

    return CNF_new

def form_combinations_from_CNF(CNF:dict):
    combinations_possible = defaultdict(set)
    for comb in combinations(CNF, 2):
        value, comp = complement(CNF[comb[0]], CNF[comb[1]])
        if any(value):
            combinations_possible[frozenset(value)] = combinations_possible[frozenset(value)].union(set([comb[0]] + [comb[1]]))

    return combinations_possible

class Solver:
    def __init__(self):
        self.iterations = 0

    def P_SAT(self, CNF:dict, combinations_possible, assignments=set(), recursive=1):
        for key, combinations in combinations_possible.items():
            self.iterations += 1
            if not any(-k in assignments for k in key):
                #print(recursive, key)
                CNF_copy = copy.deepcopy(CNF)
                CNF_copy = test_assignments(CNF_copy, assignments.union(key))
                
                idx_to_drop = set()
                idx_to_drop = idx_to_drop.union(combinations)
                new_assignments, CNF_copy = unitary_propagation(CNF_copy, assignments.union(key))

                print(CNF_copy, f'{key}, {combinations}', "\n")
                
                if len(CNF_copy) < 10:
                    time.sleep(1)

                if new_assignments:
                    print('\n', CNF_copy, '\n\n', assignments.union(key).union(new_assignments))
                    time.sleep(1)

                    new_ = assignments.union(new_assignments).union(key)
                    CNF_copy = test_assignments(CNF_copy, assignments)
                    
                    if not (check_contradiction(CNF_copy) or check_empty(CNF_copy)):
                        if not any(CNF_copy):
                            return new_

                        new_combinations = form_combinations_from_CNF(CNF_copy)
                        
                        if not any(new_combinations):
                            for clause in CNF_copy.values():
                                for literal in clause:
                                    if -literal not in new_:
                                        new_.add(literal)
                                        break

                            return new_


                        result = self.P_SAT(CNF_copy, new_combinations, assignments=new_, recursive=recursive+1)

                        if result:
                            assignments = assignments.union(result).union(new_assignments).union(key)
                            return assignments

        return False
    