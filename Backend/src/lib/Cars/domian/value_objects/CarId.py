from uuid import uuid4,UUID

class CarId:
    
    def __init__(self,value:str):
        if value is None:
            self._value = uuid4()
        else:
            self._value = value
