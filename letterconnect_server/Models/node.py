class Node:
    def __init__(self, node_id, node_type, connections):
        self.node_id = node_id
        self.node_type = node_type
        self.connections = connections

    def toJson(self):
        return {
            "id": self.node_id,
            "type": self.node_type.value,
            "connections": self.connections
        }
