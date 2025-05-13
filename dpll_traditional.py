def dpll(clauses, assignment=None):
    if assignment is None:
        assignment = {}

    # Remove clauses that are already satisfied
    clauses = [clause for clause in clauses if not any(lit in assignment and assignment[lit] for lit in clause)]
    
    # If no clauses remain, the formula is satisfied
    if not clauses:
        return True, assignment

    # If there's an empty clause, the formula is unsatisfiable under the current assignment
    if any(len(clause) == 0 for clause in clauses):
        return False, {}

    # Unit Clause Propagation
    unit_clauses = [clause for clause in clauses if len(clause) == 1]
    while unit_clauses:
        unit = next(iter(unit_clauses[0]))  # Get the single literal
        value = unit > 0
        assignment[abs(unit)] = value
        clauses = simplify(clauses, unit)
        if any(len(clause) == 0 for clause in clauses):
            return False, {}
        unit_clauses = [clause for clause in clauses if len(clause) == 1]

    # Choose a literal (simple heuristic: first literal of first clause)
    for clause in clauses:
        for literal in clause:
            var = abs(literal)
            if var not in assignment:
                # Try assigning True
                new_assignment = assignment.copy()
                new_assignment[var] = literal > 0
                result, final_assignment = dpll(simplify(clauses, literal), new_assignment)
                if result:
                    return True, final_assignment

                # Try assigning False
                new_assignment = assignment.copy()
                new_assignment[var] = literal < 0
                result, final_assignment = dpll(simplify(clauses, -literal), new_assignment)
                if result:
                    return True, final_assignment

                return False, {}

    return True, assignment


def simplify(clauses, literal):
    """Simplifies the clause list given a literal assignment."""
    new_clauses = []
    for clause in clauses:
        if literal in clause:
            continue  # Clause is satisfied
        new_clause = clause - { -literal }
        new_clauses.append(new_clause)
    return new_clauses
