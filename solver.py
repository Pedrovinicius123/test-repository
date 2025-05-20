from collections import defaultdict
from itertools import combinations
from rich.pretty import pprint
import time, copy, random, pycosat

def check_contradiction(CNF, assignments=[]):
    for clause in CNF:
        if len(clause) == 1 and ([-list(clause)[0]] in CNF or -list(clause)[0] in assignments):
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
            #print(clause)
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

def unit_propagation(CNF, assignments=[]):
    while any(CNF):
        for clause in CNF:
            if not any(clause) or (len(clause) == 1 and -list(clause)[0] in assignments):
                return False

            if len(clause) == 1:
                assignments.append(list(clause)[0])
                assignments = list(set(assignments))
                CNF.remove(clause)

            for assign in assignments:
                if assign in clause:
                    CNF.remove(clause)

                elif -assign in clause:
                    clause.remove(-assign)

    return assignments

class Solver:
    def __init__(self, CNF):
        self.CNF = CNF
        self.iterations = 1
        result = self.make_simplification(CNF)
        #pprint(pycosat.solve(list(map(list, CNF))))
        
        #if isinstance(result, list):
        #    pprint(result)
        #    pprint(test(result, self.CNF))

        #final = self.solve_by_simplification(result)
        #if final:
        #    pprint(final)
        #    

        #time.sleep(0.1)

        #print('INTERATIONS', self.iterations)
        #print(stringify_tree(result))

    def make_simplification(self, CNF, assignments=[]):
        #print(CNF)
        self.iterations += 1 
        if all(len(clause) <= 2 for clause in CNF):
            result = pycosat.solve(list(map(list,CNF)))
            if result != 'UNSAT':
                for lit in result:
                    if -lit not in assignments:
                        assignments.append(lit)

                return list(set(sorted(assignments, key=abs)))

            return False

        most_reccurent = count_most_reccurent(CNF)
        #print(most_reccurent)
        simpl = defaultdict(list)              
        
        for clause in CNF:
            clause_copy = clause.copy()
            #print(clause, most_reccurent)
            #time.sleep(1)

            if most_reccurent in clause:
                clause_copy.remove(most_reccurent)
                simpl[-most_reccurent].append(clause_copy)

            elif -most_reccurent in clause:
                clause_copy.remove(-most_reccurent)
                simpl[most_reccurent].append(clause_copy)

            elif any(clause_copy):
                simpl[most_reccurent].append(clause_copy)                
                simpl[-most_reccurent].append(clause_copy)
                

        for key in simpl.keys():
            result = self.make_simplification(simpl[key], assignments=assignments+[key])
            if isinstance(result, list):
                return result

        return simpl
