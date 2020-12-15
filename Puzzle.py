'''
Created on Dec 3, 2020

@author: home/1911_Preshly_Fernandes
'''
import copy
import random
from Solver import find_empty

class Generate_Puzzle():
    '''
    classdocs
    generate full puzzle solution using the levels passed as input
    send copy_pzzle by hiding places to my.py
    uses find_empty from Solver.py to find the empty spaces in the puzzle
    '''


    def __init__(self, level):
        '''
        Constructor
        '''
        if level == 'easy':
            self.numOfPlacesToHide = 4
        elif level == 'medium':
            self.numOfPlacesToHide = 6
        elif level == 'hard':
            self.numOfPlacesToHide = 8

        self. grid = [ [0 for i in range(9)] for j in range(9) ]
        
        self.generate_solution(self.grid)
        
        #while(self.find_empty_square(self.grid)):
        while(find_empty(self.grid)):
            self.grid = [ [0 for i in range(9)] for j in range(9) ]
            self.generate_solution(self.grid) 
        
        self.copy_puzzle = copy.deepcopy(self.grid)
        self.copy_puzzle = self.hide_puzzle(self.copy_puzzle)
    
    def possible(self, grid, row, col, num):
        if num in grid[row]:
            return False
        
        for i in range(9):
            if num == grid[i][col]:
                return False
           
        sub_row = (row // 3) * 3
        sub_col = (col // 3) * 3
        
        for i in range(0,3):
            for j in range(0,3):
                if grid[sub_row + i][sub_col + j] == num:
                    return False
        
        return True
    '''
    def find_empty_square(self, grid):
        for i in range(9):
            for j in range(9):
                if grid[i][j] == 0:
                    return (i,j)
        return
    '''
   
    def generate_solution(self, grid):
        number_list = [1,2,3,4,5,6,7,8,9]
        for y in range(9):
            for x in range(9):
                if grid[y][x] == 0:
                    random.shuffle(number_list)
                    for number in number_list:
                        if self.possible(grid, y, x, number):
                            grid[y][x] = number                                                  
                            
                            #if not self.find_empty_square(grid):
                            if not find_empty(grid):
                                return True
                            else:
                                if self.generate_solution(grid): #if grid is full
                                    return True
                            
                    #break
                    return

    def hide_puzzle(self, puzzle):
        
        col_index = [0,1,2,3,4,5,6,7,8]
                
        for row in range(9):
            #number of places to hide
            if row % 2 == 0:
                num = self.numOfPlacesToHide
            else:
                num = self.numOfPlacesToHide + 2
            
            #hide places iterating over each row
            for i in range(num):
                random.shuffle(col_index)
                hide = random.choice(col_index) #choose a random place from the list
                puzzle[row][hide] = 0 #hide
        return puzzle    
        
        
