% Rules
hypothesis(has_flu) :- symptom(fever), symptom(cough).
hypothesis(has_allergy) :- symptom(sneezing), symptom(runny_nose).

% Facts
symptom(fever).
symptom(cough).
symptom(sneezing).
symptom(runny_nose).

% Backward chaining procedure
diagnose(Condition) :-
    hypothesis(Condition),
    writeln('Patient may have: '),
    writeln(Condition),
    !.
diagnose(_).
