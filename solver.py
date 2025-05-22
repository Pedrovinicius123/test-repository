from collections import defaultdict

def solve_SAT(CNF:list):
    reversed_literals = defaultdict(set)

    for idx, clause in enumerate(CNF):
        for literal in clause:
            reversed_literals[abs(literal)].add(idx + 1 if literal > 0 else -(idx + 1))

    changed, change = set(), set()
    assignments = set()
    for literal, clauses in reversed_literals.items():
        change = change.union(set(filter(lambda x: x>0, clauses)))
        if len(change) == len(CNF):
            assignments.add(literal)
            return assignments
        
        elif change != changed:
            assignments.add(literal)

        elif change == changed:
            assignments.add(-literal)
            change = change.union(set(map(abs, filter(lambda x: x<0, clauses))))

        changed = change.copy()

    return assignments
