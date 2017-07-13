from .canary import ElHierro, Fuerteventura, GranCanaria, Gomera, Lanzarote, LaPalma, Tenerife
from .core import Scraper, NoDataException, TimestampException
from .response import Response


class CanaryIslands(Scraper):

    def __init__(self, session=None):
        super(self.__class__, self).__init__(session)
        self.__responses = []

    def get(self):
        self.__responses = []
        self.__fuerteventura()
        self.__gomera()
        self.__grancanaria()
        self.__hierro()
        self.__lanzarote()
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
        demand = 0.0
        for gen in self.__responses:
            demand += gen.demand
        return round(demand, 2)

    def __diesel(self):
        diesel = 0.0
        for gen in self.__responses:
            diesel += gen.diesel
        return round(diesel, 2)

    def __gas(self):
        gas = 0.0
        for gen in self.__responses:
            gas += gen.gas
        return round(gas, 2)

    def __wind(self):
        wind = 0.0
        for gen in self.__responses:
            wind += gen.wind
        return round(wind, 2)

    def __combined(self):
        combined = 0.0
        for gen in self.__responses:
            combined += gen.combined
        return round(combined, 2)

    def __vapor(self):
        vapor = 0.0
        for gen in self.__responses:
            vapor += gen.vapor
        return round(vapor, 2)

    def __solar(self):
        solar = 0.0
        for gen in self.__responses:
            solar += gen.solar
        return round(solar, 2)

    def __hydraulic(self):
        hydraulic = 0.0
        for gen in self.__responses:
            hydraulic += gen.hydraulic
        return round(hydraulic, 2)

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

    def __fuerteventura(self):
        fuerteventura = Fuerteventura(self.session).get()
        if not fuerteventura:
            raise NoDataException
        else:
            self.__responses.append(fuerteventura)

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

    def __lanzarote(self):
        lanzarote = Lanzarote(self.session).get()
        if not lanzarote:
            raise NoDataException
        else:
            self.__responses.append(lanzarote)

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
