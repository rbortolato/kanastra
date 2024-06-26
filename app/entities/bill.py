from app.entities.ibill import IBill

class Bill(IBill):
    def __init__(self):
        self.name = ""
        self.governmentId = ""
        self.email = ""
        self.debtAmount = ""
        self.debtDueDate = ""
        self.debtId = ""

    def create(self, row):
        rowList = row.split(',')
        if len(rowList) != 6:
            return

        self.name = rowList[0]
        self.governmentId = rowList[1]
        self.email = rowList[2]
        self.debtAmount = rowList[3]
        self.debtDueDate = rowList[4]
        self.debtId = rowList[5]

        print('Boleto criado para ' + self.name)

    def validate(self):
        return self.name and self.governmentId and self.email and self.debtAmount and self.debtDueDate and self.debtId
