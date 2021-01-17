import pygame
import sys

pygame.init()

window_width = 1000
window_height = 750

screen = pygame.display.set_mode((window_width, window_height))
background_colour = (255, 255, 255)

img = pygame.image.load("grid.JPG")

pygame.display.set_icon(img)
pygame.display.set_caption("Sudoku Solver")

screen.fill(background_colour)

number_font = pygame.font.Font('times-new-roman.ttf', 48)
large_font = pygame.font.Font('times-new-roman.ttf', 72)
normal_font = pygame.font.Font('times-new-roman.ttf', 30)
small_font = pygame.font.Font('times-new-roman.ttf', 24)


# Class to control the behaviour and appearance of buttons used in the GUI
class Button:
    def __init__(self, pos_x, pos_y, width, height, text):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.width = width
        self.height = height
        self.colour = (179, 179, 204)
        self.text = text

    def draw(self):
        pygame.draw.rect(screen, self.colour, pygame.Rect(self.pos_x, self.pos_y, self.width, self.height))

        button_text = normal_font.render(self.text, True, (0, 0, 0))

        screen.blit(button_text, (self.pos_x + (self.width / 2 - button_text.get_width() / 2),
                                  self.pos_y + (self.height / 2 - button_text.get_height() / 2)))

    def is_over(self, mouse_x, mouse_y):
        if self.pos_x < mouse_x < (self.pos_x + self.width):
            if self.pos_y < mouse_y < (self.pos_y + self.height):
                return True

        return False

    def hover_effect(self, mouse_x, mouse_y, hover_colour=(209, 209, 224)):
        if self.is_over(mouse_x, mouse_y) and self.colour != hover_colour:
            self.colour = hover_colour
            self.draw()
        elif (not self.is_over(mouse_x, mouse_y)) and self.colour != (179, 179, 204):
            self.colour = (179, 179, 204)
            self.draw()


# Class to control the behaviour and appearance of pop ups used in the GUI
class Popup:
    def __init__(self, pos_x, pos_y, width, height, text):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.width = width
        self.height = height
        self.text = text

    # render the pop up and its text onto the GUI, invoked in the activate_popup method
    def draw(self):

        popup_border = pygame.Rect(self.pos_x - 5, self.pos_y - 5, self.width + 10, self.height + 10)
        pygame.draw.rect(screen, (0, 0, 0), popup_border)

        close_button = pygame.Rect(self.pos_x, self.pos_y, 50, 50)
        pygame.draw.rect(screen, (209, 209, 224), close_button)

        popup = pygame.Rect(self.pos_x, self.pos_y, self.width, self.height)
        pygame.draw.rect(screen, (255, 255, 255), popup)

        text_list = self.text.split("\n")

        num_lines = (len(text_list) * 2) + 1

        for i in range(0, num_lines):
            if i % 2 == 0:
                text = ""

            else:
                index = i // 2
                text = text_list[index]

            popup_line = normal_font.render(text, True, (0, 0, 0))

            screen.blit(popup_line, (self.pos_x + (self.width / 2 - popup_line.get_width() / 2),
                                     self.pos_y + (self.height / num_lines) * i))

    # invokes draw method to render pop up and adds a close button, closes pop up when close button is pressed
    def activate_popup(self):
        self.draw()

        close_button = Button(self.pos_x, self.pos_y, 50, 50, "X")
        close_button.draw()

        while True:
            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.MOUSEMOTION:
                    mouse_x = event.pos[0]
                    mouse_y = event.pos[1]

                    close_button.hover_effect(mouse_x, mouse_y, (255, 51, 51))

                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_x = event.pos[0]
                    mouse_y = event.pos[1]

                    if close_button.is_over(mouse_x, mouse_y):
                        return

            pygame.display.update()


