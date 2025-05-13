from solver import P_SAT, form_combinations_from_CNF
from dpll_traditional import dpll
import random, time

def generate_random_SAT(n_variables, n_clauses, max_literals_per_clause):
    CNF = []
    options = [i+1 for i in range(n_variables)]
    options += list(map(lambda x:-x, options))
    
    for i in range(n_clauses):
        clause = random.sample(options, k=max_literals_per_clause)
        
        for literal in clause:
            if -literal in clause:
                clause.remove(-literal)

        CNF.append(set(clause))

    return CNF

if __name__ == '__main__':
    n_variables = 50
    CNF = generate_random_SAT(n_variables, 300, 3)
    paths = form_combinations_from_CNF(CNF)

    print(dpll(CNF), len(paths)**3*(1/2) + len(paths)*(1/2), 2**n_variables)
    time.sleep(2)    
    
    solver = P_SAT(paths, CNF=CNF)
    print(solver.return_result())
