% Career Advisor Expert System

career(engineer) :-
    likes(math),
    likes(computers).

career(doctor) :-
    likes(biology),
    likes(helping_people).

career(teacher) :-
    likes(teaching),
    likes(communication).

career(lawyer) :-
    likes(argument),
    likes(public_speaking).

career(artist) :-
    likes(drawing),
    likes(creativity).

career(programmer) :-
    likes(computers),
    likes(problem_solving).

% User Interests
likes(biology).
likes(helping_people).

% Display Suggested Career
suggest_career :-
    career(Career),
    write('Suggested Career: '),
    write(Career), nl.