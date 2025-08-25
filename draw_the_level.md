
# Draw the level

Start with your current implementation or the reference solution for day 1.
Make sure the code is running.

Implement the following:

### 1. Walls

Copy the following map into the initialized level.
Hashes `#` are walls, dots `.` are dots. 

    #################
    #...............#
    #.###.#####.###.#
    #.#...#...#...#.#
    #...#...#...#...#
    #.#...#####...#.#
    #...#...#...#...#
    #.#...#...#...#.#
    #.###.#####.###.#
    #...............#
    #################

### 2. Nested Loop

In the `draw()` function, loop over all the rows of the level and over every element of each row.
Use the builtin `enumerate()` function to create counter variables for botht the x and y direction.

Inside the loop, print the current element and its x/y position.

### 3. Drawing

Depending on the symbol at the current position, use `draw_tile()` to draw either a wall or a dot.
Also cover the empty space for dots that have been eaten.

You should see the complete level.

### 4. Stop at walls

Modify the `Character.move()` method to take walls into account:

Check whether the new position is a wall. If it is:

- do not move the character
- set its direction to a `Vector(x=0, y=0)`

Now the pac should move around the maze.
