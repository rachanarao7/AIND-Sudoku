# Artificial Intelligence Nanodegree
## Introductory Project: Diagonal Sudoku Solver

# Question 1 (Naked Twins)
Q: How do we use constraint propagation to solve the naked twins problem?  
A: *Student should provide answer here*

Constraint propagation is applied as follows to the Naked twins problem:

- Identify the boxes with twins, two unsolved boxes with the same possibilities

- Identifying the naked twin pairs, allows us to eliminate those values from other boxes in the same unit. This can lead either to finding a solution for the boxes 
or simplifying the problem including creations of new naked twins.

- Along with this elimination, only choice, search and other constraint propagation strategies can be used to solve the puzzle.


# Question 2 (Diagonal Sudoku)
Q: How do we use constraint propagation to solve the diagonal sudoku problem?  
A: *Student should provide answer here*

For a diagonal sudoku problem:
- For solving of a regular sudoku problem we identify peers: the same row boxes, same column boxes and same square boxes for the box that we are solving. 
With this knowledge we try to solve the puzzle using different constraint propagation techniques like eliminate and only choice. 

- For a diagonal sudoku, the peers set for a box will also include boxes on the two diagonals, top left to bottom right and top right to bottom left. The constraint propagation strategies like eliminate, only choice can be further applied to solve the puzzle.




### Install

This project requires **Python 3**.

We recommend students install [Anaconda](https://www.continuum.io/downloads), a pre-packaged Python distribution that contains all of the necessary libraries and software for this project. 
Please try using the environment we provided in the Anaconda lesson of the Nanodegree.

##### Optional: Pygame

Optionally, you can also install pygame if you want to see your visualization. If you've followed our instructions for setting up our conda environment, you should be all set.

If not, please see how to download pygame [here](http://www.pygame.org/download.shtml).

### Code

* `solution.py` - You'll fill this in as part of your solution.
* `solution_test.py` - Do not modify this. You can test your solution by running `python solution_test.py`.
* `PySudoku.py` - Do not modify this. This is code for visualizing your solution.
* `visualize.py` - Do not modify this. This is code for visualizing your solution.

### Visualizing

To visualize your solution, please only assign values to the values_dict using the `assign_value` function provided in solution.py

### Submission
Before submitting your solution to a reviewer, you are required to submit your project to Udacity's Project Assistant, which will provide some initial feedback.  

The setup is simple.  If you have not installed the client tool already, then you may do so with the command `pip install udacity-pa`.  

To submit your code to the project assistant, run `udacity submit` from within the top-level directory of this project.  You will be prompted for a username and password.  If you login using google or facebook, visit [this link](https://project-assistant.udacity.com/auth_tokens/jwt_login) for alternate login instructions.

This process will create a zipfile in your top-level directory named sudoku-<id>.zip.  This is the file that you should submit to the Udacity reviews system.

