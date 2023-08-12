% Facts
student(john).
student(lisa).
student(alex).

teacher(prof_smith).
teacher(prof_jones).
teacher(prof_doe).

subject(math).
subject(physics).
subject(chemistry).

course_code(math, m101).
course_code(physics, p201).
course_code(chemistry, c301).

% Rules
teaches(prof_smith, math).
teaches(prof_jones, physics).
teaches(prof_doe, chemistry).

enrolled_in(john, math).
enrolled_in(john, physics).
enrolled_in(lisa, physics).
enrolled_in(alex, chemistry).

% Query examples
% Get the list of students enrolled in a subject
% ?- enrolled_in(Student, physics).

% Get the course code for a subject
% ?- course_code(Subject, Code).

% Get the teacher who teaches a subject
% ?- teaches(Teacher, math).
