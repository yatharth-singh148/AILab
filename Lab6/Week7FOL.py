# Simple Unification Algorithm

def unify(expr1, expr2, subs={}):
    # If both expressions already match, return current substitutions
    if expr1 == expr2:
        return subs

    # If expr1 is a variable
    if isinstance(expr1, str) and expr1.islower():
        return unify_var(expr1, expr2, subs)

    # If expr2 is a variable
    if isinstance(expr2, str) and expr2.islower():
        return unify_var(expr2, expr1, subs)

    # If both are functions/predicates
    if isinstance(expr1, tuple) and isinstance(expr2, tuple):
        if expr1[0] != expr2[0] or len(expr1[1]) != len(expr2[1]):
            return None  # Predicate mismatch

        for a, b in zip(expr1[1], expr2[1]):
            subs = unify(a, b, subs)
            if subs is None:
                return None
        return subs

    return None


def unify_var(var, expr, subs):
    if var in subs:
        return unify(subs[var], expr, subs)

    if isinstance(expr, str) and expr in subs:
        return unify(var, subs[expr], subs)

    # Prevent x = f(x)
    if occurs_check(var, expr, subs):
        return None

    subs[var] = expr
    return subs


def occurs_check(var, expr, subs):
    if var == expr:
        return True
    if isinstance(expr, tuple):
        return any(occurs_check(var, arg, subs) for arg in expr[1])
    return False


# Example:
expr1 = ("Eats", ["x", "Apple"])
expr2 = ("Eats", ["Riya", "y"])

result = unify(expr1, expr2)
print("Unification Result:", result)
