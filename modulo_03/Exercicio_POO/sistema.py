
class SistemaAlerta:
    def __init__(self, usuario, canal):
        self.usuario = usuario
        self.canal = canal

    def disparar(self, texto):
        
        print(f"---- Iniciando alerta para {self.usuario.nome} ----")
        self.canal.enviar(texto)