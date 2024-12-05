--- Day 1: Historian Hysteria ---

--- Part one ---
To calculate the total distance (R) you need to pair each element of the two lists (L1 and L2) taking the lowest number each time. 
For each pair, calculate the "local distance" (Di, where i is the number of pair).
Finally, sum up all the local distances: R = ∑Di

--- Part two ---

Similarity score between two lists of numbers: For each number in the left list, check how many times it appears in the right list.
Then, multiply the number by the number of times it appears in the right list.

Finally, sum all the values.
