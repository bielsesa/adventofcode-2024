--- Day 6: Guard Gallivant ---

--- Part one ---
Your input is a map of the area where the guard is gallivanting.
The guard is represented by a '^', '>', 'v', or '<' character, depending on the direction she's facing.
The background is a '.' character.
The obstacles are '#' characters.

The guard will always try to move a step forward in the direction she's facing.
If she can't move forward, she will turn right 90 degrees, until she can move forward.

Once the guard arrives to one of the edges of the map, the program ends.

You need to find the number of steps the guard has taken to reach the edge of the map (all the positions she has visited).

--- Part Two ---

You need to calculate the number of possible positions you can add one new obstacle to the map, so that the guard is stuck in a loop.
