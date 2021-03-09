from Models.game import Game
from Models.node import Node
from Models.nodetype import NodeType


# Controller for managing game actions


#  Creates a new game and returns the game for appending the games array in main
def create_new_game(game_id, nodes):
    game_nodes = []
    for node in nodes:
        for nodeType in NodeType:
            if nodeType.value == node:
                new_node = Node(len(game_nodes) + 1, nodeType, [])
                game_nodes.append(new_node)
                continue
    if len(nodes) == len(game_nodes):
        new_game = Game(game_id, game_nodes)
        return new_game
    else:
        return False


# Checks if the move is valid
def control_move(game, node_from, node_to):
    if len(game.nodes[node_from - 1].connections) < 2 and len(game.nodes[node_to - 1].connections) < 2 and game.nodes[
        node_from - 1].node_type.value != game.nodes[node_to - 1].node_type.value:
        # i did the control like this because in the future maybe max connection number can change. if not,
        # we can do this like: if game.nodes[node_from].connections[0] != game.nodes[node_to].node_type.value
        for node_id in game.nodes[node_from - 1].connections:
            if game.nodes[node_id - 1].node_type == game.nodes[node_to - 1].node_type:
                return False
        for node_id in game.nodes[node_to - 1].connections:
            if game.nodes[node_id - 1].node_type == game.nodes[node_from - 1].node_type:
                return False
        return True


# If the move is valid, it writes the move to the game object
def make_move(game, node_from, node_to):
    if control_move(game=game, node_from=node_from, node_to=node_to):
        game.nodes[node_to - 1].connections.append(node_from)
        game.nodes[node_from - 1].connections.append(node_to)
        if control_finish(game):
            game = finish_game(game)
            game.switch_player()
            return game
        else:
            game.switch_player()
            return game
    else:
        return False


# It checks if the game is finished
def control_finish(game):
    not_full_nodes = []
    for node in game.nodes:
        if len(node.connections) < 2:
            not_full_nodes.append(node)
    if len(not_full_nodes) > 1:
        for node1 in not_full_nodes:
            for node2 in not_full_nodes:
                if control_move(game, node1.node_id, node2.node_id):
                    return False
        return True
    else:
        return True


# Writes down the finish at the game object
def finish_game(game):
    game.winner = game.current_player.value
    return game
