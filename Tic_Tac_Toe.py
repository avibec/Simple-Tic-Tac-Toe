
cells = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
print("---------")
print(f'| {cells[0]} {cells[1]} {cells[2]} |')
print(f'| {cells[3]} {cells[4]} {cells[5]} |')
print(f'| {cells[6]} {cells[7]} {cells[8]} |')
print("---------")
x_turn = True
y_turn = False
end_game = False


def stage():
    row = [cells[0:3], cells[3:6], cells[6:9]]
    col = [cells[0:7:3], cells[1:8:3], cells[2:9:3]]
    diagonal_left_right = cells[0] + cells[4] + cells[8]
    diagonal_right_left = cells[2] + cells[4] + cells[6]
    diagonal = [diagonal_left_right, diagonal_right_left]
    matrix = [row, col, diagonal]

    x_win = o_win = blanks = x_ = o_ = 0

    for c in cells:
        if c == "X":
            x_ += 1
    for c in cells:
        if c == "O":
            o_ += 1
    for c in cells:
        if c == " ":
            blanks += 1
    for n in matrix:
        for x in n:
            if "".join(x) == "XXX":
                x_win += 1
    for n in matrix:
        for x in n:
            if "".join(x) == "OOO":
                o_win += 1

    if x_ - o_ == 1 or x_ - o_ == 0 or x_ - o_ == -1:
        if x_win + o_win > 1:
            print("Impossible")
        elif x_win == 1 and o_win == 0:
            print("X wins")
        elif o_win == 1 and x_win == 0:
            print("O wins")
        elif x_win + o_win == 0:
            if blanks == 0:
                print("Draw")
            elif blanks > 0:
                print("Game not finished")
                move()
    else:
        print("Impossible")


def move():
    global x_turn
    global y_turn
    global end_game
    flag = True
    while flag:
        print("Enter the coordinates: ")
        x, y = input().split()
        valid = ["1", "2", "3"]

        if x.isnumeric() is False or y.isnumeric() is False:
            print("You should enter numbers!")

        # check for coordinates in range
        elif x not in valid or y not in valid:
            print("Coordinates should be from 1 to 3!")
        else:
            # turn coordinates into index
            index = ((int(x) - 1) * 3) + (int(y) + 2) - 3
            if x_turn:
                # check cell is not occupied
                if cells[index] == " ":
                    # put 'X' in empty cell
                    cells[index] = "X"
                    print("""---------""")
                    print(f'| {cells[0]} {cells[1]} {cells[2]} |')
                    print(f'| {cells[3]} {cells[4]} {cells[5]} |')
                    print(f'| {cells[6]} {cells[7]} {cells[8]} |')
                    print("""---------""")
                    flag = False
                    x_turn = False
                    y_turn = True
                    if not end_game:
                        stage()
                else:
                    print("This cell is occupied! Choose another one!")
            else:
                # check cell is not occupied
                if cells[index] == " ":
                    # put 'X' in empty cell
                    cells[index] = "O"
                    print("""---------""")
                    print(f'| {cells[0]} {cells[1]} {cells[2]} |')
                    print(f'| {cells[3]} {cells[4]} {cells[5]} |')
                    print(f'| {cells[6]} {cells[7]} {cells[8]} |')
                    print("""---------""")
                    flag = False
                    x_turn = True
                    y_turn = False
                    if not end_game:
                        stage()
                else:
                    print("This cell is occupied! Choose another one!")


stage()
