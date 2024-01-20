from TextToMatrix import *
from BreadthFirstSearch import *
from DepthFirstSearch import *
from GreedySearch import *
from AStar import *


import sys
import time

import csv


RESTRICTEDPUZZLESAMOUNT = 2000

def openCSV(file):
    list = []
    header = True
    with open(file, 'r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            if header == False:
                list.append(row[0])
            #Gets rid of the header
            header = False
            if len(list) == RESTRICTEDPUZZLESAMOUNT:
                return list
    return list


def main():
    SIZE = 9
    file = sys.argv[1]
    single = False
    if len(sys.argv) == 3:
        if sys.argv[2].lower() == 'single':
            single = True
    
    contents = openCSV(file)
    
    if not single:
        print("Number of puzzles to run current test on: ", RESTRICTEDPUZZLESAMOUNT)

        #A*
        print()
        print("Running A*:", flush=True) 
        start_time = time.time()
        for puzzle in range(len(contents)):
            initialPuzzle = ConvertTextToMatrix(contents[puzzle],SIZE)

            testPuzzle = initialPuzzle.copy()
            
            AStarPuzzle = AStar(testPuzzle)


        end_time = time.time()
        print("--- %s seconds ---" % (end_time - start_time), flush=True)

        # BFS
        print()
        print("Running BFS:", flush=True)
        start_time = time.time()
        for puzzle in range(len(contents)):
            initialPuzzle = ConvertTextToMatrix(contents[puzzle],SIZE)

            testPuzzle = initialPuzzle.copy()
            BFSPuzzle = BreadthFirstSearch(testPuzzle)

        end_time = time.time()
        print("--- %s seconds ---" % (end_time - start_time), flush=True)
        
        ## DFS
        print()
        print("Running DFS:", flush=True)  
        start_time = time.time()
        for puzzle in range(len(contents)):
            initialPuzzle = ConvertTextToMatrix(contents[puzzle],SIZE)

            testPuzzle = initialPuzzle.copy()
            
            DFSPuzzle = DepthFirstSearch(testPuzzle)

        end_time = time.time()
        print("--- %s seconds ---" % (end_time - start_time), flush=True)

        print()#Spacer
        print("Running Greedy Rows:", flush=True) 
        ## Greedy Rows
        start_time = time.time()
        for puzzle in range(len(contents)):
            initialPuzzle = ConvertTextToMatrix(contents[puzzle],SIZE)

            testPuzzle = initialPuzzle.copy()
            
            GreedyPuzzle = GreedySearch(testPuzzle, 'rows')

        end_time = time.time()
        print("--- %s seconds ---" % (end_time - start_time), flush=True)
            


        ## Greedy Columns
        print()
        print("Running Greedy Columns:", flush=True) 
        start_time = time.time()
        for puzzle in range(len(contents)):
            initialPuzzle = ConvertTextToMatrix(contents[puzzle],SIZE)

            testPuzzle = initialPuzzle.copy()
            
            GreedyPuzzle = GreedySearch(testPuzzle, 'columns')

        end_time = time.time()
        print("--- %s seconds ---" % (end_time - start_time), flush=True)



        ## Greedy Cells
        print()
        print("Running Greedy Cells:", flush=True) 
        start_time = time.time()
        for puzzle in range(len(contents)):
            initialPuzzle = ConvertTextToMatrix(contents[puzzle],SIZE)

            testPuzzle = initialPuzzle.copy()
            
            GreedyPuzzle = GreedySearch(testPuzzle, 'columns')

        end_time = time.time()
        print("--- %s seconds ---" % (end_time - start_time), flush=True)

    ## SINGLE GREEDY TESTS
    else:       
        
        initialPuzzle = ConvertSingleFileToMatrix(file)

        # Rows
        initialPuzzle = ConvertSingleFileToMatrix(file)
        print("Initial Puzzle:")
        print(initialPuzzle)
        print("")
        print("")
        print("")

        testPuzzle = initialPuzzle.copy()
            
        start_time = time.time()
        GreedyPuzzle = GreedySearch(testPuzzle, 'rows')
        end_time = time.time()

        print("")
        print("")
        print("")
        print("Greedy Rows Puzzle:")
        print(GreedyPuzzle)

        print("--- %s seconds ---" % (end_time - start_time))

        # Columns
        testPuzzle = initialPuzzle.copy()
            
        start_time = time.time()
        GreedyPuzzle = GreedySearch(testPuzzle, 'columns')
        end_time = time.time()

        print("")
        print("")
        print("")
        print("Greedy Columns Puzzle:")
        print(GreedyPuzzle)

        print("--- %s seconds ---" % (end_time - start_time))

        # Cells
        testPuzzle = initialPuzzle.copy()
            
        start_time = time.time()
        GreedyPuzzle = GreedySearch(testPuzzle, 'cells')
        end_time = time.time()

        print("")
        print("")
        print("")
        print("Greedy Cells Puzzle:")
        print(GreedyPuzzle)

        print("--- %s seconds ---" % (end_time - start_time))    

main()