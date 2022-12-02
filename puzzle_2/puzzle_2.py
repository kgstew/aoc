OP_ROCK = "A"
OP_PAPER = "B"
OP_SCISSORS = "C"
ME_ROCK = "X"
ME_PAPER = "Y"
ME_SCISSORS = "Z"
WIN = 6
DRAW = 3
LOSS = 0

PLAY_SCORE = {ME_ROCK: 1, ME_PAPER: 2, ME_SCISSORS: 3}


def shoot(op_play, my_play):
    play_score = PLAY_SCORE[my_play]
    if op_play == OP_ROCK and my_play == ME_ROCK:
        return DRAW + play_score
    if op_play == OP_ROCK and my_play == ME_SCISSORS:
        return LOSS + play_score
    if op_play == OP_ROCK and my_play == ME_PAPER:
        return WIN + play_score
    
    if op_play == OP_SCISSORS and my_play == ME_ROCK:
        return WIN + play_score
    if op_play == OP_SCISSORS and my_play == ME_SCISSORS:
        return DRAW + play_score
    if op_play == OP_SCISSORS and my_play == ME_PAPER:
        return LOSS + play_score

    if op_play == OP_PAPER and my_play == ME_ROCK:
        return LOSS + play_score
    if op_play == OP_PAPER and my_play == ME_SCISSORS:
        return WIN + play_score
    if op_play == OP_PAPER and my_play == ME_PAPER:
        return DRAW + play_score
    

with open("puzzle_2/puzzle_2_input.txt") as file:
    total_score = 0
    for line in file:
        op_play = line[0]
        my_play = line[2]

        round_score = shoot(op_play, my_play)
        total_score = total_score + round_score

    print(total_score)