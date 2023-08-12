% Initial state: monkey is at place(middle, middle), has(nothing), box is at place(bottom, middle), banana is at place(top, middle)
state(at(monkey, middle, middle), has(nothing), at(box, bottom, middle), at(banana, top, middle)).

% Actions
% walk
action(walk(middle, middle, left)).
action(walk(middle, middle, right)).
action(walk(middle, left, left)).
action(walk(middle, right, right)).
action(walk(middle, middle, middle)).

% climb box
action(climb_box).
% push box
action(push_box).

% Define the legal moves in the state space
can(do(Action), State) :-
    state(State),
    action(Action),
    apply(Action, State).

% Apply the actions to change state
apply(walk(From, To, Dir), state(at(monkey, From, Y), H, B, C)) :-
    Y \= bottom,
    Dir = up,
    To = top,
    H = nothing,
    B = B,
    C = C.

apply(walk(From, To, Dir), state(at(monkey, From, Y), H, B, C)) :-
    Y \= top,
    Dir = down,
    To = bottom,
    H = nothing,
    B = B,
    C = C.

apply(walk(From, To, Dir), state(at(monkey, X, From), H, B, C)) :-
    X \= left,
    Dir = left,
    To = left,
    H = nothing,
    B = B,
    C = C.

apply(walk(From, To, Dir), state(at(monkey, X, From), H, B, C)) :-
    X \= right,
    Dir = right,
    To = right,
    H = nothing,
    B = B,
    C = C.

apply(climb_box, state(at(monkey, X, Y), H, at(box, X, Y), C)) :-
    H = nothing,
    C = C.

apply(push_box, state(at(monkey, X, Y), H, at(X, NewY, Y), C)) :-
    H = nothing,
    Y \= bottom,
    NewY \= bottom,
    C = C.

% Goal state
goal_state(state(at(monkey, _, top), has(banana), _, _)).

% Recursive plan
plan(State, []) :- goal_state(State).
plan(State1, [Action | PlanRest]) :-
    can(do(Action), State1),
    apply(Action, State1, State2),
    plan(State2, PlanRest).
