from datetime import datetime

class ValidadorFecha:
    def __init__(self, formato='%d-%m-%Y'):
        self.formato = formato

    def es_fecha_valida(self,fecha):
        try:
            datetime.strptime(fecha, self.formato)
            return True
        except ValueError:
            return False