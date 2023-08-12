% Facts: Symptoms and conditions
symptom(fever).
symptom(cough).
symptom(headache).
symptom(rash).

condition(cold, [fever, cough]).
condition(flu, [fever, cough, headache]).
condition(allergy, [cough, rash]).
condition(measles, [fever, rash]).

% Rules for diagnosis
diagnose_patient(Symptoms, Diagnosis) :-
    findall(Condition, (condition(Condition, ConditionSymptoms), subset(ConditionSymptoms, Symptoms)), PossibleConditions),
    ( PossibleConditions = [] ->
        Diagnosis = 'Unknown';
        Diagnosis = PossibleConditions
    ).
