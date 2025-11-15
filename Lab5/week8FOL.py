# Simple Forward Chaining for the "Robert is Criminal" problem

facts = {
    "American(Robert)",
    "Missile(T1)",
    "Owns(A, T1)",
    "Enemy(A, America)"
}

rules = [
    (["Missile(x)"], "Weapon(x)"),
    
    (["Missile(x)", "Owns(A, x)"], "Sells(Robert, x, A)"),
    
    (["Enemy(r, America)"], "Hostile(r)"),
    
    (["American(p)", "Weapon(q)", "Sells(p, q, r)", "Hostile(r)"], "Criminal(p)")
]


def match(pattern, fact):
    if "(" not in pattern:
        return pattern == fact
    
    pname, pvals = pattern.split("(")
    pvals = pvals[:-1].split(",")

    fname, fvals = fact.split("(")
    fvals = fvals[:-1].split(",")

    if pname != fname or len(pvals) != len(fvals):
        return None

    mapping = {}
    for p, f in zip(pvals, fvals):
        p, f = p.strip(), f.strip()
        if p.islower():  # variable
            mapping[p] = f
        elif p != f:
            return None
    return mapping


def substitute(conclusion, subs):
    pred, args = conclusion.split("(")
    args = args[:-1].split(",")
    new_args = [subs.get(a.strip(), a.strip()) for a in args]
    return pred + "(" + ", ".join(new_args) + ")"


def forward_chain():
    added = True
    while added:
        added = False
        for conditions, conclusion in rules:
            for fact_set in zip(*[facts]*len(conditions)):
                subs = {}
                valid = True
                for cond in conditions:
                    matched = False
                    for f in facts:
                        m = match(cond, f)
                        if m is not None:
                            subs.update(m)
                            matched = True
                            break
                    if not matched:
                        valid = False
                        break

                if valid:
                    new_fact = substitute(conclusion, subs)
                    if new_fact not in facts:
                        facts.add(new_fact)
                        added = True

    return facts


final_facts = forward_chain()
print("\nFinal Facts:")
for f in final_facts:
    print(f)

print("\nIs Robert criminal?", "Criminal(Robert)" in final_facts)
