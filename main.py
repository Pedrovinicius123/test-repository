from solver import Solver
from rich.pretty import pprint

import random, math, pycosat, time
import matplotlib.pyplot as plt
import sympy as sp
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
    n_variables = 20
    times, sizes = [], []

    for i in range(3, n_variables):
        print(i)
        times_inner = []
        for j in range(10, 100):
            #print(j)   
            CNF  = generate_random_SAT(n_variables=i, n_clauses=j, max_literals_per_clause=3)
            #print(f'time pycosat: {b-a}')
            solver = Solver(CNF)
            times_inner.append(solver.iterations)

        times.append(max(times_inner))
        sizes.append(i)

    plt.scatter(sizes, times)
    space = np.linspace(min(sizes), max(sizes), 1000)
    plt.plot(space, 2**space, color='red')

    plt.ylabel("Tempo gasto")
    plt.xlabel("Tamanho dos dados")

    plt.show()

    #if isinstance(solver.result, list):
