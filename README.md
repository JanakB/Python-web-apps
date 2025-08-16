# Blog App (Twitter-like Social Network)

## 📌 Overview
This project is a **Twitter-like social network** built using **Python Django**.  
It allows users to make posts, follow other users, and interact with posts (like/unlike, edit, etc.).  

---

## 🚀 Features
- **New Post**: Signed-in users can create new posts.
- **All Posts**: Users can view all posts.
- **Profile Page**: Each user has a profile showing their posts, followers, and following count.
- **Following Page**: Users can view posts only from people they follow.
- **Pagination**: Maximum 10 posts per page with *Next* and *Previous* navigation.
- **Edit Post**: Users can edit their own posts.
- **Like/Unlike**: Users can like or unlike posts.

---

## ⚙️ Setup Instructions

### 1. Clone Repository
```bash
git clone https://github.com/your-username/blog-app.git
cd blog-app
````

### 2. Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate   # On Linux/Mac
venv\Scripts\activate      # On Windows
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run Database Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Create Superuser (Admin)

```bash
python manage.py createsuperuser
```

### 6. Run Development Server

```bash
python manage.py runserver
```

Now visit 👉 `http://127.0.0.1:8000/`

---

## 📡 API Documentation

### Authentication

* **Register User**

  * `POST /users/register/`
  * Request body:

    ```json
    {
      "username": "john_doe",
      "email": "john@example.com",
      "password": "password123"
    }
    ```
  * Response: `201 Created`

* **Login**

  * `POST /users/login/`
  * Request body:

    ```json
    {
      "username": "john_doe",
      "password": "password123"
    }
    ```
  * Response: `200 OK` (with session/cookie)

* **Logout**

  * `POST /users/logout/`
  * Response: `200 OK`

---

### Posts

* **Create Post**

  * `POST /posts/create/`
  * Request body:

    ```json
    {
      "content": "Hello Twitter-like app!"
    }
    ```
  * Response: `201 Created`

* **List All Posts**

  * `GET /posts/`
  * Response: List of posts (paginated, 10 per page)

* **Edit Post**

  * `PUT /posts/<post_id>/edit/`
  * Request body:

    ```json
    {
      "content": "Updated content here"
    }
    ```
  * Response: `200 OK`

* **Like Post**

  * `POST /posts/<post_id>/like/`
  * Response: `200 OK`

* **Unlike Post**

  * `POST /posts/<post_id>/unlike/`
  * Response: `200 OK`

---

### Profiles

* **User Profile**

  * `GET /users/<username>/`
  * Response:

    ```json
    {
      "username": "john_doe",
      "followers": 5,
      "following": 3,
      "posts": [...]
    }
    ```

* **Follow User**

  * `POST /users/<username>/follow/`
  * Response: `200 OK`

* **Unfollow User**

  * `POST /users/<username>/unfollow/`
  * Response: `200 OK`

---

## 📷 Screenshots
Welcome page
<img width="1360" height="663" alt="image" src="https://github.com/user-attachments/assets/4e7d2fdc-49c3-4687-a094-dc4849fb2f2f" />

Admin Login page
<img width="478" height="440" alt="image" src="https://github.com/user-attachments/assets/6ed5342c-ac3b-4f27-8c9e-c1f5b43c2721" />


User register page
<img width="447" height="503" alt="image" src="https://github.com/user-attachments/assets/15c0e837-48be-4287-b4ef-2cb5d71e9cbe" />

Dashboard
<img width="719" height="677" alt="image" src="https://github.com/user-attachments/assets/646a88da-31c7-4883-9747-de50d0d1a868" />

follow page
<img width="590" height="273" alt="image" src="https://github.com/user-attachments/assets/8d07fbee-7b8c-42b0-81f9-495e31a8f235" />

post options
<img width="1337" height="224" alt="image" src="https://github.com/user-attachments/assets/64b04aca-9bc4-4b44-966d-2ae6d74c42ac" />

