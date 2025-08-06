import pytest
import json
from api_pages.books_api import Book_Api
from faker import Faker
from commonLib import *

faker = Faker()

@pytest.fixture
def book_api(get_request, post_request, patch_request, delete_request):
    return Book_Api(get_request, post_request, patch_request, delete_request)

payload = {"id": faker.random_int(min=100,max=999), "title": faker.catch_phrase(), "author": faker.name(), "available": True}
update_book_payload = {"title": faker.catch_phrase(), "author": faker.name()}

def test_add_book(book_api):
    try:
        response = book_api.add_book(payload)
        add_book_data = response.json()
        print(f"Response Status Code: {response.status_code} ")
        print("Respose_Data: ",json.dumps(response.json(), indent=2))

        if response.status_code == 200:
            assert add_book_data["message"] == "Book added", (
                f"Expected Value --> 'Book added' but got '{add_book_data.get('message')}'"
            )
        
            # Use reusable check after adding
            get_response = book_api.get_books()
            check_book_details(get_response, payload)
        
        elif response.status_code == 400:
            assert add_book_data["detail"] == "Book with this ID already exists", (
                f"Expected error message but got '{add_book_data.get('detail')}'"
            )
        else:
            pytest.fail(f"Unexpected status code: {response.status_code} with response: {add_book_data}")

    except Exception as e:
        pytest.fail(f"Test failed due to unexpected error: {str(e)}")
    
'''
def test_get_books(book_api):
    try:
        response = book_api.get_books()
        print(f"Response Status Code: {response.status_code} ")
        print("Respose_Data: ",json.dumps(response.json(), indent=2))
        
        assert response.status_code == 200
        assert isinstance(response.json(), list)
        
        for book in response.json(): 
            if book["id"] == payload["id"]:
                expected_title = payload["title"]
                expected_avaialbilities = True
                expected_author = payload['author']
                assert book["title"] == expected_title, f"Expected->{expected_title} does not match with Actual->{book["title"]}"
                assert book["available"] == expected_avaialbilities, f"Expected->{expected_avaialbilities} does not match with Actual->{book["available"]}"
                assert book["author"] == expected_author, f"Expected->{expected_author} does not match with Actual->{book["author"]}" 
    except Exception as e:
        pytest.fail(f"Test failed due to unexpected error: {str(e)}")
'''   

def test_update_book(book_api):
    try:
        response = book_api.update_book(update_book_payload,payload["id"])
        print(f"Response Status Code: {response.status_code} ")
        print("Respose_Data: ",json.dumps(response.json(), indent=2))
        
        assert response.status_code == 200
        assert response.json()["message"] == "Book updated"
        
        # updating the payload after modifcation show that valadion can be perofomed
        updated_payload = {
            "id": payload["id"],
            "title": update_book_payload["title"],
            "author": update_book_payload["author"],
            "available": payload.get("available", True)
        }
        
        # Use reusable check after updating
        get_response = book_api.get_books()
        check_book_details(get_response, updated_payload)    
        
    except Exception as e:
        pytest.fail(f"Test failed due to unexpected error: {str(e)}")
        
def test_delete_added_book(book_api):
    try:
        response = book_api.delete_book(payload["id"])
        print(f"Response Status Code: {response.status_code} ")
        print("Respose_Data: ",json.dumps(response.json(), indent=2))
        deleted_book = response.json()
        assert response.status_code  == 200
        assert deleted_book["message"] == "Book deleted"
        
        #checking the deleted book should not be there in the book list
        get_response = book_api.get_books()
        books = get_response.json()
        book_found = any(book["id"] == payload["id"] for book in books)
        assert not book_found, "Book was not deleted successfully – still found in book list"      
    except Exception as e:
        pytest.fail(f"Test failed due to unexpected error: {str(e)}")
        
        
    