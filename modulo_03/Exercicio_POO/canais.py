
class CanalEnvio:
    def enviar(self, mensagem):
        raise NotImplementedError("deve ser subscrito pelas subclasses.")

class Email(CanalEnvio):
    def enviar(self, mensagem):
        print(f"Enviando para servidor de email: {mensagem}")

class SMS(CanalEnvio):
    def enviar(self, mensagem):
        print(f"Enviando para operadora telefônica: {mensagem}")