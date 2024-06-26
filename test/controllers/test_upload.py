
def test_upload(client):
    f = open('test/shared/novo.csv', 'rb')
    response = client.post('/upload', files={"data": f})
    print(response.json())
    assert response.status_code == 200
    assert response.json() == {'processed': 2, 'unprocessed_line': ''}
