from solver import NodeGen
import random
import matplotlib.pyplot as plt
import networkx as nx

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
    CNF = generate_random_SAT(30, 30, 3)

    solver = NodeGen(30)
    nx.draw(solver.G, pos=nx.spring_layout(solver.G), with_labels=True)
    plt.show()

    result = solver.solve(CNF, 1)

    print(result)
