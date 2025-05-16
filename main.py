from solver import Solver
from factorial import calc_factorial_range
import random
import matplotlib.pyplot as plt


def generate_random_SAT(n_variables, n_clauses, max_literals_per_clause):
    CNF = []
    options = [i for i in range(1, n_variables)]
    options += list(map(lambda x:-x, options))
    
    for i in range(n_clauses):
        clause = random.sample(options, k=max_literals_per_clause)
        
        for literal in clause:
            if -literal in clause:
                clause.remove(-literal)

        CNF.append(set(clause))

    return CNF

if __name__ == '__main__':
    n_variables = 30
    CNF = generate_random_SAT(n_variables, 100, 3)
    #print(pycosat.solve(list(map(list, CNF))))

    for i in range(100):
        solver = Solver(CNF)
        print(solver.contradictions, len(solver.combs))
        calc_factorial_range(len(solver.combs))


