ROCK = "A"
PAPER = "B"
SCISSORS = "C"
LOSS_OUTCOME = "X"
DRAW_OUTCOME = "Y"
WIN_OUTCOME = "Z"
WIN = 6
DRAW = 3
LOSS = 0

PLAY_SCORE = {ROCK: 1, PAPER: 2, SCISSORS: 3}


def shoot(op_play, outcome):

    if op_play == ROCK and outcome == WIN_OUTCOME:
        my_play = PAPER
        return WIN + PLAY_SCORE[my_play]
    if op_play == ROCK and outcome == DRAW_OUTCOME:
        my_play = ROCK
        return DRAW + PLAY_SCORE[my_play]
    if op_play == ROCK and outcome == LOSS_OUTCOME:
        my_play = SCISSORS
        return LOSS + PLAY_SCORE[my_play]

    if op_play == PAPER and outcome == WIN_OUTCOME:
        my_play = SCISSORS
        return WIN + PLAY_SCORE[my_play]
    if op_play == PAPER and outcome == DRAW_OUTCOME:
        my_play = PAPER
        return DRAW + PLAY_SCORE[my_play]
    if op_play == PAPER and outcome == LOSS_OUTCOME:
        my_play = ROCK
        return LOSS + PLAY_SCORE[my_play]

    if op_play == SCISSORS and outcome == WIN_OUTCOME:
        my_play = ROCK
        return WIN + PLAY_SCORE[my_play]
    if op_play == SCISSORS and outcome == DRAW_OUTCOME:
        my_play = SCISSORS
        return DRAW + PLAY_SCORE[my_play]
    if op_play == SCISSORS and outcome == LOSS_OUTCOME:
        my_play = PAPER
        return LOSS + PLAY_SCORE[my_play]

with open("puzzle_2/puzzle_2_input.txt") as file:
    total_score = 0
    for line in file:
        op_play = line[0]
        my_play = line[2]

        round_score = shoot(op_play, my_play)
        total_score = total_score + round_score

    print(total_score)