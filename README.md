# 📚 Library Management System API

This is a **Library Management System** built using **Django Rest Framework (DRF)**. It provides a set of RESTful API endpoints to manage books, authors, library members, and book borrowing/return functionalities. It also includes **Swagger API documentation** and **JWT authentication** using **Djoser**.

---

## 🚀 Features

- 📖 Manage Books and Authors  
- 👤 Register and Manage Library Members  
- 🔄 Borrow and Return Books  
- 🔐 Authentication using JWT (via Djoser)  
- 📑 Auto-generated Swagger documentation  

---

## 🛠️ Tech Stack

- Python 3.x  
- Django 4.x  
- Django REST Framework  
- Djoser (for authentication)  
- Simple JWT  
- drf-yasg (for Swagger documentation)

---


## 🧪 API Documentation

Interactive Swagger UI is available at:

🔗 [http://localhost:8000/swagger/](http://localhost:8000/swagger/)

It provides a complete overview of all available endpoints, request parameters, and responses in an easy-to-use interface.


ReDoc UI:
🔗 [http://localhost:8000/redoc/](http://localhost:8000/redoc/)


## 🔐 Authentication

Authentication is handled using **Djoser** with **JWT**.  
- Login to receive access and refresh tokens.
- Pass the token in the `Authorization` header as:

```http
Authorization: Bearer <your_access_token>


library_management/
├── books/             # App for books & authors
├── members/           # App for library members
├── borrow/            # App for borrow/return
├── users/             # Custom user and Djoser integration
├── settings.py
├── urls.py
└── ...

----


