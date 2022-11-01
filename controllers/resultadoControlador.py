from models.mesas import Mesas
from models.resultados import Resultado
from models.candidatos import Candidatos

from repositorios.mesaRepositorio import MesasRepositorio
from repositorios.resultadosRepositorio import ResultadosRepositorio
from repositorios.candidatoRepositorio import CandidatosRepositorio

class ResultadoControlador():

    def __init__(self):
        self.repositorioResultado = ResultadosRepositorio()
        self.repositorioCandidato = CandidatosRepositorio()
        self.repositorioMesa = MesasRepositorio()

    def index(self):
        return self.repositoroResultado.findAll()

    def create(self, infoResultado, id_mesa, id_candidato):
        nuevoResultado= Resultado(infoResultado)
        laMesa = Mesas(self.repositorioMesa.findById(id_mesa))
        elCandidato = Candidatos(self.repositorioCandidato.findById(id_candidato))
        nuevoResultado.mesa = laMesa
        nuevoResultado.candidato =elCandidato
        return self.repositoroResultado.save(nuevoResultado)
    
    def show(self, id):
        elResultado = Resultado(self.repositoroResultado.findById(id))
        return elResultado.__dict__
    
    def update(self, id, infoResultado, id_mesa, id_candidato):
        nuevoResultado= Resultado(infoResultado)
        laMesa = Mesas(self.repositorioMesa.findById(id_mesa))
        elCandidato = Candidatos(self.repositorioCandidato.findById(id_candidato))
        nuevoResultado.mesa = laMesa
        nuevoResultado.candidato =elCandidato
        return self.repositorioResultado.save(nuevoResultado)
    
    def delete(self, id):
        return self.repositorioResultado.delete(id)
    
    def getListarCandidatosMesa(self, id_mesa):
        return self.repositorioResultado.getListadoCandidatosInscritosMesa(id_mesa)
    
    def getListarMesasDeInscritoCandidato(self, id_candidato):
        return self.repositorioResultado.getListadoMesasCandidatoInscrito(id_candidato)
    
    def getMayorCedula(self):
        return self.repositorioResultado.getNumeroCedulaMayorCandidato()