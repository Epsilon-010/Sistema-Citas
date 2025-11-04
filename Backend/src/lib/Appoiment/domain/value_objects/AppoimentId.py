from uuid import uuid4

class AppoimentId:

    def __init__(self,value):
        if value is None:
            self._value = uuid4()
        else:
            self._value = value
    
    @property
    def value(self):
        return self._value