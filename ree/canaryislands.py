from typing import Optional
from .canary import (
    ElHierro,
    GranCanaria,
    Gomera,
    LanzaroteFuerteventura,
    LaPalma,
    Tenerife,
)
from .core import Scraper, NoDataException, TimestampException
from .response import Response


class CanaryIslands(Scraper):
    def __init__(self, session=None, verify=True):
        super(self.__class__, self).__init__(session, verify)
        self.__responses = []

    def get(self):
        self.__responses = []
        self.__gomera()
        self.__grancanaria()
        self.__hierro()
        self.__lanzarotefuerteventura()
        self.__palma()
        self.__tenerife()
        self.__checkgenerations()
        return self.__response()

    def __response(self):
        timestamp = self.__timestamp()
        response = Response(timestamp)
        response.demand = self.__demand()
        response.diesel = self.__diesel()
        response.gas = self.__gas()
        response.wind = self.__wind()
        response.combined = self.__combined()
        response.vapor = self.__vapor()
        response.solar = self.__solar()
        response.hydraulic = self.__hydraulic()
        return response

    def __demand(self):
        demand: Optional[float] = None
        for gen in self.__responses:
            if demand is None:
                demand = gen._demand
            else:
                demand += gen._demand if gen._demand else 0.0
        return demand

    def __diesel(self):
        diesel: Optional[float] = None
        for gen in self.__responses:
            if diesel is None:
                diesel = gen._diesel
            else:
                diesel += gen._diesel if gen._diesel else 0.0
        return diesel

    def __gas(self):
        gas: Optional[float] = None
        for gen in self.__responses:
            if gas is None:
                gas = gen._gas
            else:
                gas += gen._gas if gen._gas else 0.0
        return gas

    def __wind(self):
        wind: Optional[float] = None
        for gen in self.__responses:
            if wind is None:
                wind = gen._wind
            else:
                wind += gen._wind if gen._wind else 0.0
        return wind

    def __combined(self):
        combined: Optional[float] = None
        for gen in self.__responses:
            if combined is None:
                combined = gen._combined
            else:
                combined += gen._combined if gen._combined else 0.0
        return combined

    def __vapor(self):
        vapor: Optional[float] = None
        for gen in self.__responses:
            if vapor is None:
                vapor = gen._vapor
            else:
                vapor += gen._vapor if gen._vapor else 0.0
        return vapor

    def __solar(self):
        solar: Optional[float] = None
        for gen in self.__responses:
            if solar is None:
                solar = gen._solar
            else:
                solar += gen._solar if gen._solar else 0.0
        return solar

    def __hydraulic(self):
        hydraulic: Optional[float] = None
        for gen in self.__responses:
            if hydraulic is None:
                hydraulic = gen._hydraulic
            else:
                hydraulic += gen._hydraulic if gen._hydraulic else 0.0
        return hydraulic

    def __timestamp(self):
        generation = self.__responses[0]
        timestamp = generation.timestamp
        if not timestamp:
            raise TimestampException
        else:
            return timestamp

    def __checkgenerations(self):
        timestamp = self.__timestamp()
        for gen in self.__responses:
            if gen.timestamp != timestamp:
                raise TimestampException

    def __gomera(self):
        gomera = Gomera(self.session).get()
        if not gomera:
            raise NoDataException
        else:
            self.__responses.append(gomera)

    def __grancanaria(self):
        granacanaria = GranCanaria(self.session).get()
        if not granacanaria:
            raise NoDataException
        else:
            self.__responses.append(granacanaria)

    def __hierro(self):
        hierro = ElHierro(self.session).get()
        if not hierro:
            raise NoDataException
        else:
            self.__responses.append(hierro)

    def __lanzarotefuerteventura(self):
        lanzarotefuerteventura = LanzaroteFuerteventura(self.session).get()
        if not lanzarotefuerteventura:
            raise NoDataException
        else:
            self.__responses.append(lanzarotefuerteventura)

    def __palma(self):
        palma = LaPalma(self.session).get()
        if not palma:
            raise NoDataException
        else:
            self.__responses.append(palma)

    def __tenerife(self):
        tenerife = Tenerife(self.session).get()
        if not tenerife:
            raise NoDataException
        else:
            self.__responses.append(tenerife)
