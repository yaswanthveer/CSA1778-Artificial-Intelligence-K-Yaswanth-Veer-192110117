%  solve Towers of Hanoi problem
hanoi(1, Source, _, Destination, [Move]) :-
    Move = move(1, Source, Destination).

hanoi(N, Source, Aux, Destination, Moves) :-
    N > 1,
    N1 is N - 1,
    hanoi(N1, Source, Destination, Aux, Moves1),
    append(Moves1, [move(N, Source, Destination)], Moves2),
    hanoi(N1, Aux, Source, Destination, Moves3),
    append(Moves2, Moves3, Moves).
