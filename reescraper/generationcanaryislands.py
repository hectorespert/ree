from .core import Scraper
from .response import Response
from .fuerteventura import Fuerteventura
from .generationgomera import GenerationGomera
from .generationgrancanaria import GenerationGranCanaria
from .elhierro import ElHierro
from .generationlanzarote import GenerationLanzarote
from .generationpalma import GenerationPalma
from .tenerife import Tenerife


class NoDataException(Exception):
    pass


class TimestampException(Exception):
    pass


class GenerationCanaryIslands(Scraper):

    def __init__(self):
        super().__init__()
        self.__generations = []

    def get(self):
        self.__fuerteventura()
        self.__gomera()
        self.__grancanaria()
        self.__hierro()
        self.__lanzarote()
        self.__palma()
        self.__tenerife()
        self.__checkgenerations()
        return self.__generation()

    def __generation(self):
        timestamp = self.__timestamp()
        generation = Response(timestamp)
        generation.diesel = self.__diesel()
        generation.gas = self.__gas()
        generation.wind = self.__wind()
        generation.combined = self.__combined()
        generation.vapor = self.__vapor()
        generation.solar = self.__solar()
        generation.hydraulic = self.__hydraulic()
        return generation

    def __diesel(self):
        diesel = 0.0
        for gen in self.__generations:
            diesel += gen.diesel
        return round(diesel, 2)

    def __gas(self):
        gas = 0.0
        for gen in self.__generations:
            gas += gen.gas
        return round(gas, 2)

    def __wind(self):
        wind = 0.0
        for gen in self.__generations:
            wind += gen.wind
        return round(wind, 2)

    def __combined(self):
        combined = 0.0
        for gen in self.__generations:
            combined += gen.combined
        return round(combined, 2)

    def __vapor(self):
        vapor = 0.0
        for gen in self.__generations:
            vapor += gen.vapor
        return round(vapor, 2)

    def __solar(self):
        solar = 0.0
        for gen in self.__generations:
            solar += gen.solar
        return round(solar, 2)

    def __hydraulic(self):
        hydraulic = 0.0
        for gen in self.__generations:
            hydraulic += gen.hydraulic
        return round(hydraulic, 2)

    def __timestamp(self):
        generation = self.__generations[0]
        timestamp = generation.timestamp
        if not timestamp:
            raise TimestampException
        else:
            return timestamp

    def __checkgenerations(self):
        timestamp = self.__timestamp()
        for gen in self.__generations:
            if gen.timestamp != timestamp:
                raise TimestampException

    def __fuerteventura(self):
        fuerteventura = Fuerteventura(self.driver).get()
        if not fuerteventura:
            raise NoDataException
        else:
            self.__generations.append(fuerteventura)

    def __gomera(self):
        gomera = GenerationGomera(self.driver).get()
        if not gomera:
            raise NoDataException
        else:
            self.__generations.append(gomera)

    def __grancanaria(self):
        granacanaria = GenerationGranCanaria(self.driver).get()
        if not granacanaria:
            raise NoDataException
        else:
            self.__generations.append(granacanaria)

    def __hierro(self):
        hierro = ElHierro(self.driver).get()
        if not hierro:
            raise NoDataException
        else:
            self.__generations.append(hierro)

    def __lanzarote(self):
        lanzarote = GenerationLanzarote(self.driver).get()
        if not lanzarote:
            raise NoDataException
        else:
            self.__generations.append(lanzarote)

    def __palma(self):
        palma = GenerationPalma(self.driver).get()
        if not palma:
            raise NoDataException
        else:
            self.__generations.append(palma)

    def __tenerife(self):
        tenerife = Tenerife(self.driver).get()
        if not tenerife:
            raise NoDataException
        else:
            self.__generations.append(tenerife)
