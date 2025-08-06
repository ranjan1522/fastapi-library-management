def check_book_details(response, expected_payload):
    """
    Verifies that a book with given ID exists in the response and its details match the expected payload.
    """
    books = response.json()
    book_found = False

    for book in books:
        if book["id"] == expected_payload["id"]:
            book_found = True
            expected_title = expected_payload["title"]
            expected_author = expected_payload["author"]
            expected_available = expected_payload.get("available", True)

            assert book["title"] == expected_title, f"Expected title -> '{expected_title}', but got '{book['title']}'"
            assert book["author"] == expected_author, f"Expected author -> '{expected_author}', but got '{book['author']}'"
            assert book["available"] == expected_available, f"Expected available -> '{expected_available}', but got '{book['available']}'"
            break

    assert book_found, f"No book found with ID: {expected_payload['id']}"
