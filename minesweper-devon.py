

import random  #for generating random numbers for mine placement
import sys     #for exiting the game if user hits a mine
import time    #for delays and typing effects




#game constants and initial variables
BOARD_SIZE = 10        #size of the board
MINE = 'M'             #symbol representing a mine
HIDDEN = '♦'           #symbol for hidden cells
FLAG = 'F'             #symbol for flagged cells
EMPTY = ' '            #symbol for empty cell
x = 1                  #counter for mine creation messages
MARK = '?'             #marker used for invalid input notifications
other_mark = '!'       #other marker for mine creation messages
NUM_MINES = 0          #number of mines to be placed
more = 0               #timing variable
m = 'm'                #repeated 'm' used to exaggerate output messages whennecessary
SCORE = 0              #players current score
high_score = 0         #highest score achieved




#typing effect function
def type_print(text, delay=0.03):

    for char in text:
        print(char, end='', flush=True)  #flush=True ensures immediate output
        time.sleep(delay)                #pauses between each character

    print()  #moves to the next line after finishing




#asking how many mines the user wants
while True:

    try:
        NUM_MINES = int(input(f"how many mines do you want {MARK} \n"))  #get user input

        #if theres too few mines then gives warning
        if NUM_MINES <= 4:

            print(f'ermm{m} thats not quite right?\n')
            m += 'm'  #adds another 'm' to exagerate
            time.sleep(0.67)

            print("invalid input, you MUST have 'MORE' than 4 mines\n")
            MARK += '?'  #adds extra question mark to exagerate more

        #if thers too many mines then warns user
        elif NUM_MINES >= 76:

            print(f'ermm{m} thats not quite right?\n')
            m += 'm'
            time.sleep(0.67)

            print("invalid input, you MUST have 'LESS' than 76 mines\n")
            MARK += '?'

        #valid number of mines
        else:
            print(f"\ngame starting with {NUM_MINES} mines\n")

            break  #exit loop if input is valid

    except ValueError:

        #making sure the user inputs a number
        print(f'ermm{m} thats not quite right?\n')
        m += 'm'
        time.sleep(0.67)

        print("invalid input, you need to enter a number\n")
        MARK += '?'  #adds extra question mark to exagerate





#announces mine creation
print(f'\ncreating {NUM_MINES} total mines\n\n')
time.sleep(2.00067)


#more variables
left = NUM_MINES
MAKING_NUM = left
not_sure = left
not_sure -= 1
mag = len(MARK)  #length of MARK used in timing delays




#loop to create mines visually for the user
while left != 0:

    while MAKING_NUM != 0:

        print(f'\nMINE {x} CREATED!\n')  #announces the mine creation process
        print(f'{not_sure} left{other_mark}\n\n')  #shows how many remaining mines left to create

        not_sure -= 1
        other_mark += '!'  #adds extra exclamations to exagerate
        x += 1
        MAKING_NUM -= 1

        left -= 1
        more += 0.5000676767  #adjusts delay 

        if more >= 4:
            more = 0.100000676767  #resets if the delay gets too large

        time.sleep(0.4000676767 + more)  #pauses to exagerate

        if x >= 12:
            more -= 0.435067676767  #makes the delay less as after too many user will get bord
            more = 0.67




#difficulty user selection
difficulty = input('easy standard medium or hard mode? \n').lower()  #gets user input

if difficulty == 'medium':

    NUM_MINES += 2  #adds extra mines
    time.sleep(0.5006767)

    print('\n+2 mines')
    time.sleep(1.67)
    print('+2 mines created!!\n\n')

elif difficulty == 'hard':

    NUM_MINES += 4  #more mines
    time.sleep(0.5006767)

    print('\n+4 mines')
    time.sleep(2.6767)
    print('\n+4 mines created!!!!\n\n')

elif difficulty == 'standard':
    time.sleep(0.067)  #standard mode so no changes

elif difficulty == 'easy':
    #shouldnt of chose easy
    print('why didnt you selected a harder mode')
    time.sleep(0.67)

    #changes MARK to exagerate
    if mag >= 4:
        MARK = '??'

    mag /= 10  #timing adjustment to exagerate depending on if user has had previous negligence

    type_print(f'????{MARK}', (0.1 + mag))  #typing effect

    NUM_MINES += 5  #add extra mines for easy mode making them regret picking it
    time.sleep(0.67)


else:
    print('difficulty set to hard :)')  #defults to hard if no right input
    NUM_MINES *= 2
    



#delaying things before game start
time.sleep(0.40067)

type_print('\n\n\n\n\nCREATING GAME\n\n', 0.100067)

time.sleep(1.0067)

type_print('\n\n', 0.67)



#countdown sequence
time.sleep(0.5006767)
print('3...')
time.sleep(1.00676767)

print('2..')
time.sleep(1.006767676767)

print('1.')
time.sleep(1.0067676767676767)



#adjusting timing for 'start' text
if mag >= 0.567:
    mag /= 2.67
type_print('START', (0.2167 + mag))
time.sleep(1.006767)



actual_board = []  #stores actual mine locations and numbers
user_board = []    #stores what user can see
mines_left = NUM_MINES
game_over = False





