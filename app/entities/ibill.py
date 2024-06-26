import abc

class IBill:
    name: str
    governmentId: int
    email = str
    debtAmount = float
    debtDueDate = str
    debtId = str

    @abc.abstractmethod
    def validate(self):
        pass
