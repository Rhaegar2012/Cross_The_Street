"""
Creates a 16x16 board representation in a list
Numpy array not used to the immutability of the board and its small size
Class Board()
    variables
    player--Player object
    enemy-- Enemy object
    methods
    returnBoardPosition(index)
    PlaceEnemy()
    PlacePlayer()
    display_board()
"""

import random
import Agent
"""
Node Class stores node information for each node in the board
"""


class Node():
    def __init__(self, coordinates):
        self.coordinates = coordinates
        self.neighbors = []

    def create_neighbors(self, board_nodes):
        directions = [(1, 0), [0, 1], [-1, 0], [0, -1]]
        for direction in directions:
            neighbor_coordinates = (self.coordinates[0]+direction[0], self.coordinates[1]+direction[1])
            for j in board_nodes:
                if j.coordinates == neighbor_coordinates:
                    self.neighbors.append(j)

    def return_coordinates(self):
        return self.coordinates

    def return_neighbors(self):
        return self.neighbors


class Board():
    def __init__(self, player=None, enemy=None):
        self.main_board = [["_", "_", "_", "_", "_", "_", "_", "_", "_", "_"],
                           ["_", "_", "_", "_", "_", "_", "_", "_", "_", "_"],
                           ["_", "_", "_", "_", "_", "_", "_", "_", "_", "_"],
                           ["_", "_", "_", "_", "_", "_", "_", "_", "_", "_"],
                           ["_", "_", "_", "_", "_", "_", "_", "_", "_", "_"],
                           ["_", "_", "_", "_", "_", "_", "_", "_", "_", "_"],
                           ["_", "_", "_", "_", "_", "_", "_", "_", "_", "_"],
                           ["_", "_", "_", "_", "_", "_", "_", "_", "_", "_"],
                           ["_", "_", "_", "_", "_", "_", "_", "_", "_", "_"],
                           ["_", "_", "_", "_", "_", "_", "_", "_", "_", "_"]]

        self.nodes = []
        self.player = player
        self.enemy = enemy

    def place_player(self):
        player_row_index = 9
        player_column_index = 5
        for i in self.nodes:
            if i.coordinates == (player_row_index, player_column_index):
                player_node = i
        player = Agent.Player(player_row_index, player_column_index, player_node)
        player.node = player_node
        self.player = player
        self.main_board[player.row][player.column] = player.tag

    def place_enemy(self):
        enemy_row_index = random.randint(0, 9)
        enemy_column_index = random.randint(0, 9)
        for i in self.nodes:
            if i.coordinates == (enemy_row_index, enemy_column_index):
                enemy_node = i
        enemy = Agent.Enemy(enemy_row_index, enemy_column_index, enemy_node)
        self.main_board[enemy.row][enemy.column] = enemy.tag
        self.enemy = enemy

    def create_nodes(self):
        board_height = len(self.main_board)
        board_width = len(self.main_board[0])
        for x in range(board_width):
            for y in range(board_height):
                node = Node((x, y))
                self.nodes.append(node)

    def create_node_neighbors(self):
        for node in self.nodes:
            node.create_neighbors(self.nodes)

    def display_board(self):
        for i in self.main_board:
            print(i)



board = Board()
board.create_nodes()
board.create_node_neighbors()
board.place_player()
board.place_enemy()
board.display_board()





