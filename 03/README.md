--- Day 3: Mull It Over ---

--- Part one ---
A multiplication operation is represented by the following expression:

    - mul(X,Y)

If a multiplication expression is found but it does not follow the above format, it should be ignored.

Find all the valid multiplication expressions in the input and sum their results.

--- Part Two ---
The input also has these expressions scattered: do() and don't().

If a mul(X,Y) expression has a do() condition somewhere before it, it should be captured.
Otherwise, if there is a don't() condition, it shouldn't be captured.
