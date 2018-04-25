from arrow import get


class Response(object):

    def __init__(self, timestamp, demand=0.0, diesel=0.0, gas=0.0, wind=0.0, combined=0.0, vapor=0.0, solar=0.0, hydraulic=0.0, carbon=0.0, nuclear=0.0, other=0.0):
        self.timestamp = timestamp
        self._demand = demand
        self._nuclear = nuclear
        self._diesel = diesel
        self._gas = gas
        self._wind = wind
        self._combined = combined
        self._vapor = vapor
        self._solar = solar
        self._hydraulic = hydraulic
        self._carbon = carbon
        self._other = other
        self.link = {}

    @property
    def demand(self):
        return round(self._demand, 2)

    @demand.setter
    def demand(self, demand):
        self._demand = demand

    @property
    def nuclear(self):
        return round(self._nuclear, 2)

    @nuclear.setter
    def nuclear(self, nuclear):
        self._nuclear = nuclear

    @property
    def diesel(self):
        return round(self._diesel, 2)

    @diesel.setter
    def diesel(self, diesel):
        self._diesel = diesel

    @property
    def gas(self):
        return round(self._gas, 2)

    @gas.setter
    def gas(self, gas):
        self._gas = gas

    @property
    def wind(self):
        return round(self._wind, 2)

    @wind.setter
    def wind(self, wind):
        self._wind = wind

    @property
    def combined(self):
        return round(self._combined, 2)

    @combined.setter
    def combined(self, combined):
        self._combined = combined

    @property
    def vapor(self):
        return round(self._vapor, 2)

    @vapor.setter
    def vapor(self, vapor):
        self._vapor = vapor

    @property
    def solar(self):
        return round(self._solar, 2)

    @solar.setter
    def solar(self, solar):
        self._solar = solar

    @property
    def hydraulic(self):
        return round(self._hydraulic, 2)

    @hydraulic.setter
    def hydraulic(self, hydraulic):
        self._hydraulic = hydraulic

    @property
    def carbon(self):
        return round(self._carbon, 2)

    @carbon.setter
    def carbon(self, carbon):
        self._carbon = carbon

    @property
    def other(self):
        return round(self._other, 2)

    @other.setter
    def other(self, other):
        self._other = other

    def __str__(self):
        base = "Response {0} Demand {1} Diesel: {2} Gas: {3} Wind: {4} Combined: {5} Vapor: {6} Solar: {7} Hydraulic: {8} Carbon: {9} Nuclear: {10} Other: {11}"
        return base.format(get(self.timestamp),
                           self.demand,
                           self.diesel,
                           self.gas,
                           self.wind,
                           self.combined,
                           self.vapor,
                           self.solar,
                           self.hydraulic,
                           self.carbon,
                           self.nuclear,
                           self.other)

    def __repr__(self):
        return self.__str__()

    def _production(self):
        """Calculate total energy production. Not rounded"""
        return self._nuclear + self._diesel + self._gas + self._wind + self._combined + self._vapor + self._solar + self._hydraulic + self._carbon + self._other

    def production(self):
        """Calculate total energy production."""
        return round(self._production(), 2)

    def _links(self):
        """Calculate total energy production. Not Rounded"""
        total = 0.0
        for value in self.link.values():
            total += value
        return total

    def links(self):
        """Calculate total energy production."""
        return round(self._links(), 2)

    def _unknown(self):
        """Calculate unknown energy production. Not Rounded"""
        return self._demand - (self._production() + self._links())

    def unknown(self):
        """Calculate unknown energy production."""
        return max(0.0, round(self._unknown(), 2))