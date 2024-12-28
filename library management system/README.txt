Library Management System API

Description:
This is a RESTful API built using Flask for managing books and library members. It allows for basic CRUD (Create, Read, Update, Delete) operations on books and members, with pagination and search capabilities. The API also includes authentication via a static token to secure access to the endpoints.

How to Run the Project:
1. Clone the repository to your local machine:
   git clone <repository_url>

2. Install the required dependencies using pip:
   pip install -r requirements.txt

3. Run the Flask application:
   python app.py

4. By default, the application will run on `http://127.0.0.1:5000/`.

5. Use tools like Postman or curl to test the API. Ensure to include the `Authorization` header with the value `secure_token` for authentication.

Example API Requests:
- To add a new book, send a POST request to `/books` with a JSON body:
  {
    "title": "The Great Gatsby",
    "author": "F. Scott Fitzgerald",
    "published_year": 1925
  }

- To get the list of books with pagination, send a GET request to `/books`:
  http://127.0.0.1:5000/books?page=1&per_page=5

Design Choices:
1. Flask Framework: Flask was chosen for its simplicity and flexibility in building lightweight APIs. It is easy to scale and perfect for small to medium-sized applications like this one.

2. In-Memory Data Storage: For simplicity and to focus on the API design, the data is stored in-memory (using Python lists). In a real-world scenario, this would be replaced with a persistent database such as SQLite or PostgreSQL.

3. Authentication: A static token-based authentication mechanism is used (`Authorization` header with the value `secure_token`). This approach ensures that only authorized users can access the API endpoints. In a production environment, a more secure mechanism like JWT (JSON Web Tokens) could be used.

4. Pagination: Pagination is implemented for the `/books` and `/members` endpoints to improve performance and user experience when dealing with large data sets. It allows clients to request a specific number of results per page.

5. Search Feature: The `/books` endpoint supports basic filtering by title and author using query parameters (`title`, `author`). This enables users to quickly find books that match their interests.

6. CRUD Operations: The API supports full CRUD operations for both books and members. Each entity (book or member) has a unique ID that is automatically generated upon creation.

Assumptions or Limitations:
1. In-Memory Data: Data is stored in memory and will be lost when the server is restarted. This is only suitable for testing or development purposes. In production, a database should be used to persist data.

2. Authentication: The authentication token is hardcoded and static (`secure_token`). For real-world applications, a more robust authentication system should be implemented (e.g., OAuth or JWT).

3. No User Roles: This API does not include user roles or permissions. Everyone with the correct token has access to all endpoints.

4. Basic Pagination: Pagination is implemented, but more advanced features like sorting or filtering could be added for better control over the data retrieval process.

5. Limited Search Functionality: The search functionality in `/books` only supports basic filtering by title and author. It does not support more complex searches (e.g., by genre or publication date).

6. No Error Handling for Invalid Input: Input validation (e.g., checking if required fields are provided) and error handling are minimal. This should be improved for production use to ensure the integrity of the data.

Dependencies:
- Flask (for creating the API)

License:
This project is licensed under the MIT License.