# Class to control the behaviour and appearance of sudoku board used in the GUI
class SudokuBoard:
    def __init__(self, board, board_x, board_y, square_width=50):
        self.board = board
        self.board_x = board_x
        self.board_y = board_y
        self.square_width = square_width
        self.board_width = ((square_width + 1) * 9) + 1

    # Add number in board list at given position to board gui
    def add_number_to_gui(self, pos_x, pos_y):
        # Find the x any y coordinates of the top left corner of the square
        square_x = self.board_x + (self.square_width + 1) * pos_x
        square_y = self.board_y + (self.square_width + 1) * pos_y

        # cover the previous contents of this square using a white square
        square = pygame.Rect(square_x + 1, square_y + 1, self.square_width - 1, self.square_width - 1)
        pygame.draw.rect(screen, (255, 255, 255), square)

        board_num = self.board[pos_y][pos_x]

        if board_num != 0:
            text = number_font.render(str(board_num), True, (0, 0, 0))

            # find x and y coordinate for number to appear in the middle of the square
            num_x = square_x + (self.square_width / 2 - text.get_width() / 2)
            num_y = square_y + (self.square_width / 2 - text.get_height() / 2)

            screen.blit(text, (num_x, num_y))

    # Add all numbers in board list to GUI
    def print_board_gui(self):
        for i in range(0, 9):
            for j in range(0, 9):
                self.add_number_to_gui(i, j)

    # Print board list to console
    def print_board_console(self):
        for i in range(0, 9):
            print("| ", end="")
            for j in range(0, 9):
                print(str(self.board[i][j]) + " | ", end="")
            print()

    # Draw a blank board GUI
    def draw_blank_board(self):

        background = pygame.Rect(self.board_x, self.board_y, self.board_width, self.board_width)

        pygame.draw.rect(screen, (0, 0, 0), background)

        x = self.board_x + 1
        y = self.board_y + 1

        for i in range(9):
            for j in range(9):
                square = pygame.Rect(x, y, self.square_width, self.square_width)
                pygame.draw.rect(screen, (255, 255, 255), square)

                x += self.square_width + 1

            x = self.board_x + 1
            y += self.square_width + 1

    # Set all elements in board list to zero and clear all numbers from GUI board
    def clear_board(self):
        for i in range(0, 9):
            for j in range(0, 9):
                self.board[i][j] = 0

                num_x = self.board_x + (self.square_width + 1) * i
                num_y = self.board_y + (self.square_width + 1) * j

                square = pygame.Rect(num_x + 1, num_y + 1, self.square_width - 1, self.square_width - 1)
                pygame.draw.rect(screen, (255, 255, 255), square)

    # Check if board list has any unfilled numbers
    def check_board_complete(self):
        for i in range(0, 9):
            for j in range(0, 9):
                if self.board[i][j] == 0:
                    return False

        return True


