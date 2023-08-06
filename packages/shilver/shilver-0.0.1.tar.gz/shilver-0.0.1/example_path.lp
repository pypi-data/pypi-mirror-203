gridsize(6).

_edge(vtx(5,6),vtx(6,6)).
_edge(vtx(5,6),vtx(4,6)).
_edge(vtx(6,6),vtx(5,6)).
_edge(vtx(4,6),vtx(5,6)).
_edge(vtx(6,3),vtx(5,3)).
_edge(vtx(6,3),vtx(6,2)).
_edge(vtx(5,5),vtx(6,5)).
_edge(vtx(5,5),vtx(5,4)).
_edge(vtx(3,5),vtx(4,5)).
_edge(vtx(3,5),vtx(3,4)).
_edge(vtx(1,5),vtx(2,5)).
_edge(vtx(1,5),vtx(1,4)).
_edge(vtx(4,3),vtx(4,4)).
_edge(vtx(4,3),vtx(4,2)).
_edge(vtx(2,3),vtx(2,4)).
_edge(vtx(2,3),vtx(2,2)).
_edge(vtx(5,3),vtx(6,3)).
_edge(vtx(6,2),vtx(6,3)).
_edge(vtx(6,5),vtx(5,5)).
_edge(vtx(5,4),vtx(5,5)).
_edge(vtx(4,5),vtx(3,5)).
_edge(vtx(3,4),vtx(3,5)).
_edge(vtx(2,5),vtx(1,5)).
_edge(vtx(1,4),vtx(1,5)).
_edge(vtx(4,4),vtx(4,3)).
_edge(vtx(4,2),vtx(4,3)).
_edge(vtx(2,4),vtx(2,3)).
_edge(vtx(2,2),vtx(2,3)).
_edge(vtx(1,4),vtx(2,4)).
_edge(vtx(3,6),vtx(4,6)).
_edge(vtx(2,2),vtx(1,2)).
_edge(vtx(2,4),vtx(1,4)).
_edge(vtx(4,6),vtx(3,6)).
_edge(vtx(3,6),vtx(2,6)).
_edge(vtx(6,2),vtx(5,2)).
_edge(vtx(4,4),vtx(4,5)).
_edge(vtx(3,3),vtx(3,4)).
_edge(vtx(2,5),vtx(2,6)).
_edge(vtx(6,5),vtx(6,6)).
_edge(vtx(5,3),vtx(5,4)).
_edge(vtx(4,2),vtx(4,1)).
_edge(vtx(3,3),vtx(3,2)).
_edge(vtx(6,6),vtx(6,5)).
_edge(vtx(3,4),vtx(3,3)).
_edge(vtx(5,4),vtx(5,3)).
_edge(vtx(4,5),vtx(4,4)).
_edge(vtx(1,2),vtx(2,2)).
_edge(vtx(2,6),vtx(3,6)).
_edge(vtx(5,2),vtx(6,2)).
_edge(vtx(2,6),vtx(2,5)).
_edge(vtx(4,1),vtx(4,2)).
_edge(vtx(3,2),vtx(3,3)).
_edge(vtx(4,1),vtx(5,1)).
_edge(vtx(2,1),vtx(3,1)).
_edge(vtx(2,1),vtx(1,1)).
_edge(vtx(1,2),vtx(1,1)).
_edge(vtx(5,2),vtx(5,1)).
_edge(vtx(3,2),vtx(3,1)).
_edge(vtx(5,1),vtx(4,1)).
_edge(vtx(3,1),vtx(2,1)).
_edge(vtx(1,1),vtx(2,1)).
_edge(vtx(1,1),vtx(1,2)).
_edge(vtx(5,1),vtx(5,2)).
_edge(vtx(3,1),vtx(3,2)).

_included(X;Y) :- _edge(X,Y).

number(1..D*2) :- gridsize(D).

1 {
    white(V, N): gridsize(D), number(N), N>=1, N<=D; 
    black(V, N): gridsize(D), number(N), N>=1, N<=D*2
} 1 :- _included(V).
