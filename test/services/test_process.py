
from fastapi import UploadFile
from app.services.process import process_bill

def test_process_bill():
    f = open('test/shared/novo.csv', 'rb')
    file = UploadFile(f)
    response = process_bill(file)
    assert response == {'processed': 2, 'unprocessed_line': ''}
