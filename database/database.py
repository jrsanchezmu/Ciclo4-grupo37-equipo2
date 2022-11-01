from ssl import CertificateError
from pymongo import MongoClient
import json
import certifi

ca = certifi.where()

###########
def loadConfigFile():
    with open('database/config.json') as f:
        data = json.load(f)
    return data

def dbConnection():
    dataConfig: loadConfigFile()
    try: 
        #Conectamos con atlas
        client= MongoClient(dataConfig["MONGO_URI_SERVER"], tlsCAFile=ca)
        #Conexion local
        #client=MongoClient(dataConfig["MONGO_URI_LOCAL"], dataConfig['LOCAL_PORT'])
        db=client["Proyecto_Final_ciclo_4a"]

    except:
        print("Error de conexion en la db")
    return db

