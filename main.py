from solver import NodeGen
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

        CNF.append(clause)

    return CNF

if __name__ == '__main__':
    CNF = generate_random_SAT(4, 10, 3)

    print(CNF)
    solver = NodeGen(4)
    result = solver.solve(CNF)

    print(result)
