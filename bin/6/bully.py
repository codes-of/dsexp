class BullyAlgorithm:
    def __init__(self, nodeId, nodes):
        self.nodeId = nodeId
        self.nodes = nodes

    def startElection(self):
        highestNodeId = self.nodeId

        # Send "Coordinator Election" messages to all higher ID nodes
        for i in range(self.nodeId + 1, len(self.nodes) + 1):
            if i in self.nodes:
                print(f"Node {self.nodeId} sends Coordinator Election message to Node {i}")

        # Wait for "OK" messages from all higher ID nodes
        for i in range(self.nodeId + 1, len(self.nodes) + 1):
            if i in self.nodes:
                print(f"Node {self.nodeId} waiting for OK message from Node {i}")

        # Check if there is a higher ID node that responded
        for i in range(self.nodeId + 1, len(self.nodes) + 1):
            if i in self.nodes:
                print(f"Node {self.nodeId} received OK message from Node {i}")
                highestNodeId = i

        # If there is a higher ID node, send "Coordinator" message to that node
        if highestNodeId != self.nodeId:
            print(f"Node {self.nodeId} sends Coordinator message to Node {highestNodeId}")

        # Otherwise, become the coordinator
        else:
            print(f"Node {self.nodeId} is the new coordinator")


# Create a list of node IDs
nodes = [1, 2, 3, 4, 5]

# Create an instance of BullyAlgorithm with a specific node ID and the list of nodes
bully = BullyAlgorithm(3, nodes)

# Start the election process
bully.startElection()