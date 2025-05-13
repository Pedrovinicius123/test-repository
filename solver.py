import time, copy, random # for debugging
from collections import defaultdict
from itertools import combinations
from sys import stdout

def check_empty(CNF:list):
    for clause in CNF:
        if len(clause) == 0:
            return True

    return False

def check_contradiction(CNF:list):
    for clause in CNF:
        if len(clause) == 1 and set([-list(clause)[0]]) in CNF:
            return True

    return False

def unitary_propagation(CNF:list, previous=[]):
    assignments = previous
    for clause in CNF:
        if len(clause) == 1 and -list(clause)[0] not in assignments:
            assignments.append(list(clause)[0])
            
        elif len(clause) == 1 and -list(clause)[0] in assignments:
            return False

    return assignments

def test_assignments(CNF:list, assignments:set):
    for literal in assignments:
        for clause in CNF:
            if literal in clause:
                CNF.remove(clause)

            elif -literal in clause:
                clause.remove(-literal)

    return CNF

def form_combinations_from_CNF(CNF:list):
    combs = combinations(CNF, 2)
    combinations_possible = []

    for comb in combs:
        value = comb[0].intersection(comb[1])
        if any(value):
            combinations_possible.append([value, comb[0], comb[1]])

    return combinations_possible

class P_SAT:
    def __init__(self, paths, CNF:list):
        self.i = 0
        self.CNF = CNF
        self.result = self.solve(paths, CNF)
        print(self.i)

    def return_result(self):
        if self.result:
            for clause in self.CNF:
                found = False
                for assignment in self.result:
                    if assignment in clause:
                        found = True
                        break

                if not found:
                    return False

            return self.result


    def solve(self, paths, CNF:list, assignments=[], visited=[], initial_index=0):        
        self.i += 1
        sub_CNF = []
        path_original = paths[initial_index]
        
        for idx, path in enumerate(paths):
            if any(p in path for p in path_original) and idx != initial_index and path not in visited:
                for literal in path[0]:
                    if -literal not in assignments:
                        new_CNF = test_assignments(copy.deepcopy(CNF), assignments+[literal])
                        new_assignments = []

                        while any(len(clause) == 1 for clause in new_CNF) and isinstance(new_assignments, list):
                            new_assignments = unitary_propagation(new_CNF, new_assignments+[literal])
                            if not isinstance(new_assignments, list) and not new_assignments:
                                return False

                            new_CNF = test_assignments(new_CNF, new_assignments+[literal])

                        if isinstance(new_assignments, list):
                            if not any(new_CNF):
                                return set(assignments + new_assignments)

                            if not (check_empty(new_CNF) or check_contradiction(new_CNF)):
                                result = None        
                                paths.remove(path)
                                if new_CNF == CNF:                                
                                    result = self.solve(paths.copy(), new_CNF, assignments=assignments+new_assignments+[random.choice(random.choice(list(map(list, new_CNF))))], initial_index=idx-1, visited=visited+[path_original])
                                else:
                                    result = self.solve(paths.copy(), new_CNF, assignments=assignments+new_assignments+[literal], initial_index=idx-1, visited=visited+[path_original])
                                
                                if result:
                                    return result                

        return False  
