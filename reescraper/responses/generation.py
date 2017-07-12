from arrow import get


class Generation:

    def __init__(self, timestamp, diesel=0.0, gas=0.0, wind=0.0, combined=0.0, vapor=0.0, solar=0.0, hydraulic=0.0):
        self.timestamp = timestamp
        self.diesel = diesel
        self.gas = gas
        self.wind = wind
        self.combined = combined
        self.vapor = vapor
        self.solar = solar
        self.hydraulic = hydraulic

    def __str__(self):
        base = "Generation {0} Diesel: {1} Gas: {2} Wind: {3} Combined: {4} Vapor: {5} Solar: {6} Hydraulic: {7}"
        return base.format(get(self.timestamp),
                           self.diesel,
                           self.gas,
                           self.wind,
                           self.combined,
                           self.vapor,
                           self.solar,
                           self.hydraulic)
