from HelperFunctions import *
from DepthFirstSearch import *

def calculate_heuristic(cell_options, puzzle, cell_index):
    # Convert cell_index to tuple
    cell_index_tuple = tuple(cell_index)

    # Convert cell_options values to tuples
    cell_options = {key: tuple(value) for key, value in cell_options.items()}

    # Calculate the heuristic value for a given cell based on the provided formula
    options_per_box = len(cell_options[cell_index_tuple])
    
    # Options for entire row and cell
    row_options = set().union(*(cell_options.get((i, cell_index_tuple[1]), ()) for i in range(9)))
    col_options = set().union(*(cell_options.get((cell_index_tuple[0], j), ()) for j in range(9)))
    options_per_row = len(row_options)
    options_per_col = len(col_options)
    
    total_options = options_per_box + options_per_row + options_per_col

    if total_options == 0:
        return float('inf')  # Return infinity for cells with no options
    
    return 1 / total_options


def options(puzzle):
    dict = {}   
    heuristicPuzzle = puzzle.copy()
    unvisitedValues = []
    emptyCellIndex = getEmptyCell(heuristicPuzzle)
    while emptyCellIndex[0] != -1:
        allPossibleValues = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        #Check row
        for row in range(0,9):
            if puzzle[emptyCellIndex[0]][row] in allPossibleValues:
                allPossibleValues.remove(puzzle[emptyCellIndex[0]][row])
        #Check column
        for column in range(0,9):
            if puzzle[column][emptyCellIndex[1]] in allPossibleValues:
                allPossibleValues.remove(puzzle[column][emptyCellIndex[1]])
        #Check sqaure
        square = squareChoice(emptyCellIndex[0],emptyCellIndex[1])
        squareListValues = squareValues(square, puzzle)
        for index in range(len(squareListValues)):
            if squareListValues[index] in allPossibleValues:
                allPossibleValues.remove(squareListValues[index])

        
        dict[tuple([emptyCellIndex[0],emptyCellIndex[1]])] = allPossibleValues
        
        unvisitedValues.append(allPossibleValues)
        
        heuristicPuzzle[emptyCellIndex[0]][emptyCellIndex[1]] = -1

        emptyCellIndex = getEmptyCell(heuristicPuzzle)

    return dict

def getEmptyCellByNumConstraints(options):
    smallestLen = 9
    index = [-1,-1]
    for cell in options:
        if len(options[cell]) < smallestLen:
            smallestLen = len(options[cell])
            index = cell
    return [index[0], index[1]]

def AStar(puzzle):
    # initialise the set w/ the heuristics
    open_set = [(calculate_heuristic(options(puzzle), puzzle, getEmptyCellByNumConstraints(options(puzzle))), puzzle)]
    closed_set = set()

    while open_set:
        open_set.sort()  # Sort by heuristic value
        current_puzzle = open_set.pop(0)[1]

        if ValidSolution(current_puzzle):
            return current_puzzle

        #check visited
        closed_set.add(tuple(map(tuple, current_puzzle)))

        emptyCellOptions = options(current_puzzle)
        emptyCellIndex = getEmptyCellByNumConstraints(emptyCellOptions)

        for value in emptyCellOptions[tuple(emptyCellIndex)]:
            #new puzzle with the new value assigned
            new_puzzle = [row[:] for row in current_puzzle]
            new_puzzle[emptyCellIndex[0]][emptyCellIndex[1]] = value

            #check if we didnt explored begore
            if tuple(map(tuple, new_puzzle)) not in closed_set:
                heuristic_value = calculate_heuristic(emptyCellOptions, new_puzzle, tuple(emptyCellIndex))
                open_set.append((heuristic_value, new_puzzle))

    return None  # Puzzle not solvable
