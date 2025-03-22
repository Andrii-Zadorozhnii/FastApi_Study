from fastapi import FastAPI, HTTPException
import uvicorn
from pydantic import BaseModel

app = FastAPI()

books = [
    {
      "id": 1,
      "title": "1984",
      "author": "George Orwell"
    },
    {
      "id": 2,
      "title": "To Kill a Mockingbird",
      "author": "Harper Lee"
    },
    {
      "id": 3,
      "title": "The Great Gatsby",
      "author": "F. Scott Fitzgerald"
    },
    {
      "id": 4,
      "title": "Moby-Dick",
      "author": "Herman Melville"
    },
    {
      "id": 5,
      "title": "Pride and Prejudice",
      "author": "Jane Austen"
    }
  ]


@app.get("/books",
         tags=["Books 📚"],
         summary='Receive all books')
def read_books():
    return books



@app.get("/books/{book_id}",
         tags=['Books 📚'],
         summary='Receive a book by id')
def get_book(book_id: int):
    for book in books:
        if book['id'] == book_id:
            return book
    raise HTTPException(status_code=404, detail="Книга не найдена")



class NewBook(BaseModel):
    title: str
    author: str


@app.post('/books',
          tags=["Books 📚"])
def create_book(new_book: NewBook):
    books.append({
        "id": len(books) + 1,
        "title": new_book.title,
        "author": new_book.author.title()
    })
    return{"success":"True",
           "message": "Book added"}










if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)