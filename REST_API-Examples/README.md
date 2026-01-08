## REST API – Fundamentals

####  What is an API?


An API (Application Programming Interface) is a way for two applications to talk to each other.

📌 **Example:**

* A mobile app requests data
* A server sends data back


#### What is a REST API?


**REST (Representational State Transfer)** is an architectural style for designing networked applications. A REST API is a web service that follows REST principles, allowing different systems to communicate over HTTP.

#### Key Principles of REST

- **Stateless** : Each request contains all necessary information 
- **Client-Server** : Separation of concerns between client and server
- **Cacheable**: Responses can be cached to improve performance
- **Uniform Interface**: Consistent way to interact with resources
- **Layered System**: Architecture can be composed of multiple layers
- **Response**: Data is usually sent in JSON format





#### What is Client–Server Architecture?


* Client sends request (browser, app)
* Server processes request
* Server sends response

---
### API Components

#### What are the main components of an API request?

**Answer:**

1. Endpoint (URL)
2. HTTP method
3. Headers
4. Query parameters
5. Path parameters
6. Request body


#### 📌  What is JSON?

**Answer:**
JSON (JavaScript Object Notation) is a lightweight data format used to exchange data between client and server.



### HTTP Methods

HTTP methods define the action to be performed on data.

| Method | Purpose             | Example        |
| ------ | ------------------- | -------------- |
| GET    | Fetch data          | Get users      |
| POST   | Create data         | Add user       |
| PUT    | Update full data    | Update profile |
| PATCH  | Update partial data | Update email   |
| DELETE | Delete data         | Remove user    |

#### Example URL Structure

```
GET    /api/v1/users           # Get all users
GET    /api/v1/users/123       # Get user with ID 123
POST   /api/v1/users           # Create new user
PUT    /api/v1/users/123       # Update user 123
DELETE /api/v1/users/123       # Delete user 123
GET    /api/v1/users/123/posts # Get posts for user 123
```

**Examples** :

#### GET
Retrieve data from the server. Should not modify any data.

**Example:**
```http
GET /api/users/123
```
**Response:**
```json
{
  "id": 123,
  "name": "John Doe",
  "email": "john@example.com"
}
```

#### POST
Create new resources on the server.

**Example:**
```http
POST /api/users
Content-Type: application/json

{
  "name": "Jane Smith",
  "email": "jane@example.com"
}
```
**Response:**
```json
{
  "id": 124,
  "name": "Jane Smith",
  "email": "jane@example.com",
  "created_at": "2024-01-08T10:30:00Z"
}
```

#### PUT
Update or replace an entire resource.

**Example:**
```http
PUT /api/users/123
Content-Type: application/json

{
  "name": "John Updated",
  "email": "john.updated@example.com"
}
```
**Response:**
```json
{
  "id": 123,
  "name": "John Updated",
  "email": "john.updated@example.com",
  "updated_at": "2024-01-08T10:35:00Z"
}
```

#### PATCH
Partially update a resource.

**Example:**
```http
PATCH /api/users/123
Content-Type: application/json

{
  "email": "newemail@example.com"
}
```
**Response:**
```json
{
  "id": 123,
  "name": "John Doe",
  "email": "newemail@example.com",
  "updated_at": "2024-01-08T10:40:00Z"
}
```

#### DELETE
Remove a resource from the server.

**Example:**
```http
DELETE /api/users/123
```
**Response:**
```json
{
  "message": "User deleted successfully"
}
```
----

### HTTP Status Codes


Status codes indicate the result of an API request.

| Code | Meaning            |
| ---- | ------------------ |
| 200  | Request successful |
| 201  | Resource created   |
| 400  | Bad request        |
| 401  | Unauthorized       |
| 403  | Forbidden          |
| 404  | Not found          |
| 500  | Server error       |


### Common Response Formats

#### Success Response
```json
{
  "status": "success",
  "data": {
    "id": 1,
    "name": "Example"
  }
}
```

#### Error Response
```json
{
  "status": "error",
  "message": "Resource not found",
  "code": 404
}
```




### Authentication

#### API Key Authentication
```http
GET /api/users
Authorization: Bearer YOUR_API_KEY
```

----


### Python `requests` Library


`requests` is a Python library used to send HTTP requests easily.


**Installation:**

```bash
pip install requests
```


#### Free API :

**JSONPlaceholder API**

* Free
* No authentication
* Fake data for testing

Base URL:

```
https://jsonplaceholder.typicode.com
```






