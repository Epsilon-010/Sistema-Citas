from uuid import uuid4, UUID

class UserId:
    def __init__(self, value=None):
        if value is None:
            self._value = uuid4()
        else:
            
            if isinstance(value, UUID):
                self._value = value
            else:
                try:
                    self._value = UUID(value)
                except (ValueError, AttributeError):
                    raise ValueError("ID invalido")
    
    @property
    def value(self):
        return str(self._value)

    


