class UnificationError(Exception):
    pass

def unify_variable(var, x, substitution):
    if var in substitution:
        return unify(substitution[var], x, substitution)
    elif x in substitution:
        return unify(var, substitution[x], substitution)
    else:
        substitution[var] = x
        return substitution

def unify(x, y, substitution=None):
    if substitution is None:
        substitution = {}

    if x == y:
        return substitution
    elif isinstance(x, str) and x[0].islower():
        return unify_variable(x, y, substitution)
    elif isinstance(y, str) and y[0].islower():
        return unify_variable(y, x, substitution)
    elif isinstance(x, tuple) and isinstance(y, tuple):
        if len(x) == len(y):
            for xi, yi in zip(x, y):
                substitution = unify(xi, yi, substitution)
            return substitution
    raise UnificationError("Unification failed")

# Example usage:
x = ('P', 'a', 'x')
y = ('P', 'y', 'mother(y)')

try:
    result = unify(x, y)
    print("Unification successful. Substitution:", result)
except UnificationError as e:
    print("Unification failed:", str(e))
