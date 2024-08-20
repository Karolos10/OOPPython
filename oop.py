class Book:
    
    def __init__(self, title, author, price, stock, oid):
        
        self.title = title
        self.author = author
        self.price = price
        self.stock = stock
        self.oid = id
    
    

book1 = Book('Python Programming', 'John Doe', 29.99, 100, 1)
print(book1)

