import board

tetris = board.Board((10,25))

pieces = []

game_alive = True

while game_alive:
    generate_new_piece()
    while piece_alive:
        game_output()
        instruction = input("What do you want to do")
        process_instruction(instruction)
        piece_alive = check_and_move_down()
    print("GAME OVER")



def game_ouput():
    print(tetris)

def process_instruction(cmd):
    if cmd == "D":
        print(current_shape)
    if cmd == "L":
        pass
        # move left
    if cmd == "R":
        pass
        # move right
    if cmd == "TL":
        pass
        # rotate left
    if cmd == "TR":
        pass
        # rotate right
    if cmd == "D":
        pass
        # move down