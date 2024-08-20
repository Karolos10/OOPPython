class Book:
    
    def __init__(self, title, author, price, stock, oid):
        
        self._title = title
        self._author = author
        self._price = price
        self._stock = stock
        self._oid = oid
    
    def getInfo(self):
        return f"""\n Title: {self._title} \n Author: {self._author} \n Price: {self._price} \n Stock: {self._stock} \n ID: {self._oid}"""

class Comic(Book):
    def __init__(self, title, author, price, stock, oid, illustrator, vol):
        super().__init__(title, author, price, stock, oid)
        self._illustrator = illustrator
        self._vol = vol
    
    def getInfo(self):
        str_illustrator = ', '.join(self._illustrator)
        return f"{super().getInfo()} \n Illustrator: {str_illustrator} \n Volume: {self._vol}"
    

book1 = Book('Python Programming', 'John Doe', 29.99, 100, 1)
book2 = Book('Java Programming', 'Jane Doe', 39.99, 50, 2)

print(book1.getInfo())
print(book2.getInfo())

comic1 = Comic('One Piece', 'Eiichiro Oda', 9.99, 1000, 3, 'Eiichiro Oda', 1)
comic2 = Comic('Naruto', 'Masashi Kishimoto', 9.99, 500, 4, ['Masashi Kishimoto', 'Eiichiro Oda'], 1)
print(comic1.getInfo())
print(comic2.getInfo())