# Clears old screen then sets appearance and controls behaviour of custom page
def custom_solve():
    screen.fill(background_colour)

    menu_button = Button(5, 5, 100, 50, "Menu")
    menu_button.draw()

    solve_button = Button(250, 25, 200, 50, "Solve Puzzle")
    solve_button.draw()

    clear_button = Button(550, 25, 200, 50, "Clear Puzzle")
    clear_button.draw()

    board = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]

    sudoku_puzzle = SudokuBoard(board, 270, 100, 50)

    sudoku_puzzle.draw_blank_board()
    sudoku_puzzle.print_board_gui()

    num = -1

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # set num variable to the number key pressed
            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_0:
                    num = 0
                elif event.key == pygame.K_1:
                    num = 1
                elif event.key == pygame.K_2:
                    num = 2
                elif event.key == pygame.K_3:
                    num = 3
                elif event.key == pygame.K_4:
                    num = 4
                elif event.key == pygame.K_5:
                    num = 5
                elif event.key == pygame.K_6:
                    num = 6
                elif event.key == pygame.K_7:
                    num = 7
                elif event.key == pygame.K_8:
                    num = 8
                elif event.key == pygame.K_9:
                    num = 9

            # creates hover effect if mouse is over a button
            if event.type == pygame.MOUSEMOTION:
                mouse_x = event.pos[0]
                mouse_y = event.pos[1]

                menu_button.hover_effect(mouse_x, mouse_y)

                solve_button.hover_effect(mouse_x, mouse_y)

                clear_button.hover_effect(mouse_x, mouse_y)

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x = event.pos[0]
                mouse_y = event.pos[1]

                if menu_button.is_over(mouse_x, mouse_y):
                    main_menu()

                if clear_button.is_over(mouse_x, mouse_y):
                    sudoku_puzzle.clear_board()

                if solve_button.is_over(mouse_x, mouse_y):

                    solve_button.text = "Solving..."
                    solve_button.draw()

                    pygame.display.update()

                    if check_starting_board(sudoku_puzzle):
                        if check_square(sudoku_puzzle, 0, 0):
                            sudoku_puzzle.print_board_gui()
                            print("Done")
                        else:
                            # Inputted board has no solution
                            print("Could not solve puzzle")
                            error_popup = Popup(300, 200, 400, 200, "Error\nBoard could not be solved")
                            error_popup.activate_popup()

                            # Redraw board when popup is closed
                            sudoku_puzzle.draw_blank_board()
                            sudoku_puzzle.print_board_gui()
                    else:
                        # Inputted board does not follow sudoku rules
                        print("Starting board is not valid")
                        error_popup = Popup(300, 200, 400, 200, "Invalid Board\nPlease correct it")
                        error_popup.activate_popup()

                        # Redraw board when popup is closed
                        sudoku_puzzle.draw_blank_board()
                        sudoku_puzzle.print_board_gui()

                    solve_button.text = "Solve Puzzle"
                    solve_button.draw()

                # if mouse is somewhere on the sudoku board
                elif sudoku_puzzle.board_x < mouse_x < sudoku_puzzle.board_x + sudoku_puzzle.board_width and \
                        sudoku_puzzle.board_y < mouse_y < sudoku_puzzle.board_y + sudoku_puzzle.board_width:

                    # calculate the x and y position of the square on the board that was clicked
                    pos_x = (mouse_x - sudoku_puzzle.board_x) // (sudoku_puzzle.square_width + 1)
                    pos_y = (mouse_y - sudoku_puzzle.board_y) // (sudoku_puzzle.square_width + 1)

                    # if a number was previously pressed
                    if num != -1:

                        # find x and y coordinate of the square on the screen
                        square_x = sudoku_puzzle.board_x + (sudoku_puzzle.square_width + 1) * pos_x
                        square_y = sudoku_puzzle.board_y + (sudoku_puzzle.square_width + 1) * pos_y

                        # num is zero, hide old number with a rectangle, removing it from the screen
                        if num == 0:
                            square = pygame.Rect(square_x + 1, square_y + 1,
                                                 sudoku_puzzle.square_width - 1, sudoku_puzzle.square_width - 1)

                            pygame.draw.rect(screen, (255, 255, 255), square)

                        else:
                            # If there is another number on the board, hide it first
                            if sudoku_puzzle.board[pos_y][pos_x] != 0:
                                square = pygame.Rect(square_x + 1, square_y + 1,
                                                     sudoku_puzzle.square_width - 1, sudoku_puzzle.square_width - 1)

                                pygame.draw.rect(screen, (255, 255, 255), square)

                            text = number_font.render(str(num), True, (0, 0, 0))

                            # find x and y coordinate for number to appear in the middle of the square
                            num_x = square_x + (sudoku_puzzle.square_width / 2 - text.get_width() / 2)
                            num_y = square_y + (sudoku_puzzle.square_width / 2 - text.get_height() / 2)

                            screen.blit(text, (num_x, num_y))

                        sudoku_puzzle.board[pos_y][pos_x] = num

        pygame.display.update()


# Clears old screen then sets appearance and controls behaviour of main menu page
def main_menu():
    screen.fill(background_colour)

    text = large_font.render("Sudoku Solver", True, (0, 0, 0))

    screen.blit(text, ((window_width / 2 - text.get_width() / 2), 100))

    example_button = Button(300, 300, 400, 50, "Solve Example Puzzle")
    example_button.draw()

    custom_button = Button(300, 400, 400, 50, "Solve Custom Puzzle")
    custom_button.draw()

    instruction_button = Button(300, 500, 400, 50, "Read Instructions")
    instruction_button.draw()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # creates hover effect if mouse is over a button
            if event.type == pygame.MOUSEMOTION:
                mouse_x = event.pos[0]
                mouse_y = event.pos[1]

                example_button.hover_effect(mouse_x, mouse_y)

                custom_button.hover_effect(mouse_x, mouse_y)

                instruction_button.hover_effect(mouse_x, mouse_y)

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x = event.pos[0]
                mouse_y = event.pos[1]

                if example_button.is_over(mouse_x, mouse_y):
                    example_puzzle()

                if instruction_button.is_over(mouse_x, mouse_y):
                    instructions_screen()

                if custom_button.is_over(mouse_x, mouse_y):
                    custom_solve()

        pygame.display.update()


