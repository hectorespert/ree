

class Demand:

    def __init__(self, demand,  timestamp):
        self.demand = demand
        self.timestamp = timestamp

    def __str__(self):
        return str(self.timestamp) + " " + str(self.demand)
