from arrow import get


class Demand:

    def __init__(self, demand,  timestamp):
        self.demand = demand
        self.timestamp = timestamp

    def __str__(self):
        base = "Demand {0} {1} "
        return base.format(get(self.timestamp), self.demand)
