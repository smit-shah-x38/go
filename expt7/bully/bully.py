import random
import time

class Process:
    def __init__(self, id, alive=True):
        self.id = id
        self.alive = alive

class Network:
    def __init__(self, processes):
        self.processes = processes

    def elect_leader(self, initiator_id):
        print(f"Process {initiator_id} initiating election.")

        # Send election message to higher ID processes
        for process in self.processes:
            if process.id > initiator_id and process.alive:
                print(f"Process {initiator_id} sending election message to {process.id}.")
                # Simulate sending message (replace with actual network communication)
                time.sleep(random.uniform(0.1, 0.5))  # Random delay

                # If no response within timeout, assume higher ID process is down
                if not process.alive:
                    print(f"Process {process.id} did not respond. Assuming it's down.")

        # If no higher ID process responds, declare itself leader
        print(f"Process {initiator_id} declares itself as leader.")

# Create a network with some processes
processes = [
    Process(1),
    Process(2),
    Process(3, alive=False),  # Simulate a failed process
    Process(4),
]
network = Network(processes)

# Simulate an election initiated by process 2
network.elect_leader(2)