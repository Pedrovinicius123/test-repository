from solver import solve_SAT
from rich.pretty import pprint

import random
import matplotlib.pyplot as plt
import numpy as np


def generate_random_SAT(n_variables, n_clauses, max_literals_per_clause):
    CNF = []
    options = [i for i in range(1, n_variables+1)]
    options += list(map(lambda x:-x, options))
    
    for i in range(n_clauses):
        incorrect = True

        while incorrect:
            incorrect = False
            clause = random.sample(options, k=max_literals_per_clause)
            
            for literal in clause:
                if -literal in clause:
                    incorrect = True

        CNF.append(set(clause))

    return CNF

if __name__ == '__main__':
    n_variables = 5
    times, sizes = [], []

    CNF = generate_random_SAT(n_variables, 7, 3)
    print(CNF)
    print(solve_SAT(CNF))

    #if isinstance(solver.result, list):
