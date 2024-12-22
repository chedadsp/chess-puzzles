import chess
import chess.engine

engine_path = "stockfish/stockfish-ubuntu-x86-64-avx2"
# board = chess.Board()
#board = chess.Board("rk2K3/1PR5/8/1N2P3/8/8/3P4/1R6 w - - 0 1")
board = chess.Board("r3K3/kPR5/8/4P3/8/8/3P4/1R6 w - - 0 1")


def print_board():
    print(board)
    print()

print("Initial board position:")
print_board()

engine = chess.engine.SimpleEngine.popen_uci(engine_path, setpgrp=True)

while not board.is_game_over():
    result = engine.play(board, chess.engine.Limit(depth=50))
    board.push(result.move)
    print_board()
    print()

if board.is_checkmate():
    print("Checkmate achieved!")
else:
    print("Game over, but no checkmate.")

engine.quit()
