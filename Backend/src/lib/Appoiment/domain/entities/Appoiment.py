from typing import Optional
from ..value_objects.AppoimentId import AppoimentId

class Appoiment:

    def __init__(self,id:Optional[str] = None,id_visitante:Optional[str] = None,car_id:Optional[str] = None,fecha:Optional[str] = None,hora:Optional[str] = None,visitado:Optional[str] = None,area:Optional[str] = None):
        self.id = AppoimentId(id)
        self.id_visitante = id_visitante
        self.car_id = car_id
        self.fecha = fecha
        self.hora = hora
        self.visitado = visitado
        self.area = area



        