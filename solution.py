assignments = []
rows = 'ABCDEFGHI'
cols = '123456789'

def cross(a, b):
    "Cross product of elements in A and elements in B."
    return [s+t for s in a for t in b]
    
    
boxes = cross(rows, cols)

row_units = [cross(r, cols) for r in rows]
column_units = [cross(rows, c) for c in cols]
diagonal_units1 = list(map(lambda x:x[0]+x[1], zip(rows, cols)))
diagonal_units2 = list(map(lambda x:x[0]+x[1], zip(rows, reversed(cols))))
square_units = [cross(rs, cs) for rs in ('ABC','DEF','GHI') for cs in ('123','456','789')]
unitlist = row_units + column_units + square_units + [diagonal_units1] + [diagonal_units2]
#unitlist.append(diagonal_units1)
#unitlist.append(diagonal_units2)
units = dict((s, [u for u in unitlist if s in u]) for s in boxes)
peers = dict((s, set(sum(units[s],[]))-set([s])) for s in boxes)

def assign_value(values, box, value):
    """
    Please use this function to update your values dictionary!
    Assigns a value to a given box. If it updates the board record it.
    """

    # Don't waste memory appending actions that don't actually change any values
    if values[box] == value:
        return values

    values[box] = value
    if len(value) == 1:
        assignments.append(values.copy())
    return values
    
def naked_twins(values):
    print ("")
    display (values)
    for i in range(len(rows)):
        # Call naked twins constraint propagation - Currently this is set for the third column, but can be extended to all rows and columns
        single_col = dict(zip(row_units[i], lookup_labels(values, row_units[i])))
        single_col = (naked_twins_helper(single_col))
        #print ("Naked Twins:")
        #print (single_col)
        #print ("")
        # Update the grid with the results of naked twins
        for k,v in single_col.items():
            values[k] = v
    
    for j in range(len(cols)):
        # Call naked twins constraint propagation - Currently this is set for the third column, but can be extended to all rows and columns
        single_col = dict(zip(column_units[j], lookup_labels(values, column_units[j])))
        single_col = (naked_twins_helper(single_col))
        #print ("Naked Twins:")
        #print (single_col)
        #print ("")
        # Update the grid with the results of naked twins
        for k,v in single_col.items():
            values[k] = v
    
    for j in range(len(cols)):
        # Call naked twins constraint propagation - Currently this is set for the third column, but can be extended to all rows and columns
        single_col = dict(zip(square_units[j], lookup_labels(values, square_units[j])))
        single_col = (naked_twins_helper(single_col))
        #print ("Naked Twins:")
        #print (single_col)
        #print ("")
        # Update the grid with the results of naked twins
        for k,v in single_col.items():
            values[k] = v
    return values

def naked_twins_helper(single_unit_values):
    """Eliminate values using the naked twins strategy.
    Args:
        values(dict): a dictionary of the form {'box_name': '123456789', ...}

    Returns:
        the values dictionary with the naked twins eliminated from peers.
    """
    # Find all instances of naked twins
    # Eliminate the naked twins as possibilities for their peers
    print(single_unit_values)
    twins = set()
    keys = list(single_unit_values.keys())
	# Identify twins and eliminate the values in other boxes
    for j in range(len(keys)):
        if len(single_unit_values[keys[j]]) ==2:
            for i in range(j+1, len(keys)):
                if single_unit_values[keys[i]] == single_unit_values[keys[j]]:
                    twins.add(single_unit_values[keys[j]][0])
                    twins.add(single_unit_values[keys[j]][1])                    
    for key in single_unit_values:
        if len(single_unit_values[key]) > 2:
            single_unit_values[key] = ''.join([c for c in single_unit_values[key] if c not in twins])
    return single_unit_values


	
def lookup_labels(grid, label_list):
    """ 
    Return values for the label list sent
    """
    single_unit = []
    for label in label_list:
        single_unit.append(grid[label])
    return single_unit

    

