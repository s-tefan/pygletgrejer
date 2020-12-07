-module(matrix).
-export([
    from_list_of_lists/1,
    eye/1,
    transpose/1,
    transpose_ll/1
]).

from_list_of_lists(LL) ->
    {matrix, length(LL), length(hd(LL)), LL}.

eye(N) ->
    {matrix, N, N, unity}.

transpose(Matrix) ->
    {matrix, M, N, LL} = Matrix,
    case LL of
        unity ->
            {matrix, N, M, LL};
        [FirstRow|Rem] ->
            {matrix, N, M, transpose_ll([FirstRow|Rem])}
    end.

add_first_col_ll([A], [[]]) ->
    [[A]];
add_first_col_ll([H|R], [[]]) ->
    [[H]|add_first_col_ll(R,[[]])];
add_first_col_ll([H|[]], [RH|[]]) ->
    [[H | RH]];
add_first_col_ll([H|T], [RH|RT]) ->
    [[H | RH] | add_first_col_ll(T,RT)].

transpose_ll([Row]) ->
    add_first_col_ll(Row,[[]]);
transpose_ll([FirstRow|Rest]) ->
    add_first_col_ll(FirstRow,transpose_ll(Rest)).
