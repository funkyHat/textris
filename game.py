import board
from textris.shapes import s1, s2, l1, l2, t, square, line
import random


tetris = board.Board((10,25))

pieces = [
    (s1, "an S-shape"),
    (s2, "an S-shape"),
    (l1, "an L-shaped block"),
    (l2, "an L-shaped block"),
    (t, "a T-shaped block"),
    (square, "a 2x2 square"),
    (line, "a flat line 4 blocks long")]

def generate_new_piece():
    return random.choice(pieces)

def game_output():
    print(tetris)

def process_instruction(cmd, desc):
    if cmd == "D":
        print(f"I am a {desc}")
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
    if cmd == "F":
        pass
        # move down

def check_and_move_down():
    return True

game_alive = True

while game_alive:
    peice, desc = generate_new_piece()
    piece_alive = True
    while piece_alive:
        game_output()
        print("Your options are: \nD- describe \nL - Move left\n R - Move right\nTL - Turn Left\n TR - turn right\n F - Move down fast")
        instruction = input("What do you want to do?")
        process_instruction(instruction, desc)
        piece_alive = check_and_move_down()
    print("GAME OVER")

def rotate_left(*points):
    # rotate
    return [(point[1], -1 * point[0] + 3) for point in points]

def rotate_right(*points):
    return [(-1*point[1] + 3, point[0]) for point in points]
