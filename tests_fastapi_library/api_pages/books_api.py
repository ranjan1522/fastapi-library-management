class Book_Api:
    def __init__(self, get_request, post_request, patch_request, delete_request):
        self.get= get_request
        self.post = post_request
        self.patch = patch_request
        self.delete = delete_request
    
    def get_books(self):
        return self.get("/books/")
    
    def add_book(self,payload):
        return self.post("/books/", payload)
    
    def update_book(self,update,book_id):
        return self.patch(f"/books/{book_id}", update)
    
    def delete_book(self,book_id):
        return self.delete(f"/books/{book_id}")
    
    