--- Day 4: Ceres Search ---

--- Part one ---
You need to find the number of occurrences of the word 'XMAS' in the input file.
This word can appear in any direction: horizontal, vertical, and diagonal (both up and down).

The input file can be trated as a 2D character grid.
Taking this into account, you can iterate through each character in the grid and check if the word 'XMAS' appears in any direction, having a direction matrix like this:

```python   
directions = [
    (1, 0), # right
    (-1, 0), # left
    (0, 1), # down
    (0, -1), # up
    (1, -1), # diagonal down-left
    (1, 1), # diagonal down-right
    (-1, -1), # diagonal up-left
    (-1, 1), # diagonal up-right    
] 
```

Having this, you can iterate through each character and check for each direction a number of times equal to the length of the word 'XMAS'.

--- Part Two ---
Actually, you need to find the number of occurrences of the word 'MAS' that form an X shape.
The word can appear up and down, so the directions you need to check now are:

```python
directions = [
    (1, -1), # diagonal down-left
    (1, 1), # diagonal down-right
    (-1, -1), # diagonal up-left
    (-1, 1), # diagonal up-right 
]
```

Also, since it needs to form an X shape, actually you can just check the letter 'A' in the middle of the X, and then check if the word 'MAS' appears in the 4 directions.