# Clears old screen then sets appearance and controls behaviour of example puzzle page
def example_puzzle():
    screen.fill(background_colour)

    menu_button = Button(5, 5, 100, 50, "Menu")
    menu_button.draw()

    solve_button = Button(250, 25, 200, 50, "Solve Puzzle")
    solve_button.draw()

    clear_button = Button(550, 25, 200, 50, "Clear Puzzle")
    clear_button.draw()

    easy_button = Button(150, 100, 200, 50, "Easy Puzzle")
    easy_button.draw()

    medium_button = Button(400, 100, 200, 50, "Medium Puzzle")
    medium_button.draw()

    hard_button = Button(650, 100, 200, 50, "Hard Puzzle")
    hard_button.draw()

    board = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]

    sudoku_puzzle = SudokuBoard(board, 270, 200, 50)

    sudoku_puzzle.draw_blank_board()
    sudoku_puzzle.print_board_gui()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # creates hover effect if mouse is over a button
            if event.type == pygame.MOUSEMOTION:
                mouse_x = event.pos[0]
                mouse_y = event.pos[1]

                menu_button.hover_effect(mouse_x, mouse_y)

                solve_button.hover_effect(mouse_x, mouse_y)

                easy_button.hover_effect(mouse_x, mouse_y)

                medium_button.hover_effect(mouse_x, mouse_y)

                hard_button.hover_effect(mouse_x, mouse_y)

                clear_button.hover_effect(mouse_x, mouse_y)

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x = event.pos[0]
                mouse_y = event.pos[1]

                if menu_button.is_over(mouse_x, mouse_y):
                    main_menu()

                if clear_button.is_over(mouse_x, mouse_y):
                    sudoku_puzzle.clear_board()

                if solve_button.is_over(mouse_x, mouse_y):

                    solve_button.text = "Solving..."
                    solve_button.draw()

                    pygame.display.update()

                    if check_square(sudoku_puzzle, 0, 0):
                        sudoku_puzzle.print_board_gui()
                        print("Done")
                    else:
                        print("Could not solve puzzle")

                    solve_button.text = "Solve Puzzle"
                    solve_button.draw()

                if easy_button.is_over(mouse_x, mouse_y):
                    sudoku_puzzle.board = sample_puzzle("easy")
                    sudoku_puzzle.print_board_gui()

                if medium_button.is_over(mouse_x, mouse_y):
                    sudoku_puzzle.board = sample_puzzle("medium")
                    sudoku_puzzle.print_board_gui()

                if hard_button.is_over(mouse_x, mouse_y):
                    sudoku_puzzle.board = sample_puzzle("hard")
                    sudoku_puzzle.print_board_gui()

        pygame.display.update()


# Clears old screen then add the instruction text in the instructions page
def instructions_screen():
    screen.fill(background_colour)

    menu_button = Button(5, 5, 100, 50, "Menu")
    menu_button.draw()

    text = large_font.render("Application Instructions", True, (0, 0, 0))
    screen.blit(text, ((window_width / 2 - text.get_width() / 2), 100))

    text = small_font.render("Thanks for using my application, here is some information on how to use this program.",
                             True, (0, 0, 0))
    screen.blit(text, (100, 250))

    text = small_font.render("There are two modes of the program, example puzzle mode and custom mode.",
                             True, (0, 0, 0))
    screen.blit(text, (100, 275))

    text = small_font.render("The example puzzle mode lets you choose a saved easy, medium or hard puzzle to solve.",
                             True, (0, 0, 0))
    screen.blit(text, (100, 350))

    text = small_font.render("The custom puzzle mode starts with a blank board where you can add your own numbers",
                             True, (0, 0, 0))
    screen.blit(text, (100, 400))

    text = small_font.render("by pressing a number key and clicking on the square you want to add the number to,",
                             True, (0, 0, 0))
    screen.blit(text, (100, 425))

    text = small_font.render("you would then be able to solve the puzzle you entered with the solve button.",
                             True, (0, 0, 0))
    screen.blit(text, (100, 450))

    text = small_font.render("This program should be able to solve any sudoku puzzle, but note that more complex",
                             True, (0, 0, 0))
    screen.blit(text, (100, 500))

    text = small_font.render("puzzles may take 10-15 seconds to solve.",
                             True, (0, 0, 0))
    screen.blit(text, (100, 525))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # creates hover effect if mouse is over a button
            if event.type == pygame.MOUSEMOTION:
                mouse_x = event.pos[0]
                mouse_y = event.pos[1]

                menu_button.hover_effect(mouse_x, mouse_y)

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x = event.pos[0]
                mouse_y = event.pos[1]

                if menu_button.is_over(mouse_x, mouse_y):
                    main_menu()

        pygame.display.update()


