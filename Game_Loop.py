"""
Game Loop Functions
game_loop() - Executes game loop
create_board() - Creates the initial board state
move_player() - updates player position according to input
move_enemy() - enemy movement based on the A* algorithm
"""
import Board
import Queue

def game_loop():
    win = False
    loss = False
    board = create_board()
    while not win or not loss:
        player_board = move_player(board)
        enemy_board = move_enemy(player_board)
        win = check_if_win(enemy_board, win)
        loss = check_if_lost(enemy_board, loss)


def create_board():
    board = Board.Board()
    board.create_nodes()
    board.create_node_neighbors()
    board.place_player()
    board.place_enemy()
    board.display_board()
    return board


def move_player(board):
    move = input("Direction: ")
    board.main_board[board.player.node.coordinates[0]][board.player.node.coordinates[1]] = "_"
    if move == "up":
        direction = [-1, 0]
    elif move == "down":
        direction = [1, 0]
    elif move == "left":
        direction = [0, -1]
    elif move == "right":
        direction = [0, 1]
    new_position = (board.player.node.coordinates[0]+direction[0], board.player.node.coordinates[1]+direction[1])
    for i in board.nodes:
        if i.coordinates == new_position:
            new_node = i
    board.player.node = new_node
    board.main_board[board.player.node.coordinates[0]][board.player.node.coordinates[1]] = "P"
    board.display_board()
    return board


def move_enemy(board):
    player_node = board.player.node
    enemy_node = board.enemy.node
    """
    Enemy agent scans the board 
    """
    frontier = Queue.Queue()
    frontier.enqueue(enemy_node)
    came_from={}
    came_from[enemy_node] = None
    while not frontier.is_empty():
        current = frontier.dequeue()
        for nxt in current.neighbors:
            if nxt not in came_from:
                frontier.enqueue(nxt)
                came_from[nxt] = current
    """
    Enemy Agent builds the path towards the player 
    """
    current = player_node
    path = []
    while current != enemy_node:
        path.append(current)
        current = came_from[current]
    path.append(enemy_node)
    path.reverse()
    for i in path:
        print(i.coordinates)
    """
    Updates the enemy position in the board based on the constructed path towards the player
    """
    board.main_board[board.enemy.node.coordinates[0]][board.enemy.node.coordinates[1]] = "_"
    board.enemy.node = path[2]
    board.main_board[board.enemy.node.coordinates[0]][board.enemy.node.coordinates[1]] = "E"
    board.display_board()
    return board


def check_if_win(board, win):
    player_pos = board.player.node.coordinates
    if player_pos[0] == 0:
        print("You win!, Play Again?")
        win = True
    return win


def check_if_lost (board, loss):
    player_pos = board.player.node.coordinates
    enemy_pos = board.enemy.node.coordinates
    if player_pos == enemy_pos:
        print("You lose!, Play Again?")
        loss = True
    return loss







