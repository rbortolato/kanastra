from app.core.sigleton import Singleton

class Cache(Singleton):
    def __init__(self):
        self.cache = {}

    def add(self, debtId):
        self.cache[debtId] = True

    def exists(self, debtId):
        return self.cache.get(debtId)
