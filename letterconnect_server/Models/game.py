from Models.player import Player


class Game:
    def __init__(self, game_id, nodes):
        self.game_id = game_id
        self.winner = None
        self.current_player = Player.first
        self.nodes = nodes

    def switch_player(self):
        if self.current_player == Player.first:
            self.current_player = Player.second
        elif self.current_player == Player.second:
            self.current_player = Player.first

    def get_nodes(self):
        nodes = []
        for i in self.nodes:
            nodes.append(i.toJson())
        return nodes

    def toJson(self):
        return {
            "winner": self.winner,
            "current_player": self.current_player.value,
            "nodes": self.get_nodes()
        }
