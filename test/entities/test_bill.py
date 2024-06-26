from app.entities.bill import Bill

def test_validate_true():
    bill = Bill()
    row = 'Elijah Santos,9558,janet95@example.com,7811,2024-01-19,ea23f2ca-663a-4266-a742-9da4c9f4fcb3'
    bill.create(row)
    assert bill.validate()

def test_validate_false():
    bill = Bill()
    row = '9558,janet95@example.com,7811,2024-01-19,ea23f2ca-663a-4266-a742-9da4c9f4fcb3'
    bill.create(row)
    assert not bill.validate()
