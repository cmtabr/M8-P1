import re, os, time

class Bot:
    def __init__(self):
        self._intents = {
            r'\b(Como posso atualizar meu cartão de crédito| Preciso mudar a forma de pagamento, o que fazer| Quero atualizar minhas informações de pagamento| Método de pagamento desatualizado, como proceder para atualizar)\b': "card_update",
            r'\b(Onde vejo o status do meu pedido | Como faço para rastrear meu pedido | Quero saber onde está meu pedido, como faço| "Status de entrega, como consultar)\b' : 'orders',
            r'\b(?:ola|oi|hi)\b': 'greetings'
        }
        self._actions = {
            "card_update": self.card_update,
            "orders": self.order_info,
            "greetings": self.greetings
        }
    
    def card_update(self, message):
        return print(f'Você pode atualizar seu cartão de crédito na seção Perfil>Cartões>Atualizar')
    
    def order_info(self, message):
        return print(f'Você pode verificar mais informações sobre seu pedido na seção Perfil>Meus pedidos')

    def greetings(self, message):
        return print(f'Olá, tudo bem?')

    def action(self, message):
        for key, value in self._intents.items():
            pattern = re.compile(key, re.IGNORECASE)
            groups = pattern.findall(message)
            if groups:
                print(f"{self._actions[value](groups[0])}", end=" ")
            else:
                print(f'Não entendi o que você falou "{message}"')

    def get_message(self):
        while True:
            message = input("Em que posso ser útil? ")
            if message == 'sair':
                break
            self.action(message)
            time.sleep(3)
            os.system('cls')

def main():
    teste = Bot()
    teste.get_message()

if __name__ == '__main__':
    main()