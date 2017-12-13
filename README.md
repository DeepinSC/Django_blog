# Django_blog
Based on Django REST Framework, Django Rest Blog is the blog website which you can use its api to create/edit/delete blogs on. 

### INSTALLATION
1. Install python3.x in your system;
2. `git` and `clone` this repository and `cd` your path (where the same folder as LICENSE);
3. Use `pip install virtualenv` to install virtualenv in your system;
4. Use `virtualenv env` to create a new env;
5. `cd django_blog`;
6. Use `pip install -r requirements/base.txt` to install requirements;
7. `cd MLBlog`;
8. `python manage.py makemigrations`;
9. `python manage.py migrate`;

## RUN SERVER
Run server by typing `python manage.py runserver` and you can operate on `http://127.0.0.1:8000/blogs/`.



