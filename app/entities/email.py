from app.entities.cache import Cache
from app.entities.ibill import IBill

class Email:
    def send(self, bill: IBill):
        cache = Cache()
        if cache.exists(bill.debtId):
            print('Boleto já processado')
        else:
            pass
            cache.add(bill.debtId)
            print('Email enviado para ' + bill.email)
