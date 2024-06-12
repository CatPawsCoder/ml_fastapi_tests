from fastapi.testclient import TestClient
from main import app  # Убедитесь, что импортируете правильный модуль

client = TestClient(app)

def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}

def test_predict_positive():
    response = client.post("/predict/", json={"text": "I like machine learning!"})
    json_data = response.json()
    assert response.status_code == 200
    assert json_data['label'] == 'POSITIVE'

def test_predict_negative():
    response = client.post("/predict/", json={"text": "I hate machine learning!"})
    json_data = response.json()
    assert response.status_code == 200
    assert json_data['label'] == 'NEGATIVE'

def test_model_info():
    response = client.get("/model_info/")
    assert response.status_code == 200
    assert response.json() == {
        "model": "distilbert-base-uncased-finetuned-sst-2-english",
        "task": "sentiment-analysis"
    }
