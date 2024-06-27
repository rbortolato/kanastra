from app.entities.bill import Bill
from app.entities.email import Email

def process_bill(file):
    error = []
    success = 0
    first_row = True
    email = Email()

    with file.file as csv_file:
        for i, row_csv in enumerate(csv_file):
            if first_row:
                first_row = False
                continue
            row = row_csv.decode('utf-8').replace('\r', '').replace('\n', '')

            try:
                bill = Bill()
                bill.create(row)
                if not bill.validate():
                    error.append(str(i))
                    continue

                email.send(bill)
                success += 1
            except Exception as e:
                print(str(e))
                error.append(str(i))
                continue

    assert (len(error) > 0 or success > 0), "Arquivo está vazio"

    return {"processed": success, "unprocessed_line": ', '.join(error)}
