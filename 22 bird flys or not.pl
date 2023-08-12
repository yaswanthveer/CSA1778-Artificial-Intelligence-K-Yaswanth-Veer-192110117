% Facts
can_fly(sparrow).
can_fly(pigeon).
can_fly(eagle).
cannot_fly(penguin).
cannot_fly(ostrich).

% Rules
bird(X) :- can_fly(X).
bird(X) :- cannot_fly(X).