def grid_values(grid):
    """
    Convert grid into a dict of {square: char} with '123456789' for empties.
    Args:
        grid(string) - A grid in string form.
    Returns:
        A grid in dictionary form
            Keys: The boxes, e.g., 'A1'
            Values: The value in each box, e.g., '8'. If the box has no value, then the value will be '123456789'.
    """
    values = []
    all_digits = '123456789'
    for c in grid:
        if c == '.':
            values.append(all_digits)
        elif c in all_digits:
            values.append(c)
    assert len(values) == 81
    return dict(zip(boxes, values))

def display(values):
    """
    Display the values as a 2-D grid.
    Input: The sudoku in dictionary form
    Output: None
    """
    width = 1+max(len(values[s]) for s in boxes)
    line = '+'.join(['-'*(width*3)]*3)
    for r in rows:
        print(''.join(values[r+c].center(width)+('|' if c in '36' else '')
                      for c in cols))
        if r in 'CF': print(line)
    return


def eliminate(values):
    """Eliminate values from peers of each box with a single value.

    Go through all the boxes, and whenever there is a box with a single value,
    eliminate this value from the set of values of all its peers.

    Args:
        values: Sudoku in dictionary form.
    Returns:
        Resulting Sudoku in dictionary form after eliminating values.
    """
    solved_values = [box for box in values.keys() if len(values[box]) == 1]
    for box in solved_values:
        digit = values[box]
        for peer in peers[box]:
            values[peer] = values[peer].replace(digit,'')
    return values


def only_choice(values):
    for unit in unitlist:
        for digit in '123456789':
            dplaces = [box for box in unit if digit in values[box]]
            if len(dplaces) == 1:
                values[dplaces[0]] = digit
    return values

def reduce_puzzle(values):
    """
    Iterate eliminate() and only_choice(). If at some point, there is a box with no available values, return False.
    If the sudoku is solved, return the sudoku.
    If after an iteration of both functions, the sudoku remains the same, return the sudoku.
    Input: A sudoku in dictionary form.
    Output: The resulting sudoku in dictionary form.
    """
    solved_values = [box for box in values.keys() if len(values[box]) == 1]
    stalled = False
    while not stalled:
        solved_values_before = len([box for box in values.keys() if len(values[box]) == 1])
        values = eliminate(values)
        values = only_choice(values)
        solved_values_after = len([box for box in values.keys() if len(values[box]) == 1])
        stalled = solved_values_before == solved_values_after
        if len([box for box in values.keys() if len(values[box]) == 0]):
            return False
    return values

def search(values):
    "Using depth-first search and propagation, try all possible values."
    # First, reduce the puzzle using the previous function
    values = reduce_puzzle(values)
    if values is False:
        return False ## Failed earlier
    if all(len(values[s]) == 1 for s in boxes): 
        return values ## Solved!
    # Choose one of the unfilled squares with the fewest possibilities
    n,s = min((len(values[s]), s) for s in boxes if len(values[s]) > 1)
    # Now use recurrence to solve each one of the resulting sudokus, and 
    for value in values[s]:
        new_sudoku = values.copy()
        new_sudoku[s] = value
        attempt = search(new_sudoku)
        if attempt:
            return attempt

def solve(grid):
    """
    Find the solution to a Sudoku grid.
    Args:
        grid(string): a string representing a sudoku grid.
            Example: '2.............62....1....7...6..8...3...9...7...6..4...4....8....52.............3'
    Returns:
        The dictionary representation of the final sudoku grid. False if no solution exists.
    """
    sudoku_grid = grid_values(grid)
    value_grid = search(reduce_puzzle(only_choice(eliminate(sudoku_grid))))
    #value_grid = naked_twins(value_grid)
    #print (value_grid)
    return value_grid
    
    

if __name__ == '__main__':
    #display(naked_twins(reduce_puzzle(only_choice(eliminate(nt_values)))))
    #display(naked_twins(reduce_puzzle(only_choice(eliminate(sudoku_grid)))))
    diag_sudoku_grid = '9.1....8.8.5.7..4.2.4....6...7......5..............83.3..6......9................'
	# Solve and print the solution
    final_grid = solve(diag_sudoku_grid)
    if final_grid is False:
        print ("No solution")
    else:
        display(final_grid)

    try:
        from visualize import visualize_assignments
        visualize_assignments(assignments)

    except SystemExit:
        pass
    except:
        print('We could not visualize your board due to a pygame issue. Not a problem! It is not a requirement.')
