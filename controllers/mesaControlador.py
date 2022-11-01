from repositorios.mesaRepositorio import MesasRepositorio
from models.mesas import Mesas

class MesaControlador():

    def __init__(self):
        self.repositorioMesa = MesasRepositorio()


    def index(self):
        return self.repositorioMesa.findAll()
     
    def create(self, infoMesa):
        nuevaMesa= Mesas(infoMesa)
        return self.repositorioMesa.save(nuevaMesa)


    def show(self, id):
        laMesa = Mesas(self.repositorioMesa.findById(id))
        return laMesa.__dict__
    
    def update(self, id, infoMesa):
        mesaActual = Mesas(self.repositorioMesa.findById(id))
        mesaActual.numero = infoMesa["numero"]
        mesaActual.cantidad_inscritos= infoMesa["cantidad_inscritos"]
        return self.repositorioMesa.save(mesaActual)
    
    def delete(self, id):
        return self.repositorioMesa.delete(id)