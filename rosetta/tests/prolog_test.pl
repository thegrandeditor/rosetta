parent(john, mary).
parent(mary, ann).
ancestor(X, Y) :- parent(X, Y).
ancestor(X, Z) :- parent(X, Y), ancestor(Y, Z).

?- ancestor(john, ann).
