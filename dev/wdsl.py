from requests import Session, utils
from zeep import Client
from zeep.transports import Transport

import logging.config

logging.config.dictConfig({
    'version': 1,
    'formatters': {
        'verbose': {
            'format': '%(name)s: %(message)s'
        }
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose',
        },
    },
    'loggers': {
        'zeep.transports': {
            'level': 'DEBUG',
            'propagate': True,
            'handlers': ['console'],
        },
    }
})

wsdl = "https://demanda.ree.es/WSVisionaBaleares/wsBalearesService?WSDL"

headers = {
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:54.0) Gecko/20100101 Firefox/54.0"
}

session = Session()


transport = Transport(session=session)


client = Client(wsdl=wsdl, transport=transport)

print(client.service.demandaGeneracion30('2017-07-14', '66357', 'BALEARES'))

#66047
#66239
#66291
#66317
#66357
#66431