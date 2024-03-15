import random
import time

class Process:
    def __init__(self, id, alive=True):
        self.id = id
        self.alive = alive
        self.has_token = False

class Network:
    def __init__(self, processes):
        self.processes = processes
        self.ring_order = self.create_ring()  # Create a ring structure
        self.leader_id = None

    def create_ring(self):
        # Create a circular linked list-like structure
        for i in range(len(self.processes)):
            self.processes[i].next = self.processes[(i + 1) % len(self.processes)]
        return self.processes[0]  # Return the first process in the ring

    def start_election(self, initiator_id):
        print(f"Process {initiator_id} initiating election.")
        initiator = next(p for p in self.processes if p.id == initiator_id)
        initiator.has_token = True

        # Initialize leader_id with the initiator's ID
        self.leader_id = initiator.id  # <-- This line is added

        self.pass_token(initiator)
        
    def pass_token(self, current_process):
        while True:
            next_process = current_process.next

            # Simulate token passing (replace with actual network communication)
            print(f"Process {current_process.id} passing token to {next_process.id}.")
            time.sleep(random.uniform(0.1, 0.5))  # Random delay

            if next_process.alive:
                next_process.has_token = True
                current_process.has_token = False

                if next_process.id > self.leader_id:
                    self.leader_id = next_process.id
                    print(f"Process {next_process.id} becomes the new leader.")

                if next_process.id == self.ring_order.id:
                    # Token has completed a full circle, election is done
                    print("Election complete.")
                    break

                current_process = next_process
            else:
                print(f"Process {next_process.id} is down. Removing from ring.")
                current_process.next = next_process.next  # Bypass the failed process

# Create a network with some processes
processes = [
    Process(1),
    Process(2),
    Process(3, alive=False),  # Simulate a failed process
    Process(4),
]
network = Network(processes)

# Simulate an election initiated by process 1
network.start_election(1)