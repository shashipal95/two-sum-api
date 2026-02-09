from fastapi.testclient import TestClient
from API import app

client = TestClient(app)


def test_basic_example():
    response = client.post("/two-sum", json={"nums": [2, 7, 11, 15], "target": 9})
    assert response.status_code == 200
    assert response.json() == {"indices": [0, 1]}


def test_example_two():
    response = client.post("/two-sum", json={"nums": [3, 2, 4], "target": 6})
    assert response.status_code == 200
    assert response.json() == {"indices": [1, 2]}


def test_same_number_used_twice():
    response = client.post("/two-sum", json={"nums": [3, 3], "target": 6})
    assert response.status_code == 200
    assert response.json() == {"indices": [0, 1]}


def test_zero_in_array():
    response = client.post("/two-sum", json={"nums": [0, 4, 3, 0], "target": 0})
    assert response.status_code == 200
    assert response.json() == {"indices": [0, 3]}


def test_negative_numbers():
    response = client.post(
        "/two-sum", json={"nums": [-1, -2, -3, -4, -5], "target": -8}
    )
    assert response.status_code == 200
    assert response.json() == {"indices": [2, 4]}


def test_large_numbers():
    response = client.post(
        "/two-sum", json={"nums": [1000000, 500, 200, 1000000], "target": 2000000}
    )
    assert response.status_code == 200
    assert response.json() == {"indices": [0, 3]}


def test_solution_at_end():
    response = client.post(
        "/two-sum", json={"nums": [1, 2, 3, 4, 5, 10, 20], "target": 30}
    )
    assert response.status_code == 200
    assert response.json() == {"indices": [5, 6]}


def test_unsorted_array():
    response = client.post("/two-sum", json={"nums": [1, 5, 2, 9, 3, 4], "target": 14})
    assert response.status_code == 200
    assert response.json() == {"indices": [1, 3]}


def test_no_solution_returns_400():
    response = client.post("/two-sum", json={"nums": [1, 2, 3], "target": 100})
    assert response.status_code == 400
    assert response.json()["detail"] == "No valid pair found"


def test_invalid_payload_missing_field():
    response = client.post("/two-sum", json={"nums": [1, 2, 3]})
    assert response.status_code == 422


def test_invalid_payload_wrong_type():
    response = client.post("/two-sum", json={"nums": "not-a-list", "target": 9})
    assert response.status_code == 422
