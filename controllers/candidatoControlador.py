from repositorios.candidatoRepositorio import CandidatosRepositorio
from repositorios.partidoRepositorio import PartidoRepositorio
from models.candidatos import Candidatos
from models.partido import Partido

class CandidatoControlador():
    def __init__(self):
        self.repositorioCandidato = CandidatosRepositorio()
        self.repositorioPartido = PartidoRepositorio()

    def index(self):
        return self.repositorioCandidato.findAll()
    
    def create(self, infoCandidato):
        nuevoCandidato = Candidatos(infoCandidato)
        return self.repositorioCandidato.save(nuevoCandidato)
    
    def show(self, id):
        elCandidato = Candidatos(self.repositorioCandidato.findAll(id))
        return elCandidato.__dict__
    
    def update(self, id, infoCandidato):
        candidatoActual = Candidatos(self.repositorioCandidato.findById(id))
        candidatoActual.cedula = infoCandidato["cedula"]
        candidatoActual.nombre = infoCandidato["nombre"]
        candidatoActual.apellido = infoCandidato["apellido"]
        return self.repositorioCandidato.save(candidatoActual)


    def delete(self, id):
        return self.repositorioCandidato.celete(id)
    
    def asignarCandidato(self, id, id_partido):
        candidatoActual = Candidatos(self.repositorioCandidato.findById(id))
        partidoActual = Partido(self.repositorioPartido.findById(id_partido))
        candidatoActual.partido = partidoActual
        return self.repositorioCandidato.save(candidatoActual)