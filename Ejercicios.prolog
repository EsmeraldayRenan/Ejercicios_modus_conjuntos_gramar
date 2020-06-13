
%MARTINEZ RONQUILLO ESMERALDA
%HERNANDEZ LUNA JUAN RENAN

%******************************* EJERCICIO 1*****************************

% Desarrolle un predicado que permita validar un NIP de una banco que 
% Responde a la siguiente gramatica
% Nip ::= <Digito> ' ' <Digito> ' ' <Digito> ' ' <Digito>
% Digito ::= 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9

% nip("1235").
% true.
% nip("123").
% false.


latom_lstring([], []).
latom_lstring([F|C],R) :- latom_lstring(C,S), atom_string(F,SF), append([SF],S,R).
preparar_string(Term, LS) :-
		atom(Term),
		atom_string(Term,Str),
		preparar_string(Str,LS).

preparar_string(Str,LS) :-
		string(Str),
		string_chars(Str,LAC),
		latom_lstring(LAC, LS).

digito(D) :-
		D == "0"; D == "1"; D == "2"; D == "3"; D == "4";
 		D == "5"; D == "6"; D == "7"; D == "8"; D == "9".
 		
nip([F|[]]) :- digito(F).
nip([F|C]) :- digito(F), nip(C).

nip(J) :- string_length(J,R), R == 4 , preparar_string(J,B), nip(B).



%******************************* EJERCICIO 2*****************************


% Desarrolle un predicado que permita validar un octeto de una ip
% Responde a la siguiente gramatica
% Octeto ::= '2'<R5><R5> | '1'<Digito><Digito> | <Digito><Digito> | <Digito>
% R5 ::= 0 | 1 | 2 | 3 | 4 | 5
% Digito ::= 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9

% nips("255").
% true.
% nips("256").
% false

r5(D) :-
		D == "0"; D == "1"; D == "2";
		D == "3"; D == "4"; D == "5".

oc1([Q|[]]) :- digito(Q).
oc1([Q|E]) :- digito(Q), oc1(E).
oc2([H|[]]) :- r5(H).
oc2([H|E]) :- r5(H), oc2(E).
oc3([H|E]) :- H == "2", oc2([H|E]); H == "1", oc1([H|E]).


nips(G) :- 
		string_length(G,R), R == 3 , preparar_string(G,Q), oc3(Q);
		string_length(G,R), R == 2 , preparar_string(G,Q), oc1(Q);
		string_length(G,R), R == 1 , preparar_string(G,Q), oc1(Q).








