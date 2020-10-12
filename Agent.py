"""
Player class
variables
     position = the initial player position within the board
     input = the player input for the console
Methods
    update_player_position(input)

"""


class Agent():
    def __init__(self, row_index=None, column_index=None, tag="", node=None):
        self.position = [row_index, column_index]
        self.node= node
        self.tag = tag

    def update_position(self):
        raise NotImplementedError("update_position")

    def return_position(self):
        return self.position

class Player(Agent):
    def __init__(self, row_index, column_index, node=None, tag="P"):
        self.row = row_index
        self.column = column_index
        self.node = node
        self.position = self.node.coordinates
        self.tag = tag


class Enemy(Agent):
    def __init__(self, row_index, column_index, node=None, tag="E"):
        self.row = row_index
        self.column = column_index
        self.node = node
        self.position = self.node.coordinates
        self.tag = tag





