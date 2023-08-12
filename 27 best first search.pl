% Sample graph representation
edge(a, b, 4).
edge(a, c, 3).
edge(b, d, 5).
edge(b, e, 2).
edge(c, f, 6).
edge(c, g, 7).

% Best First Search algorithm
best_first_search(Start, Goal, Path) :-
    best_first_search_recursive([node(Start, [])], Goal, Path).

best_first_search_recursive([node(Goal, Path) | _], Goal, Path).

best_first_search_recursive([node(Current, CurrentPath) | Rest], Goal, Path) :-
    findall(node(Next, [Next | CurrentPath]), edge(Current, Next, _), NextNodes),
    append(Rest, NextNodes, NewQueue),
    sort_queue(NewQueue, SortedQueue),
    best_first_search_recursive(SortedQueue, Goal, Path).

sort_queue(Queue, SortedQueue) :-
    predsort(compare_priority, Queue, SortedQueue).

compare_priority(Order, node(_, Path1), node(_, Path2)) :-
    length(Path1, Length1),
    length(Path2, Length2),
    compare(Order, Length1, Length2).
