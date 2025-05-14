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
        self.result = self.solve(paths, paths[0], CNF)
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
                    print('NO SATISFIED: ', clause)
                    return False

            return self.result


    def solve(self, paths, path_original, CNF:list, assignments=[]):        
        self.i += 1
        
        for idx, path in enumerate(paths):
            if any(p in path for p in path_original):
                for literal in path[0]:
                    if -literal not in assignments:
                        new_CNF = test_assignments(copy.deepcopy(CNF), assignments+[literal])
                        new_assignments = []

                        while any(len(clause) == 1 for clause in new_CNF) and isinstance(new_assignments, list):
                            new_assignments = unitary_propagation(new_CNF, assignments+new_assignments+[literal])
                            if not isinstance(new_assignments, list) and not new_assignments:
                                return False

                            new_CNF = test_assignments(new_CNF, assignments+new_assignments+[literal])

                        print("FORMULA: ", new_CNF)
                        time.sleep(1)                        

                        if isinstance(new_assignments, list):
                            if not (check_empty(new_CNF) or check_contradiction(new_CNF)):
                                if not any(new_CNF):
                                    return set(assignments + new_assignments + [literal])
                                
                                paths_copy = paths.copy()
                                paths_copy.remove(path)

                                if new_CNF == CNF:      
                                    for clause in new_CNF:
                                        for lit in clause:
                                            if lit not in set(assignments+new_assignments+[literal]):
                                                print("!")
                                                result = self.solve(paths_copy, path, new_CNF, assignments=list(set(assignments))+new_assignments+[literal, lit])
                                                if result:
                                                    return result

                                else:
                                    result = self.solve(paths_copy, path, new_CNF, assignments=list(set(assignments))+new_assignments+[literal])
                                
                                    if result:
                                        return result                

        return False  
