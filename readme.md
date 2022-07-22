______________________________________________________________________________________________________

DESCRIPTION:
Inventory Management System
______________________________________________________________________________________________________

SETUP:

1. Python -3.8.10
2. clone the repository:
3. Create Virtual environment

    install : 
    python3 -m pip install --user virtualenv
    create virtual environment command : virtualenv venv

4. Activate virtual environment : 
    source venv/bin/activate

5. install Django==3.2.4

6. Migrations
    python manage.py makemigrations
    python manage.py migrate

7. For the first time create super user
    python manage.py createsuperuser

8. Run django project
    python manage.py runserver

9. for access admin console enter below url in browser and enter credentials
    http://127.0.0.1:8000/admin/

10. for checking unit test cases run below command
    python manage.py test