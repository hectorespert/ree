from arrow import get


class Response:

    def __init__(self, timestamp, demand=0.0, diesel=0.0, gas=0.0, wind=0.0, combined=0.0, vapor=0.0, solar=0.0, hydraulic=0.0, carbon=0.0):
        self.timestamp = timestamp
        self.demand = demand
        self.diesel = diesel
        self.gas = gas
        self.wind = wind
        self.combined = combined
        self.vapor = vapor
        self.solar = solar
        self.hydraulic = hydraulic
        self.carbon = carbon
        self.link = {}

    def __str__(self):
        base = "Response {0} Demand {1} Diesel: {2} Gas: {3} Wind: {4} Combined: {5} Vapor: {6} Solar: {7} Hydraulic: {8} Carbon: {9}"
        return base.format(get(self.timestamp),
                           self.demand,
                           self.diesel,
                           self.gas,
                           self.wind,
                           self.combined,
                           self.vapor,
                           self.solar,
                           self.hydraulic,
                           self.carbon)

    def production(self):
        """Calculate total energy production."""
        return round(self.diesel + self.gas + self.wind + self.combined + self.vapor + self.solar + self.hydraulic + self.carbon, 2)

    def links(self):
        """Calculate total energy production."""
        total = 0.0
        for value in self.link.values():
            total += value
        return round(total, 2)

    def unknown(self):
        """Calculate unknown energy production."""
        return max(0.0, round(self.demand - (self.production() + self.links()), 2))