#function to place mines on the board
def create_board():

    global actual_board, user_board

    #initialise empty boards
    actual_board = [[0 for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]
    user_board = [[HIDDEN for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]

    mines_placed = 0  #counter for placed mines

    #randomly places mines
    while mines_placed < NUM_MINES:
        row = random.randint(0, BOARD_SIZE - 1)  #random row
        col = random.randint(0, BOARD_SIZE - 1)  #random column

        if actual_board[row][col] != MINE:  #only placeing iff its empty
            actual_board[row][col] = MINE
            mines_placed += 1

            #increments the numbers around mine
            for r in range(row - 1, row + 2):
                for c in range(col - 1, col + 2):
                    if 0 <= r < BOARD_SIZE and 0 <= c < BOARD_SIZE:  #inside board
                        if actual_board[r][c] != MINE:

                            try:
                                actual_board[r][c] += 1  #increments the nearby mine count

                            except TypeError:
                                pass  #ignores if theres a type error if cell is a mine






#function to display the board to the user
def display_board():

    column_headers = " ".join([str(i) for i in range(BOARD_SIZE)])  #header row
    print(f"\n  {column_headers}")

    border = "-" * (BOARD_SIZE * 2 + 2)  #horizontal border
    print(border)

    #prints each row
    for i, row in enumerate(user_board):

        row_str = " ".join([str(cell) for cell in row])
        print(f"{i}|{row_str}|")  #rows number and cells

    print(border)
    print(f"mines left: {mines_left}\n")  #shows remaining flags/mines






#function to reveal a cell
def reveal_cell(row, col):

    global game_over, high_score, SCORE

    #checks if the cords inputed is inside the board
    if not (0 <= row < BOARD_SIZE and 0 <= col < BOARD_SIZE): return

    #if its already revealed or flagged then it does nothing
    if user_board[row][col] in (EMPTY, FLAG) or str(user_board[row][col]).isdigit(): return #checks if the cell is already revealwd

    #checks if cords is a mine
    if actual_board[row][col] == MINE:

        game_over = True
        user_board[row][col] = MINE
        display_board()  #shows full board

        type_print('you hit a mine\n', 0.0167)
        type_print('...\n', 0.2367)
        type_print("\n\nGAME OVER   \n\n\n\n\n     :( \n\n\n", 0.1867)
        print(f'you had a score of {SCORE}')

        #updates high score if necessary
        if SCORE > high_score:
            high_score = SCORE
            print(f'you got a new high score of {high_score}')

        else:
            print(f'current high score is {high_score}')

        sys.exit()  #exits game straight away

    #reveals the number or empty cell
    cell_value = actual_board[row][col]
    user_board[row][col] = str(cell_value) if cell_value > 0 else EMPTY

    #if empty then its going to reveal surrounding cells
    if actual_board[row][col] == 0:

        for r in range(row - 1, row + 2):
            for c in range(col - 1, col + 2):
                reveal_cell(r, c)  #recursive reveal





#function which will toggle flag on a cell
def toggle_flag(row, col):

    global mines_left

    if user_board[row][col] == HIDDEN:
        user_board[row][col] = FLAG  #places flag
        mines_left -= 1

    elif user_board[row][col] == FLAG:
        user_board[row][col] = HIDDEN  #removes flag
        mines_left += 1




#function which will check if player has won
def check_win():

    for r in range(BOARD_SIZE):
        for c in range(BOARD_SIZE):

            if actual_board[r][c] != MINE and user_board[r][c] == HIDDEN:
                return False  #still unrevealed non mine cell exists

    return True  #all non mine cells revealed




#the main game loop
def play_game():
    create_board()

    global game_over, SCORE, high_score, m


    while not game_over:
        display_board()  #shows the current board

        try:
            print("'r' means reveal and 'f' means flag")
            time.sleep(0.1)
            print('flagging an already flagged cell will unflag it\n')
            move = input("type 'score' to see current score or enter move (eg, 'r 0 1' or 'f 0 1'): ").split()  #gets the user move
            
            #shows current score if user types 'score'
            if len(move) == 1 and move[0] == 'score':
                print(f'your score is {SCORE} with the current high score only being {high_score}\n\n')
                continue

            #invalid input handling
            if not move or len(move) != 3:
                type_print(f'ermm{m} thats not quite right?\n', 0.01)
                m += 'm'
                time.sleep(0.67)
                print("invalid input format you need to do 'action row col'")

                continue

            action = move[0].lower()  #'r' or 'f'
            row = int(move[1])
            col = int(move[2])

            #reveals cell
            if action == 'r':
                SCORE += 1  #increments the score by one
                reveal_cell(row, col)

            #flags  the cell
            elif action == 'f':
                toggle_flag(row, col)

            #invalid action input check
            else:
                type_print(f'ermm{m} thats not quite right?\n', 0.01)
                m += 'm'
                time.sleep(0.67)
                print("invalid move, use 'r' (reveal) or 'f' (flag).")

            #checks if player has won
            if check_win():
                print("congratulations! you cleared the field!")
                print(f'you got a score of {SCORE}\n')

                #updates the high score
                if SCORE > high_score:
                    high_score = SCORE
                    print(f'you got a new high score of {high_score}')

                else:
                    print(f'current high score is {high_score}')

                game_over = True
                display_board()  #final board display

        #handle invalid numbers or out of range input
        except (ValueError, IndexError):
            type_print(f'ermm{m} thats not quite right?\n', 0.01)
            m += 'm'
            time.sleep(0.67)
            print("invalid input, row and column must be valid numbers.")





#starts game
if __name__ == "__main__":
    play_game()





