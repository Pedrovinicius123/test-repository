from solver import form_combinations_from_CNF, dict_cnf, Solver, test_assignments
import random, time


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
    n_variables = 20
    CNF = generate_random_SAT(n_variables, 50, 3)

    #print(pycosat.solve(list(map(list, CNF))))

    CNF_new = dict_cnf(CNF)
    paths = form_combinations_from_CNF(CNF_new)
    result = Solver().P_SAT(CNF_new, paths)

    if result:
        print(result)
        print(test_assignments(CNF_new, result))
        
