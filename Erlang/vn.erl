-module(vn).
-export([
    succ/1,
    pred/1, 
    int_from_vn/1, 
    vn_from_int/1, 
    is_vn/1, 
    plus/2,
    times/2,
    gte/2,
    list_print/1]).



succ([]) -> [[]];
succ(A) -> [A|A].

pred([A|A]) -> A;
pred(A) -> A. % Limit ordinals


int_from_vn([]) -> 0;
int_from_vn([A|A]) -> 1 + int_from_vn(A).

vn_from_int(0) -> [];
vn_from_int(N) when is_integer(N), N > 0 -> 
    succ(vn_from_int(N-1)).



is_vn([]) -> true;
is_vn([A|A]) -> true;
is_vn(_) -> false.

plus([], A) -> A;
plus(A, []) -> A;
plus(A, [B|B]) -> succ(plus(A,B));
plus([[]],omega) -> omega;
plus(omega,omega) -> {plus, omega, omega}.

times([],_) -> [];
times(_,[]) -> [];
times([A|A],B) -> plus(times(A,B), B).

gte(_,{}) -> true;
gte([A|A],[B|B]) -> gte(A,A).



list_print([A|[B|C]]) ->
    io:format("~w, ", [A]),
    list_print([B|C]);
list_print([A|[]]) ->
    io:format("~w~n", [A]);
list_print([]) ->
    io:format("~n", []).

