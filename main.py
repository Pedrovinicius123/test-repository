from solver import Solver
from factorial import calc_factorial_range, calc_iterations
from rich.pretty import pprint

import random, math, pycosat
import matplotlib.pyplot as plt
import sympy as sp



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
    CNF  = generate_random_SAT(n_variables=n_variables, n_clauses=50, max_literals_per_clause=3)
    print(pycosat.solve(list(map(list, CNF)))) 
    #print(calc_iterations(n_variables), 2**n_variables)
    
    solver = Solver(CNF)
    #if isinstance(solver.result, list):
