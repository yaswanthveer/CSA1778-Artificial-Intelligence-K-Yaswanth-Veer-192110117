% Facts
dob(veer, date(2003, 7, 11)).
dob(hemu, date(2002, 4, 31)).
dob(manohar, date(2000, 9, 22)).

% Rules
age(Name, Age) :-
    dob(Name, date(Year, Month, Day)),
    current_date(date(CurrentYear, CurrentMonth, CurrentDay)),
    Age is CurrentYear - Year - ( (CurrentMonth, CurrentDay) < (Month, Day) ).

current_date(date(2023, 8, 11)).