# Returns sample puzzle based on the selected difficulty
def sample_puzzle(difficulty):
    if difficulty == "easy":
        return [
            [0, 3, 7, 8, 0, 0, 2, 9, 1],
            [0, 0, 1, 7, 0, 6, 0, 3, 0],
            [5, 9, 4, 0, 2, 0, 0, 0, 0],
            [0, 0, 0, 9, 0, 0, 8, 7, 5],
            [2, 0, 0, 0, 6, 7, 0, 1, 0],
            [0, 0, 0, 0, 4, 8, 9, 0, 0],
            [3, 6, 5, 2, 0, 0, 0, 0, 0],
            [9, 0, 0, 0, 1, 3, 6, 0, 2],
            [0, 1, 0, 6, 0, 0, 3, 0, 9]
        ]

    elif difficulty == "medium":
        return [
            [0, 0, 1, 0, 0, 2, 0, 0, 0],
            [0, 0, 0, 8, 4, 0, 0, 5, 0],
            [0, 8, 0, 0, 0, 0, 0, 1, 0],
            [0, 6, 0, 0, 0, 8, 0, 0, 0],
            [0, 0, 7, 6, 0, 0, 3, 0, 0],
            [0, 1, 0, 9, 0, 0, 0, 0, 7],
            [0, 2, 5, 0, 0, 0, 0, 8, 0],
            [7, 0, 0, 0, 0, 4, 2, 0, 0],
            [0, 0, 0, 0, 3, 0, 0, 0, 0]
        ]

    elif difficulty == "hard":

        return [
            [0, 0, 0, 7, 0, 0, 0, 0, 4],
            [6, 0, 0, 0, 0, 0, 8, 0, 0],
            [0, 4, 0, 5, 0, 1, 0, 0, 0],
            [0, 0, 0, 1, 0, 0, 0, 0, 0],
            [7, 0, 6, 0, 5, 0, 9, 0, 0],
            [0, 0, 3, 0, 0, 8, 2, 0, 0],
            [0, 0, 0, 2, 0, 0, 0, 0, 0],
            [0, 0, 8, 0, 0, 4, 0, 9, 3],
            [0, 1, 0, 0, 7, 0, 5, 0, 0]
        ]


# looks for valid number for square at given x and y position
# sets board variable at the given position to valid number if a valid number is found
# then recursively calls itself with next x and y position
# tries another valid number if recursive function returns false
# returns false in no valid number is found
def check_square(sudoku_puzzle, x_pos, y_pos):
    if y_pos >= 9:
        y_pos = 0
        x_pos += 1

    current_square = (x_pos * 9) + y_pos

    # cycled through every square
    if current_square == 81:
        return True

    # default number in the puzzle
    elif sudoku_puzzle.board[x_pos][y_pos] != 0:
        return check_square(sudoku_puzzle, x_pos, y_pos + 1)

    # blank space
    else:
        for i in range(1, 10):

            # if i is a valid value for this location
            if check_square_value(sudoku_puzzle, x_pos, y_pos, i):
                sudoku_puzzle.board[x_pos][y_pos] = i
                status = check_square(sudoku_puzzle, x_pos, y_pos + 1)

                if not status:
                    continue
                else:
                    return True

    # If this point is reached, they are no correct values for this position, meaning a previous value is incorrect
    # set this square to the blank value and return False indicating a previous square must be changed
    sudoku_puzzle.board[x_pos][y_pos] = 0
    return False


# checks if given value is valid in the given x and y position according to rules of sudoku
def check_square_value(sudoku_puzzle, x_pos, y_pos, value):
    # check row
    for y in range(0, 9):
        if sudoku_puzzle.board[x_pos][y] == value and y != y_pos:
            return False

    # check column
    for x in range(0, 9):
        if sudoku_puzzle.board[x][y_pos] == value and x != x_pos:
            return False

    x_start = (x_pos // 3) * 3
    y_start = (y_pos // 3) * 3

    # check 3 x 3 square
    for i in range(x_start, x_start + 3):
        for j in range(y_start, y_start + 3):
            if sudoku_puzzle.board[i][j] == value and (i != x_pos and j != y_pos):
                return False

    return True


# check if all the numbers on the board follow the rules of Sudoku
def check_starting_board(sudoku_puzzle):
    for i in range(0, 9):
        for j in range(0, 9):
            if sudoku_puzzle.board[i][j] != 0:
                # the value in the square is not valid, return false
                if not check_square_value(sudoku_puzzle, i, j, sudoku_puzzle.board[i][j]):
                    return False

    return True


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main_menu()
