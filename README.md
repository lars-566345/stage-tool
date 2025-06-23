
# stage-tool

## Environment variables needed to run the application

### Django

> *Put the .env file in the following location: "/backend/mysite/.env"*

 - DJANGO_SECRET_KEY
 - DB_ENGINE ("sqlite" or "postgreql")
 - DB_NAME
 - DB_USER
 - DB_PASSWORD
 - DB_HOST
 - DB_PORT
 - DEBUG
 - DJANGO_LOGGING_LEVEL
 - DJANGO_CORE_APP_LOGGING_LEVEL
 - DJANGO_SUPER_USER_PASSWORD

### React

> *Put the .env file in the following location: "/frontend/.env"*

 - VITE_API_URL

## Get started
1. Open a terminal
2. Create a venv (python3 -m venv venv)
3. Activate the venv
4. Install the requirements for the backend
5. Run the custom setup django management command (python manage.py create_test_environment)
6. Navigate to mysite
7. Run "python manage.py runserver"
8. Open a second terminal
9. Install requirements for frontend
10. Run "npm run dev"
