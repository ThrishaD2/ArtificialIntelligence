def unify(term1, term2, substitution=None):
    if substitution is None:
        substitution = {}

    if term1 == term2:
        return substitution

    if isinstance(term1, str) and term1.islower():  # term1 is a variable
        return unify_var(term1, term2, substitution)

    if isinstance(term2, str) and term2.islower():  # term2 is a variable
        return unify_var(term2, term1, substitution)

    if isinstance(term1, list) and isinstance(term2, list) and len(term1) == len(term2) and term1[0] == term2[0]:
        for i in range(1, len(term1)):
            substitution = unify(term1[i], term2[i], substitution)
            if substitution is None:
                return None
        return substitution

    return None

def unify_var(var, term, substitution):
    if var in substitution:
        return unify(substitution[var], term, substitution)
    elif isinstance(term, str) and term in substitution: # Add check for string before using term as a dictionary key
        return unify(var, substitution[term], substitution)
    elif occurs_check(var, term, substitution):
        return None
    else:
        substitution[var] = term
        return substitution

def occurs_check(var, term, substitution):
    if var == term:
        return True
    if isinstance(term, str) and term in substitution:
        return occurs_check(var, substitution[term], substitution)
    if isinstance(term, list):
        for t in term:
            if occurs_check(var, t, substitution):
                return True
    return False
####OUESTION 1######
term1_1 = ["P", "a", "x", ["f", ["g", "y"]]]
term2_1 = ["P", "z", ["f", "z"], ["f", "u"]]

substitution_1 = unify(term1_1, term2_1)

if substitution_1 is not None:
    print("Unification is possible for the first pair.")
    print("Substitution:", substitution_1)
else:
    print("Unification is not possible for the first pair.")

OUTPUT:
Unification is possible for the first pair.
Substitution: {'a': 'z', 'x': ['f', 'z'], 'u': ['g', 'y']}

####QUESTION 2####
term1_2 = ["Q", ["f", "a"], ["g", "x"]]
term2_2 = ["Q", "y", "y"]

substitution_2 = unify(term1_2, term2_2)

if substitution_2 is not None:
    print("Unification is possible for the second pair.")
    print("Substitution:", substitution_2)
else:
    print("Unification is not possible for the second pair.")

OUTPUT:
Unification is not possible for the second pair.

#####QUESTION 3#####
term1_3 = ["prime", 11]
term2_3 = ["prime", "y"]

substitution_3 = unify(term1_3, term2_3)

if substitution_3 is not None:
    print("Unification is possible for prime(11) and prime(y).")
    print("Substitution:", substitution_3)
else:
    print("Unification is not possible for prime(11) and prime(y).")

OUTPUT:
Unification is possible for prime(11) and prime(y).
Substitution: {'y': 11}


######QUESTION 4####
term1_4 = ["p", ["f", "a"], ["g", "Y"]]
term2_4 = ["p", "X", "X"]

substitution_4 = unify(term1_4, term2_4)

if substitution_4 is not None:
    print("Unification is possible for p(f(a),g(Y)) and p(X,X).")
    print("Substitution:", substitution_4)
else:
    print("Unification is not possible for p(f(a),g(Y)) and p(X,X).")

OUTPUT:
Unification is not possible for p(f(a),g(Y)) and p(X,X).
