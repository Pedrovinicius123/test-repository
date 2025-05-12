from solver import P_SAT
import random

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
    n_variables = 7
    CNF = generate_random_SAT(n_variables, 20, 3)

    print(CNF)    
    result = P_SAT(CNF=CNF)
    print(result)
