import math# for debugging
from collections import defaultdict
from itertools import combinations

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
        value, comp = complement(comb[0], comb[1])
        if any(value):
            combinations_possible[frozenset(value)] = combinations_possible[frozenset(value)].union(set([frozenset(comp[0])] + [frozenset(comp[1])]))

    return combinations_possible

def form_paths_from_combinations(combs):
    literals_pool = set()
    contradictions = 0

    for key in combs.keys():
        for literal in key:
            if -literal in literals_pool and literal not in literals_pool:
                contradictions += 1

            else:
                literals_pool.add(literal)

    paths = combinations(combs.keys(), (contradictions if contradictions > 0 else 1))
    return paths, contradictions


class Solver:
    def __init__(self, CNF):
        self.combs = form_combinations_from_CNF(CNF)
        self.paths, self.contradictions = form_paths_from_combinations(self.combs)
        print('NICE')
        print(math.factorial(len(self.combs))/ (math.factorial(self.contradictions) * math.factorial(len(self.combs) - self.contradictions)))
