from arrow import get


class Response:

    def __init__(self, timestamp, demand=None, diesel=None, gas=None, wind=None, combined=None, vapor=None, solar=None, hydraulic=None):
        self.timestamp = timestamp
        self.demand = demand
        self.diesel = diesel
        self.gas = gas
        self.wind = wind
        self.combined = combined
        self.vapor = vapor
        self.solar = solar
        self.hydraulic = hydraulic

    def __str__(self):
        base = "Response {0} Demand {1} Diesel: {2} Gas: {3} Wind: {4} Combined: {5} Vapor: {6} Solar: {7} Hydraulic: {8}"
        return base.format(get(self.timestamp),
                           self.demand,
                           self.diesel,
                           self.gas,
                           self.wind,
                           self.combined,
                           self.vapor,
                           self.solar,
                           self.hydraulic)
