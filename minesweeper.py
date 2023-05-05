#2D list declared to represent the minesweeper field.
minefield = [['-', '-', '-', '#', '#'],
         ['-', '#', '-', '-', '-'],
         ['-', '-', '#', '-', '-'],
         ['-', '#', '#', '-', '-'],
         ['-', '-', '-', '-', '-']]

#Function declared to return the expected minesweeper field output. Takes the parameter of grid which will work with a 2D list.
#NB - In this task, I will take the original list (minefield) and update it so that it will provide the output values. It doesn't appear to be necessary for this task, but if the 
#original input needed to be kept for whatever reason, this could be done using grid.copy() in the function to provide an unchanged version of the input list. 
def minesweeper_generator(grid):
 

    #Empty list declared to store the position of the mines
    mine_position = []

    #Two for loops using enumerate. The outer loop works through each 'row' in field, i.e. each of the sublists in field. The second loop works through the individual values in the specified row.
    #row_count holds the index of the sublist and row holds the actual values contained in each sublist.
    for row_count, row in enumerate(grid, start = 0):
        #This inner loop is working through each of the values in the rows from field. The contents of each individual entry in the row is saved in position_value and the index is saved in position_count
        for position_count, position_value in enumerate(row, start = 0):
            
            #Conditional block checks to see if there is a mine or not.
            if position_value == '#':
                #If a mine is found, the index of the row and index of the mine within that row are added to mine_position
                mine_position.append([row_count, position_count])
            else:
                #If there is no mine, then the value within field needs updating to an integar (0) so that math can be performed on it to indicate how many mines are nearby.
                grid[row_count][position_count] = 0
                
                
    #This outer loop cycles through all the co-ordinates of the mines in mine_position
    for mine in mine_position:
        
        #List declared as positions_to_change, which will take in co-ordinates of the mine-neighbouring cells which need to be changed.
        positions_to_change = []
        #The mine[0] values reflect the row and mine[1] the specific position within the row. These 9 append calls all use maths equations to access each position that neighbours a mine. 
        #These are based on the table in the task outline. The co-ordinates are appended in a list so that each position entry is kept together.
        positions_to_change.append([mine[0] - 1, mine[1] - 1])
        positions_to_change.append([mine[0] - 1, mine[1]])
        positions_to_change.append([mine[0] - 1, mine[1] + 1])
        positions_to_change.append([mine[0], mine[1] - 1])
        positions_to_change.append([mine[0], mine[1]])
        positions_to_change.append([mine[0], mine[1] + 1])
        positions_to_change.append([mine[0] + 1, mine[1] - 1])
        positions_to_change.append([mine[0] + 1, mine[1]])
        positions_to_change.append([mine[0] + 1, mine[1] + 1])
    


        #Once all of the positions of a mine-neighbouring cell have been added to positions_to_change, this for loop will work through them and decide if the output grid
        # (in this case, minefield) needs to be updated.
        for position in positions_to_change:

            #If the given row value is greater than 4 or less than 0, then it will not be possible to update the output grid as it only displays 5 rows. For this reason, pass is called to
            #avoid errors.
            if position[0] > 4 or position[0] < 0:
                pass

            #If the given inner-row value is greater than 4 or less than 0, then it will not be possible to update the output grid as it only displays 5 columns. For this reason, pass is 
            #called to avoid errors.    
            elif position[1] > 4 or position[1] < 0:
                pass

            #All values that are between 4 and 0 are fine and can be changed in the else block.    
            else:
                #This conditional checks that there isn't already a mine at the given co-ordinates. If there is, it passes and does not update. 
                if grid[position[0]][position[1]] == '#':
                    pass
                #Finally, the position will be iterated by 1. These were all set to 0 in the first set of loops from line 13.
                else:
                    grid[position[0]][position[1]] += 1



    #Displays the desired output as matrix form.
    for row in grid:
        #Map converts the entire row passed into it as string and joins it using the same amount of space. Yields uniform matrix output.
        print('  '.join(map(str, row)))


#Function called to display result with minefield list. 
    
minesweeper_generator(minefield)
