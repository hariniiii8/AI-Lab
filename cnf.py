from sympy import symbols, And, Or, Equivalent, Not, to_cnf

def fol_to_cnf(fol_formula):
    # Assuming fol_formula is a propositional logic formula
    # Convert the formula to CNF using sympy
    cnf_formula = to_cnf(fol_formula)
    return cnf_formula

# Example usage
P, Q, R = symbols('P Q R')

# FOL formula: P <=> (Q & R)
fol_formula = Equivalent(P, And(Q,R))

# Convert to CNF
cnf_formula = fol_to_cnf(fol_formula)

print("FOL Formula:", fol_formula)
print("CNF Formula:", cnf_formula)
