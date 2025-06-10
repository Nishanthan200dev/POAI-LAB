def unify(x, y, theta={}):
    if theta is None:
        return None
    elif x == y:
        return theta
    elif isinstance(x, str) and x.islower():  # x is a variable
        return unify_var(x, y, theta)
    elif isinstance(y, str) and y.islower():  # y is a variable
        return unify_var(y, x, theta)
    elif isinstance(x, list) and isinstance(y, list) and len(x) == len(y):
        return unify(x[1:], y[1:], unify(x[0], y[0], theta))
    else:
        return None

def unify_var(var, x, theta):
    if var in theta:
        return unify(theta[var], x, theta)
    elif x in theta:
        return unify(var, theta[x], theta)
    else:
        theta[var] = x
        return theta

# Backward chaining resolution function
def resolution(kb, query):
    for clause in kb:
        head = clause[0]
        body = clause[1:]
        theta = unify(head, query, {})
        if theta is not None:
            if not body:
                return True  # Fact found
            # Check all subgoals recursively
            all_resolved = True
            for subgoal in body:
                # Apply substitution theta to subgoal
                subgoal_inst = [theta.get(term, term) for term in subgoal]
                if not resolution(kb, subgoal_inst):
                    all_resolved = False
                    break
            if all_resolved:
                return True
    return False

# Knowledge base with implications (format: [head, body1, body2, ...])
knowledge_base = [
    [["Mortal", "x"], ["Human", "x"]],  # Human(x) → Mortal(x)
    [["Human", "John"]],               # Human(John)
]

# Query: Mortal(John)?
query = ["Mortal", "John"]

# Apply resolution
if resolution(knowledge_base, query):
    print("Query is resolved: John is Mortal")
else:
    print("Query could not be resolved")
