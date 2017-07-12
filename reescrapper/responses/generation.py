from arrow import get


class Generation:

    def __init__(self, timestamp, diesel, gas, wind, combined, vapor, solar, hydraulic):
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
