from solver import Solver, make_tree, make_graph
import random
import matplotlib.pyplot as plt
import networkx as nx
import pycosat

def generate_random_SAT(n_variables, n_clauses, max_literals_per_clause):
    CNF = []
    options = [i+1 for i in range(n_variables)]
    options += list(map(lambda x:-x, options))
    
    for i in range(n_clauses):
        clause = random.sample(options, k=max_literals_per_clause)
        
        for literal in clause:
            if -literal in clause:
                clause.remove(-literal)

        CNF.append(clause)

    return CNF

if __name__ == '__main__':
    n_variables = 7
    CNF = generate_random_SAT(n_variables, 40, 5)

    tree, clause_idx = make_tree(CNF)
    g = make_graph(n_variables)
    solver = Solver()

    print(CNF)    
    result = solver.solve(clause_idx, tree, g)
    print('DPLL', pycosat.solve(CNF))
    print(result)
