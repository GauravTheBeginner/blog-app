# Blog App README

## Overview

This is a simple blog application developed to practice CRUD (Create, Read, Update, Delete) functionality in web development. It allows users to create, read, update, and delete blog posts.

## Features

- **Create**: Users can create new blog posts with a title, content.
- **Read**: Users can view existing blog posts with their titles, content.
- **Update**: Users can edit their own blog posts to modify the title, content, or image.
- **Delete**: Users can delete their own blog posts permanently.


## Technologies Used

- **Backend**: Python, Django REST framework
- **Database**: sqlite3

## Installation

To run this application on your local machine, follow these steps:

1. Clone the repository:
    ```bash
    git clone https://github.com/GauravTheBeginner/blog-app.git
    ```

2. Install Python dependencies:
    ```bash
    cd blog-app/mysite
    pip install -r requirements.txt
    ```

3. Apply migrations and set up the database:
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

4. Run the backend server:
    ```bash
    python manage.py runserver
    ```

5. Access the application in your web browser at [http://127.0.0.1:8000/api/blogposts/](http://127.0.0.1:8000/api/blogposts/).
   
## Contributions

Contributions are welcome! If you find any bugs or have suggestions for improvement, feel free to open an issue or create a pull request.

## License

This project is licensed under the [MIT License](LICENSE).
