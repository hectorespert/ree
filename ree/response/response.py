from datetime import datetime, timezone
from typing import Optional

from arrow import get


class Response(object):
    def __init__(
        self,
        timestamp,
        demand: Optional[float] = None,
        diesel: Optional[float] = None,
        gas: Optional[float] = None,
        wind: Optional[float] = None,
        combined: Optional[float] = None,
        vapor: Optional[float] = None,
        solar: Optional[float] = None,
        hydraulic: Optional[float] = None,
        carbon: Optional[float] = None,
        nuclear: Optional[float] = None,
        waste: Optional[float] = None,
        other: Optional[float] = None,
    ):
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
        self._waste = waste
        self.link = {}

    @property
    def demand(self):
        return round(self._demand, 2) if self._demand is not None else None

    @demand.setter
    def demand(self, demand: Optional[float]):
        self._demand = demand

    @property
    def nuclear(self):
        return round(self._nuclear, 2) if self._nuclear is not None else None

    @nuclear.setter
    def nuclear(self, nuclear: Optional[float]):
        self._nuclear = nuclear

    @property
    def diesel(self):
        return round(self._diesel, 2) if self._diesel is not None else None

    @diesel.setter
    def diesel(self, diesel: Optional[float]):
        self._diesel = diesel

    @property
    def gas(self):
        return round(self._gas, 2) if self._gas is not None else None

    @gas.setter
    def gas(self, gas: Optional[float]):
        self._gas = gas

    @property
    def wind(self):
        return round(self._wind, 2) if self._wind is not None else None

    @wind.setter
    def wind(self, wind: Optional[float]):
        self._wind = wind

    @property
    def combined(self):
        return round(self._combined, 2) if self._combined is not None else None

    @combined.setter
    def combined(self, combined: Optional[float]):
        self._combined = combined

    @property
    def vapor(self):
        return round(self._vapor, 2) if self._vapor is not None else None

    @vapor.setter
    def vapor(self, vapor: Optional[float]):
        self._vapor = vapor

    @property
    def solar(self):
        return round(self._solar, 2) if self._solar is not None else None

    @solar.setter
    def solar(self, solar: Optional[float]):
        self._solar = solar

    @property
    def hydraulic(self):
        return round(self._hydraulic, 2) if self._hydraulic is not None else None

    @hydraulic.setter
    def hydraulic(self, hydraulic: Optional[float]):
        self._hydraulic = hydraulic

    @property
    def carbon(self):
        return round(self._carbon, 2) if self._carbon is not None else None

    @carbon.setter
    def carbon(self, carbon: Optional[float]):
        self._carbon = carbon

    @property
    def waste(self):
        return round(self._waste, 2) if self._waste is not None else None

    @waste.setter
    def waste(self, waste: Optional[float]):
        self._waste = waste

    @property
    def other(self):
        return round(self._other, 2) if self._other is not None else None

    @other.setter
    def other(self, other: Optional[float]):
        self._other = other

    def __str__(self):
        return f"Response {get(self.timestamp)} Demand {self.demand} Diesel: {self.diesel} Gas: {self.gas} Wind: {self.wind} Combined: {self.combined} Vapor: {self.vapor} Solar: {self.solar} Hydraulic: {self.hydraulic} Carbon: {self.carbon} Nuclear: {self.nuclear} Waste: {self.waste} Other: {self.other}"

    def to_dict(self):
        return {
            "timestamp": self.timestamp,
            "datetime": datetime.fromtimestamp(self.timestamp)
            .astimezone(timezone.utc)
            .isoformat(),
            "demand": self._demand,
            "diesel": self._diesel,
            "gas": self._gas,
            "wind": self._wind,
            "combined": self._combined,
            "vapor": self._vapor,
            "solar": self._solar,
            "hydraulic": self._hydraulic,
            "carbon": self._carbon,
            "nuclear": self._nuclear,
            "waste": self._waste,
            "other": self._other,
        }

    def __repr__(self):
        return self.__str__()

    def _production(self):
        """Calculate total energy production. Not rounded"""
        return sum(
            getattr(self, attr) if getattr(self, attr) else 0
            for attr in [
                "_nuclear",
                "_diesel",
                "_gas",
                "_wind",
                "_combined",
                "_vapor",
                "_solar",
                "_hydraulic",
                "_carbon",
                "_waste",
                "_other",
            ]
        )

    def production(self):
        """Calculate total energy production."""
        return round(self._production(), 2)

    def _links(self):
        """Calculate total energy production. Not Rounded"""
        total = 0.0
        for value in self.link.values():
            total += value if value else 0.0
        return total

    def links(self):
        """Calculate total energy production."""
        return round(self._links(), 2)

    def _unknown(self):
        """Calculate unknown energy production. Not Rounded"""
        if self._demand and self._production() and self._links():
            return self._demand - (self._production() + self._links())
        else:
            raise ValueError("Demand, production or links not defined")

    def unknown(self):
        """Calculate unknown energy production."""
        if self._unknown():
            return max(0.0, round(self._unknown(), 2))
