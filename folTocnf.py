def eliminate_implications(fol_formula):
    # Replace implications with equivalent disjunctions
    return Or(Not(fol_formula.args[0]), fol_formula.args[1])

def move_negations_inwards(fol_formula):
    # Apply De Morgan's laws to move negations inward
    if fol_formula.func == Not:
        if fol_formula.args[0].func == And:
            return Or(*[move_negations_inwards(Not(arg)) for arg in fol_formula.args[0].args])
        elif fol_formula.args[0].func == Or:
            return And(*[move_negations_inwards(Not(arg)) for arg in fol_formula.args[0].args])
    elif fol_formula.func in (And, Or):
        return fol_formula.func(*[move_negations_inwards(arg) for arg in fol_formula.args])
    return fol_formula

def distribute_disjunctions(fol_formula):
    # Apply distributive laws
    if fol_formula.func == Or and any(arg.func == And for arg in fol_formula.args):
        and_arg = next(arg for arg in fol_formula.args if arg.func == And)
        other_args = [arg for arg in fol_formula.args if arg != and_arg]
        return And(*[Or(*[sub_arg | other_arg for other_arg in other_args]) for sub_arg in and_arg.args])
    elif fol_formula.func in (And, Or):
        return fol_formula.func(*[distribute_disjunctions(arg) for arg in fol_formula.args])
    return fol_formula

def fol_to_cnf(fol_formula):
    # Convert FOL formula to CNF using custom implementation
    cnf_formula = eliminate_implications(fol_formula)
    cnf_formula = move_negations_inwards(cnf_formula)
    cnf_formula = distribute_disjunctions(cnf_formula)
    return cnf_formula

# Example usage
P, Q, R = symbols('P Q R')

# FOL formula: P <=> (Q & R)
fol_formula = Equivalent(P, And(Q, R))

# Convert to CNF using custom implementation
cnf_formula = fol_to_cnf(fol_formula)

print("FOL Formula:", fol_formula)
print("CNF Formula:", cnf_formula)
