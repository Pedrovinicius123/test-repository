from solver import P_SAT, form_combinations_from_CNF
import random, pycosat, time

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
    n_variables = 20
    CNF = generate_random_SAT(n_variables, 50, 3)

    print(pycosat.solve(list(map(list, CNF))))
    time.sleep(2)    
    paths = form_combinations_from_CNF(CNF)
    solver = P_SAT(paths, CNF=CNF)
    result = solver.return_result()
    print('RESULT: ', result)
    
    if result:
        for literal in result:
            if -literal in result:
                print("OOOOPAAAA!!")
                break
        
        
