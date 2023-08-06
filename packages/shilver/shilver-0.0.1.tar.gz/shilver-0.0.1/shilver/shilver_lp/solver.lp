% White and black vertexes must be included
included(V) :- white(V,N).
included(V) :- black(V,N).

% Generate edges between adyacent edges
2 { edge(vtx(X,Y), vtx(X2,Y)): X2=X+1, X2<=D, gridsize(D); 
    edge(vtx(X,Y), vtx(X2,Y)): X2=X-1, X2>=1; 
    edge(vtx(X,Y), vtx(X,Y2)): Y2=Y+1, Y2<=D, gridsize(D); 
    edge(vtx(X,Y), vtx(X,Y2)): Y2=Y-1, Y2>=1 } 2 :- included(vtx(X,Y)).

% edge/2 is undirected
edge(V2,V1) :- edge(V1,V2).
% 
included(A;B) :- edge(A,B).

% Line cross Vtx straightly
straight(Vtx) :- 
    edge(Vtx, vtx(X1, Y)),
    edge(Vtx, vtx(X2, Y)),
    X1!=X2.
straight(Vtx) :- 
    edge(Vtx, vtx(X, Y1)),
    edge(Vtx, vtx(X, Y2)),
    Y1!=Y2.

% Line makes an elbow on Vtx
elbow(Vtx) :- 
    edge(Vtx, vtx(X1, Y1)),
    edge(Vtx, vtx(X2, Y2)),
    Y1!=Y2, X1!=X2.

% A Vtx is part of the arm of another if is connected with it by a straight line
straightly_connected(Vtx, StrConnected) :-
    edge(Vtx, StrConnected).
straightly_connected(Vtx, StrConnected) :-
    straightly_connected(Vtx, MiddleVtx),
    straight(MiddleVtx),
    edge(MiddleVtx, StrConnected),
    Vtx!=StrConnected.

% %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

% Connected
connected(V) :- V=#min{Vtx:white(Vtx,N); Vtx:black(Vtx,N)}.
connected(V2) :- connected(V1), edge(V1, V2).

% % Any selected edge must be connected with the rest
:- included(Vtx1), not connected(Vtx1).

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

% Any white/black Vtx should be included and
%  - white must be straight
%  - black must be elbows
:- white(Vtx,N), elbow(Vtx).
:- black(Vtx,N), straight(Vtx).

% White points
:- white(Vtx,N), N!=#count{StrConnected:straightly_connected(Vtx, StrConnected)}.

% Black points
:- black(Vtx,N), N!=#count{StrConnected:straightly_connected(Vtx, StrConnected)}.
