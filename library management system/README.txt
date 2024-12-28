Library Management System API

Description:
This is a Flask-based Library Management System API designed to manage books and members in a library. The API supports CRUD operations for both books and members, along with basic authentication and pagination features.

Features:
- Add, update, and delete books and members.
- View a list of books and members with pagination support.
- Search books by title or author.
- Authentication via a static token for secure access to the API endpoints.
- In-memory data storage (for development or testing purposes).

API Endpoints:

1. **Books Endpoints**:
   - `GET /books`: Retrieves a paginated list of books, with optional filtering by title and author.
   - `POST /books`: Adds a new book to the library.
   - `GET /books/<book_id>`: Retrieves a specific book by its ID.
   - `PUT /books/<book_id>`: Updates a specific book by its ID.
   - `DELETE /books/<book_id>`: Deletes a specific book by its ID.

2. **Members Endpoints**:
   - `GET /members`: Retrieves a paginated list of members.
   - `POST /members`: Adds a new member to the library.
   - `GET /members/<member_id>`: Retrieves a specific member by their ID.
   - `PUT /members/<member_id>`: Updates a specific member's information.
   - `DELETE /members/<member_id>`: Deletes a specific member.

Authentication:
- To access any endpoint, the `Authorization` header must include the token `secure_token`.

Usage:
1. Clone the repository.
2. Install required dependencies: `pip install -r requirements.txt`.
3. Run the application: `python app.py`.
4. Use tools like Postman or curl to interact with the API.

Example:
To add a book, send a POST request to `/books` with a JSON body like:
{
  "title": "The Great Gatsby",
  "author": "F. Scott Fitzgerald",
  "published_year": 1925
}

Dependencies:
- Flask
