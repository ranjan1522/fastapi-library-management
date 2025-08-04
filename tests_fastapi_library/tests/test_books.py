import pytest
import json
from api_pages.books_api import Book_Api

@pytest.fixture
def book_api(get_request, post_request, patch_request, delete_request):
    return Book_Api(get_request, post_request, patch_request, delete_request)

def test_get_books(book_api):
    response = book_api.get_books()
    #print(json.dumps(response.json(), indent=2))
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    for book in response.json():
        if book["id"] == 3:
            expected_title = "The Alchemist"
            expected_avaialbilities = True
            assert book["title"] == expected_title, f"Expected->{expected_title} does not match with Actual->{book["title"]}"
            assert book["available"] == expected_avaialbilities, f"Expected->{expected_avaialbilities} does not match with Actual->{book["available"]}"
     
    