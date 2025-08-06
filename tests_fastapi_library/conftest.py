import pytest
import requests

API_BASE_URL = "https://fastapi-library-management-ht5m.onrender.com"

@pytest.fixture(scope="module")
def api_url():
    return API_BASE_URL

@pytest.fixture
def headers():
    return {"Content-Type": "application/json"}

@pytest.fixture
def get_request(api_url, headers):
    def _get(endpoint: str):
        url = f"{api_url}{endpoint}"
        print(f"Request_URL: {url}, Request_Headers: {headers}")
        return requests.get(url, headers=headers)
    return _get

@pytest.fixture
def post_request(api_url, headers):
    def _post(endpoint: str, payload: dict):
        url = f"{api_url}{endpoint}"
        print(f"Request_URL: {url}, Request_Headers: {headers}, Request_Payload: {payload}")
        return requests.post(url, json=payload, headers=headers)
    return _post

@pytest.fixture
def patch_request(api_url, headers):
    def _patch(endpoint: str, payload: dict):
        url = f"{api_url}{endpoint}"
        print(f"Request_URL: {url}, Request_Headers: {headers}, Request_Payload: {payload}")
        return requests.patch(url, json=payload, headers=headers)
    return _patch

@pytest.fixture
def delete_request(api_url, headers):
    def _delete(endpoint: str):
        url = f"{api_url}{endpoint}"
        return requests.delete(url, headers=headers)
    return _delete
