# virtual-library

## Requirements (software)
Python 3.8+

## Installation 
- Create a Virtual Environment and Activate it.
- Install the project dependencies by running following command
```
pip install -r requirements.txt
```
- Run the following commands to create database tables(SQLite will be automatically generated, to use anything else, change database info in settings.py)
```
python manage.py migrate
```
## How to Run the Project
- Run the following command
```
python manage.py runserver 
```
- Now, visit http://127.0.0.1:8000/ to access the website.
