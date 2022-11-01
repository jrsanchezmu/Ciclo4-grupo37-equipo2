from repositorios.interfazRepositorio import InterfazRepositorio
from models.resultados import Resultado
from bson import ObjectId

class ResultadosRepositorio(InterfazRepositorio[Resultado]):

    #Devuelve los candidatos votados en la mesa
    def getListadoCandidatosInscritosMesa(self, id_mesa):
        theQuery = {"mesa.$id": ObjectId(id_mesa)}
        return self.query(theQuery)
    
    #Funcion que revisa el candidato votado en cada mesa
    def getListadoMesasCandidatoInscrito(self, id_candidato):
        theQuery = {"candidato.$id": ObjectId(id_candidato)}
        return self.query(theQuery)
    
    #Devuelve la cedula más grande o sea la cedula  mas nueva
    def getNumeroCedulaMayorCandidato(self):
        query1 = {
            "$gruop":{
                "_id":"$candidato",
                "max" :{
                    "$max":"$cedula"
                },
                "doc":{"$first":"$$ROOT"}
            }
        }
        pipeline = [query1]
        return self.queryAggregation(pipeline)
