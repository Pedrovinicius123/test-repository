from collections import defaultdict
from itertools import combinations
from factorial import calc_factorial_range
from rich.pretty import pprint
import time, copy, random

def check_contradiction(CNF):
    for clause in CNF:
        if len(clause) == 1 and [-list(clause)[0]] in CNF:
            return True

    return False

def check_empty(CNF):
    for clause in CNF:
        if len(clause) == 0:
            return True

    return False

def test(assignments, CNF):
    for clause in CNF:
        found = False

        for literal in assignments:
            if literal in clause:
                found = True
                break

        if not found:
            print(clause)
            return False

    return True

def count_most_reccurent(CNF, assignments=[]):
    rec = defaultdict(int)

    for clause in CNF:
        for literal in clause:
            if -literal not in assignments:
                rec[literal] += 1

    if any(rec):
        return max(rec, key=rec.get)
    return False

class Solver:
    def __init__(self, CNF):
        self.CNF = CNF
        self.iterations = 1
        result = self.make_simplification(CNF)
        pprint(result)
        print('INTERATIONS', self.iterations)
        #print(stringify_tree(result))

    def make_simplification(self, CNF, assignments=[]):
        print(CNF)
        self.iterations += 1 
        time.sleep(0.1)
        if all(len(clause) <= 1 for clause in CNF):
            return CNF

        most_reccurent = count_most_reccurent(CNF, assignments=assignments)
        simpl = defaultdict(list)              

        if not most_reccurent or check_contradiction(CNF):
            return False
        
        for clause in CNF:
            clause_copy = clause.copy()

            if most_reccurent in clause:
                clause_copy.remove(most_reccurent)
                simpl[most_reccurent].append(clause_copy)

            elif -most_reccurent in clause:
                clause_copy.remove(-most_reccurent)
                simpl[-most_reccurent].append(clause_copy)

            if any(clause_copy):
                simpl[most_reccurent].append(clause_copy)
                continue

            CNF.remove(clause)

        for key in simpl.keys():
            result = self.make_simplification(simpl[key], assignments=assignments+[key])
            simpl[key] = result

        return simpl
                