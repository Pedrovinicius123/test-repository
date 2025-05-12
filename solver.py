from ast import Assign
import time # for debugging
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

def unitary_propagation(CNF:list):
    assignments = set()
    for clause in CNF:
        if len(clause) == 1 and -list(clause)[0] not in assignments:
            assignments.add(list(clause)[0])
            
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
    paths = combinations(combs, len(CNF)-1)
    print('FINISHED')

    return paths

def P_SAT(CNF:list, assignments_previous=set()):
    print('A')
    paths = form_combinations_from_CNF(CNF)
    i = 0

    for path in paths:
        i += 1
        assignment = assignments_previous
        found = True
        break_all = False
        isolated = []

        for comb in path:
            if break_all:
                break

            literals = comb[0].intersection(comb[1])
            if not any(literals):
                isolated.extend([comb[0], comb[1]])

            for literal in literals:
                if -literal not in assignment:
                    assignment.add(literal)
                
                else:
                    break_all = True
                    found = False
                    break

        print(assignment)
        time.sleep(1)

        if isolated:
            
            isolated = test_assignments(isolated, assignment)
            res = unitary_propagation(isolated)
            
            if res:
                assignment = assignment.union(res)
                isolated = test_assignments(isolated, res)
            
            if not any(isolated):
                return assignment

            if not (check_contradiction(isolated) or check_empty(isolated)):
                result = P_SAT(isolated, assignments_previous=assignment)
                if result:
                    assignment = assignment.union(result)
                    return assignment

        if found:
            return assignment

    return False                
